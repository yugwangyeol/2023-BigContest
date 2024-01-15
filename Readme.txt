# Enviroment
OS : window 11
GPU : Nvidia Geforce RTX 4080
CUDA : 11.8

# Folder
CoTracker : Object Tracking을 위한 CoTracker 파일 모음
Data : Input Data 모음
Output : Output Data 모음
Stats : 통계 분석과 시각화를 위한 파일 모음
Whisper : 기술 추출을 위한 Whisper 파일 모음

# 실행 코드

##Co Tracker
1. cd "Co Tracker"
2. python demo.py --video_path "../Data/video/" --backward_tracking (--save_video True 필요시만, 필요한 영상만 하세요.)

##Whisper
1. whisper_inference.ipynb 실행

##Stats
1. stats_model.ipynb 실행
2. Visualization.ipynb 실행

