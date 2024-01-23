# 2023 BigContest 비정형데이터 분
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

&nbsp;&nbsp;&nbsp;&nbsp; 2023 Bigcontest 여러 분야중에 비정형 데이터 분석 분야에 참가하였다. 비정형 데이터 분석 분야 주제는 **씨름 영상데이터를 활용한 씨름 영상 분석모델 도출 및 활용방안 제시**로 분석 뿐만 아니라 서비스 방면도 고려해야 한다. 주어진 데이터는 약 2시간 정도의 씨름 유튜브 영상과 경기 기록 데이터, 씨름 기술 소개 영상 3개였다. 해당 데이터를 가지고 분석을 진행하였다. 

![스크린샷 2024-01-23 235919](https://github.com/yugwangyeol/2023-BigContest/assets/72298825/2c7620a4-4a7a-4442-bc84-4a46e7cb20a1) | ![스크린샷 2024-01-23 235937](https://github.com/yugwangyeol/2023-BigContest/assets/72298825/948a7f9a-1882-455c-8b2e-77c2064605d3). ---|---|



<br/>

## 5-1. 예선 Process

### ch.1 EDA  

- 나라별, 항구별, 배의 타입별 등등의 특성 확인
- 각 배의 카테고리컬한 피처들의 조합의 통계값들 확인
- **기상정보에 대한 Target값 로직 파악**

---

### ch.2 Feature Engineering  

- 시간 feature들은 inherently cyclical 하다는 특징을 활용하기 위해 sin/cos 변환
- 특정 피처들의 target 값의 평균으로 파생 변수 생성
- Clustering

---

### ch.3 Modeling

- Autogluon
- 기상정보에 따른 후처

<br/>

## 5-2. 본선 Process

### ch.1 EDA  

- Signal, Sensor 관계 파악
- **Signal, Sensor를 통한 건설 기계 추정**

---

### ch.2 Feature Engineering  

- Fourier transform 등 다양한 피쳐 변환
- 부하 토크, 동적 반응 피쳐 생성
- ML에 맞게 Widow를 통한 피쳐 변환

---

### ch.3 Modeling

- LSTM
- CNN_LSTM
- Autogulon

<br/>

## 6. 프로젝트 팀원 및 담당 역할

**[팀원]**

- 학부생 3명

**[담당 역할]**

- 데이터 전처리 및 EDA
- 인사이트 도출
- 모델링&알고리즘 개발
- 발표 자료 제작

<br/>

## 6. 발표 자료&참고 자료

[HD-AI-CHALLENGE DACON](https://dacon.io/competitions/official/236158/overview/description)  
[HD AI Challenge 본선 발표 자료](https://github.com/yugwangyeol/HD-AI_Challenge/blob/main/Presentation/%5BHD%5D%ED%98%84%EB%8C%80_%EC%B5%9C%EC%A2%85.pdf)
