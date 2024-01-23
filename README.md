# 2023 BigContest 비정형데이터 분야 
씨름 영상데이터를 활용한 씨름 영상 분석모델 도출 및 활용방안 제시

<br/>

## 1. 배경 & 목적
 
- 씨름 영상데이터를 활용한 씨름 영상 분석모델 도출 및 활용방안 제시
- 참가팀이 직접 문제를 만들고 해결해 나가는 과정을 스토리텔링
  - 영상 데이터 전처리 및 분석 방법론
  - 영상 기반 씨름 경기 분석
  - 데이터 분석 모델의 서비스 활용 방안
  - 분석 모델의 통계적 결과 도출 방안 제시
- K-씨름 서비스 컨텐츠 창출

<br/>

## 2. 주최/주관 & 팀원 & 성과

- 주최: 과학기술정보통신부, NIA 한국지능정보사회진흥원
- 주관: 스포츠투아이,예술의 전당, Finda, DESILO, KAIT 한국정보통신진흥협회 등
- 후원: KBD 빅데이터포럼
- 참가 대상: 전국 대학(원)생(휴학생 포함) - 전일제 대학(원)생만 해당
- 성과 : 2023 빅콘테스트 비정형데이터 분석 부문 최우수상 수상 (1등)
- 특허 : 현재 진행 중
<br/>

![스크린샷 2024-01-23 234949](https://github.com/yugwangyeol/2023-BigContest/assets/72298825/a0c2b163-04a4-43a1-8d69-1c6fc017fda3)

<br/>

## 3. 프로젝트 기간

- 제출마감: 2023년 9월 27일
- 1차 서류 심사 결과: 2023년 11월 3일
- PT 발표 심사 : 2023년 11월 14일
- 2차 PT 발표 심사 결과: 2022년 12월 9일
- 시상식 : 2023년 12월 13일

<br/>

## 4. 프로젝트 소개

&nbsp;&nbsp;&nbsp;&nbsp; 2023 Bigcontest 비정형 데이터 분석 분야 주제는 **씨름 영상데이터를 활용한 씨름 영상 분석모델 도출 및 활용방안 제시**로 분석 뿐만 아니라 서비스 방면도 고려해야 한다. 주어진 데이터는 약 2시간 정도의 씨름 유튜브 영상과 경기 기록 데이터, 씨름 기술 소개 영상 3개였다. 해당 데이터를 가지고 분석을 진행하였다. 

<br/>

<img src="https://github.com/yugwangyeol/2023-BigContest/assets/72298825/2c7620a4-4a7a-4442-bc84-4a46e7cb20a1"  width="450"/><img src="https://github.com/yugwangyeol/2023-BigContest/assets/72298825/948a7f9a-1882-455c-8b2e-77c2064605d3"  width="450"/>

<br/>

&nbsp;&nbsp;&nbsp;&nbsp; 생소한 씨름이라는 도메인을 공부하며, 한국 씨름의 하락세의 원인으로 위와 같은 3가지 문제점을 선정하였다. 그리고 이를 해결 하기 위해 **AI 기술을 활용한 선수 체력 지표 개발 및 콘텐츠화**를 주제로 진행하였다.

<br/>

<img src="https://github.com/yugwangyeol/2023-BigContest/assets/72298825/aa8b8064-e3e2-4e1a-8ca4-c74396140e5c"  width="450"/><img src="https://github.com/yugwangyeol/2023-BigContest/assets/72298825/b8b271a1-add4-4d6e-b961-6c6aca1c9a6c"  width="450"/>

<br/>

&nbsp;&nbsp;&nbsp;&nbsp; 이를 해결 하기 위해 기존 데이터로 부터 키, 몸무게, 샅바시간, 경기시간, 휴식시간, 라운드를 라벨링 및 데이터를 추출하였다. 그리고 **STT기술을 활용하여 해설진의 목소리로부터 선수들의 기술횟수와 Object Tracking을 활용하여 선수들의 움직임 거리**를 추출 하였다.

<br/>

<img src="https://github.com/yugwangyeol/2023-BigContest/assets/72298825/0d016a54-7e07-42ec-9a2a-b07023356877"  width="900"/>  

<br/>

&nbsp;&nbsp;&nbsp;&nbsp; 생성된 변수들을 가지고 누적 경기값을 Target값으로 회귀 분석 통해 선수들의 체력 지표를 생성하였다.

<br/>

<img src="https://github.com/yugwangyeol/2023-BigContest/assets/72298825/be638113-654a-49ff-a761-c378795e72f5"  width="450"/><img src="https://github.com/yugwangyeol/2023-BigContest/assets/72298825/ed5ef421-2466-455b-9344-7846e5e581dd"  width="450"/>
<img src="https://github.com/yugwangyeol/2023-BigContest/assets/72298825/82454229-8026-4519-b964-3b9ab786ad51"  width="450"/><img src="https://github.com/yugwangyeol/2023-BigContest/assets/72298825/c1ff0a56-c920-47c6-8d9a-8f45c2359eeb"  width="450"/>

<br/>

&nbsp;&nbsp;&nbsp;&nbsp; 이를 통해 중계화면 사이드바에 선수들의 체력 지표 표시, 선수 소개 시 남은 체력 표시, 게임과 같은 효과와 같은 새로운 콘텐츠와 실시간으로 입력 가능한 서비스를 제안하였다.

<br/>

## 5. 예선 Process

### ch.1 Data Preparation 

- 추가 영상 데이터 수집
- 영상 분할
- 해설진 음성 추출
- 선수 데이터 수집
- 기술 사전 생성
- 데이터 변수 라벨

---

### ch.2 Modeling  

- KeyPoint Detection (YoloV8, RPM Pose)
- Object Tracking (CoTracker, Pips)
- STT (SeamlessM$T, Whisper)

---

### ch.3 Post-processing

- STT 기술 사전 적용
- Object Tracking Zoom In/Out 탐지

### ch.4 Regression

- 변수 설정
- Stats model 생성
- 체력 지표 계산
- EDA

### ch.5 Content

- 경기 중 체력 현황 사이드바
- 경기 시작 전 선수 소개 체력 지표 표시
- 경기 시 선수 머리 위에 체력 게이지 표시
- 실시간 방식 제안

<br/>

## 6. 프로젝트 팀원 및 담당 역할

**[팀원]**

- 학부생 4명

**[담당 역할]**

- 

<br/>

## 7. 발표 자료&참고 자료

[2023 Bigconetest 발표 자료](https://github.com/yugwangyeol/2023-BigContest/blob/main/Presentation/%EB%B9%84%EC%A0%95%ED%98%95%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%B6%84%EC%84%9D%EB%B6%84%EC%95%BC_%ED%8C%80_E1I3S4T3F1J4.pdf)

## 8. 증빙 자료
![스크린샷 2024-01-23 234949](https://github.com/yugwangyeol/2023-BigContest/assets/72298825/a0c2b163-04a4-43a1-8d69-1c6fc017fda3)
![KakaoTalk_20240124_003630353](https://github.com/yugwangyeol/2023-BigContest/assets/72298825/d54bdd2b-a690-4d61-bebd-7d96087df1d6)


