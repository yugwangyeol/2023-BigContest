# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.

# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.

import os
import cv2
import torch
import argparse
import numpy as np
import pandas as pd

from PIL import Image
from cotracker.utils.visualizer import Visualizer, read_video_from_path, cut_video, keypoint_extraction
from cotracker.predictor import CoTrackerPredictor

from mmpose.apis import MMPoseInferencer
from glob import glob

# 폴더에서 파일명을 불러오는 함수를 생성
def list_files_in_folder(folder_path):
    return os.listdir(folder_path)

# 사용하고자 하는 Device 설정
DEFAULT_DEVICE = ('cuda' if torch.cuda.is_available() else
                  'mps' if torch.backends.mps.is_available() else
                  'cpu')

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--video_path",
        help="거리를 계산하고자 하는 영상들이 담긴 폴더의 경로를 입력",
    )
    parser.add_argument(
        "--checkpoint",
        default="./checkpoints/cotracker_stride_4_wind_8.pth",
        help="cotracker 모델의 checkpoint의 파일 경로를 입력",
    )
    parser.add_argument(
        "--backward_tracking",
        action="store_true",
        help="point의 이동경로를 순방향이 아닌 양방향으로 계산할지에 대한 여부",
    )
    parser.add_argument(
        "--save_video",
        default=False,
        help='point의 이동 경로를 시각화한 영상을 저장할 지에 대한 여부'
    )

    # CLI에서 실행할 때 지정한 argument 변수들을 불러온다.
    args = parser.parse_args()

    # 폴더 안에 존재하는 영상들의 파일 명을 리스트로 저장
    file_list = list_files_in_folder(args.video_path)

    # 이동 거리를 저장하기 위한 빈 리스트 생성
    total_distance_list = []
    
    # keypoint를 추출하기 위한 모델을 생성
    inferencer = MMPoseInferencer(
    './checkpoints/rtmpose-m_8xb256-420e_coco-256x192.py',
    './checkpoints/rtmpose-m_simcc-aic-coco_pt-aic-coco_420e-256x192-63eb25f7_20230126.pth',
    device='cuda:0')
    
    # point를 tracking하기 위한 모델을 생성
    model = CoTrackerPredictor(checkpoint=args.checkpoint)
    model = model.to(DEFAULT_DEVICE)

    # 이동 거리를 계산하기 위한 파일들을 하나씩 불러와 계산
    for file_name in file_list:
        print('-' * 50)
        print('Start calculate distance')
        print('Video title : ', file_name)

        # 영상의 길이가 길어지게 되면 용량이 너무 커져 보유하고 있는 컴퓨팅 자원으로는 모델 실행이 불가능
        # 이를 위해 영상을 10초 단위로 잘라 저장
        # 10초씩 저장된 영상을 하나씩 불러와 거리를 측정하고 이를 하나로 합쳐 최종적으로 영상에서의 이동 거리를 측정

        # cut_video
        # 입력 : 
        # 이동 거리를 측정하고자 하는 전체 영상
        # 출력 : 
        # path_list -> 10초씩 분할된 영상의 파일 경로가 저장된 리스트
        # fps -> 영상의 초당 프레임
        path_list, fps = cut_video(args.video_path + file_name)
        print('Complete split video')

        # 10초씩 저장된 영상을 tracking 모델의 입력 형태로 변환한 형태를 저장하기 위한 빈 리스트 생성
        video_list = []

        # 10초 단위의 영상을 하나씩 불러와 형태 변환
        for split_path in path_list:
            # read_video_from_path
            # 입력 : 
            # 10초로 분할된 영상
            # 출력 : 
            # 영상을 frame 단위로 잘라 해당 frame을 np.array 형태로 저장한 array
            # shape -> (B, T, N, C)
            # B : 배치 사이즈, T : frame 번호, N : point의 인덱스 번호, C : point의 좌표(x, y)
            split_video = read_video_from_path(split_path)

            # np.array 를 torch.tensor로 변환
            split_video = torch.from_numpy(split_video).permute(0, 3, 1, 2)[None].float()
            video_list.append(split_video)

        # point의 이동 경로와 이를 시각화할 때 필요한 데이터를 저장하기 위한 빈 리스트 생성
        tracks_list, visibility_list = [], []
        
        # 최초 거리를 0으로 설정
        distance = 0
        
        # keypoint_extraction
        # 입력 : 
        # tracking 하고자 하는 영상, keypoint를 추출하는 모델
        # 출력 :
        # 영상 속에 존재하는 사람의 팔꿈치의 위치를 point로 저장한 리스트 출력
        # shape -> (4, 3) (point의 개수, 입력 프레임 번호 + point의 좌표)
        # 마지막 point는 zoom 여부를 판별하기 위한 point
        query_frame = keypoint_extraction(args.video_path + file_name, inferencer=inferencer)
        print('Keypoint extraction complete')

        # torch.tensor로 변환
        query_frame = torch.tensor(query_frame)
        query_frame = query_frame[None].to(DEFAULT_DEVICE)
        
        # 영상이 zoom-in인지 zoom-out인지를 판단하기 위한 flag
        zoom = True

        # 10초 단위로 분할된 영상을 1개씩 불러와 계산
        for idx, video in enumerate(video_list):
            video = video.to(DEFAULT_DEVICE)

            # model
            # 입력 :
            # video : 거리를 계산하고자 하는 영상
            # queries : 최초의 point 좌표를 입력
            # backward_tracking : 역방향으로 계산할지에 대한 여부
            # 출력 :
            # pred_tracks : 입력한 point의 이동 경로를 frame 단위로 저장
            # shape -> (B, F, N, C)
            # B : 배치 사이즈, F : 프레임 번호, N : point의 index 번호, C : point의 좌표(x, y)
            # pred_visibility : 해당 point를 시각화할지에 대한 여부를 저장
            # shape -> (B, F, N, 1)
            # B : 배치 사이즈, F : 프레임 번호, N : point의 index 번호, 1 : 시각화할지에 대한 True, False 값
            pred_tracks, pred_visibility = model(
                video,
                queries=query_frame,
                backward_tracking=args.backward_tracking,
            )
            print(f"video_{idx} computed")
            tracks_list.append(pred_tracks)
            visibility_list.append(pred_visibility)

            # tracks에 저장된 point의 경로를 frame 단위로 하나씩 계산
            for i in range(0, pred_tracks.shape[1] - 1):
                # zoom을 판단하기 위한 point가 이전 frame 대비 x 값이 5 이상 이동하였다면 zoom in에서 out으로 변경되었다 판단
                if pred_tracks[0, i+1, -1, 0] - pred_tracks[0, i, -1, 0] >= 5:
                    zoom = False 
                    print('zoom in -> zoom out')
                    continue
                
                # zoom을 판단하기 위한 point가 영상 밖으로 이동하였다면 zoom out에서 in으로 변경되었다 판단
                if pred_tracks[0, i, -1, 0] >= 0 and pred_tracks[0, i+1, -1, 0] < 0:
                    zoom = True 
                    print('zoom out -> zoom in')
                    # 최초의 zoom을 True로 설정하였기 때문에 거리 계산에 오류가 있었음
                    # 따라서, 이전에 0.6784를 곱해준 것을 다시 원래 스케일로 변환
                    distance *= 1 / 0.6784
                    continue
                
                # 다음 frame으로 point가 얼마나 이동했는지를 계산하기 위해 유클리드 거리를 계산
                delta_x = pred_tracks[0, i, :-1, 0] - pred_tracks[0, i+1, :-1, 0]
                delta_y = pred_tracks[0, i, :-1, 1] - pred_tracks[0, i+1, :-1, 1]
                distance_list = torch.sqrt(delta_x ** 2 + delta_y ** 2)

                if zoom:
                    # zoom in이 되었다면 out에 비교해 동일 픽셀을 이동해도 더 조금 이동하기 때문에 0.6784를 곱함
                    distance += float(sum(distance_list)) * 0.6784
                else:
                    distance += float(sum(distance_list))

            # 전체 영상을 10초 단위로 잘라 계산하고 있기 때문에 마지막 point 위치를 다음 영상에 그대로 입력해야 함
            # 따라서 마지막 frame에서의 point 좌표를 다음 영상에 입력으로 사용
            query_frame = pred_tracks[0, -1, :, :]
            zero_col = torch.zeros((query_frame.shape[0], 1), dtype=query_frame.dtype).to(DEFAULT_DEVICE)
            query_frame = torch.cat((zero_col, query_frame), dim=1)
            query_frame = query_frame[None]

        print('total distance : ', distance)
        total_distance_list.append(distance)

        # 영상에서 point의 이동 경로를 시각화한 영상을 저장
        if args.save_video:
            # 10초씩 분할되어 있던 경로를 하나로 합침
            pred_tracks = torch.cat(tracks_list, axis=1)
            pred_visibility = torch.cat(visibility_list, axis=1)
            video = torch.cat(video_list, axis=1)

            full_path = args.video_path + file_name.split("/")[-1]
            seq_name = full_path.split('/')[-1]

            # Visualizer
            # 시각화하기 위한 class
            # save_dir : 영상을 저장하고자 하는 폴더의 경로
            # pad_value : zoom을 판단하기 위한 point가 영상 밖으로 나갈 수 있기 때문에 이를 확인하기 위해 영상 주변을 padding하여 흰색으로 표현
            # linewidth : 이동 경로를 표현하는 선의 굵기
            # fps : 영상의 초당 frame 개수
            vis = Visualizer(save_dir="./saved_videos", pad_value=120, linewidth=3, fps=fps, tracks_leave_trace=-1)
            vis.visualize(video, pred_tracks, pred_visibility)

    # 파일 별 이동 거리를 저장하기 위한 데이터프레임 생성
    df = pd.DataFrame(columns=['file','distance'])
    df['file'] = file_list
    df['distance'] = total_distance_list
    df.to_csv('../Output/total_distance.csv', encoding='cp949', index=False)