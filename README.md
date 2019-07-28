# 추천 시스템 조사 및 구축 방법에 대한 조사
## 추천 방법
- 사용자에게 적합한 상품
- 다양한 상품 추천
- 접하지 못한 상품 추천
- 예상치 못한 상품 추천

## 추천 시스템의 종류
### Collaborative filtering recommender systems
- user base
- item base
* cold start 문제 발생
### Content-based recommender systems
- Eucleaean Distance
> 다차원의 공간 좌표에서 두점의 거리를 재는 방법
> 두 문서븨 백터의 값이 양적 균등하지 않은 경우 유클리디안 거리는 합리적이지 않다고 판단. 
- Cosine Simularity
> 원점으로 부터의 발생하는 성향 분석에 유리
- Pearson Correlation
### Hybrid recommender systems
#### 하이브리드의 방법
- 여러 추천기법의 결과를 가중 형균합을 통해 하나의 결과로 도출.
하나의 추천 기법을 선택하거나 각 기법의 변수를 다양하게 혼합하여 활용하는 방법
- 내용기반 추천에 사용되는 정보를 협업 필터링을 통해 활용하는 형태
- 협업필터링의 특징을 내용기반에 입히는 방법
- 두모델을 동시에 고려하는 단일 모델
### Context-aware recommender systems


### Model-based recommender systems
- TF-Ranking 
    > 정보검색(IR)과 추천(Recommendation)에서 사용 가능<br />
      LTR 분야<br />
      Light GBM 같은 기존 모델이 있었으나 대용량 처리를 위해 TF-Ranking 이 나왔음<br />
      Easy-to-use
      tensorflow-ranking을 이용한 개발 가능
    + https://www.youtube.com/watch?v=ldWy3885qXc

- 협업필터링과 스태킹 모형을 이용한 상품추천시스템 개발
    > 실험 결과는 제안 모형이 단순히 협업필터링만을 이용한 추천시스템과 스태킹 모형의 적용 없이 기계학습 모 델로 구축한 추천시스템에 비해 추천 성능이 향상됨을 보였다
    + http://www.ndsl.kr/ndsl/commons/util/ndslOriginalView.do?dbt=JAKO&cn=JAKO201918454913903&oCn=JAKO201918454913903&pageCode=PG11&journal=NJOU00576176

- 영화추천을 위한 합성곱 신경망
    > 연구에서 제안기법(wCNN)의 추천정확도 평가를 위해 선행연구[14]의 기법인 wDNN과 비교하였다. 제안 기법은 전통적 사용자 기반 협업필터링 방식(CF)에 비해 영화추천시스템의 정확도를 크게 개선하였다. 또한 심층신경망을 이용한 기법(wDNN)에 비해서도 정확도가 개선되었다.
    + http://www.ndsl.kr/ndsl/commons/util/ndslOriginalView.do?dbt=JAKO&cn=JAKO201911338887828&oCn=JAKO201911338887828&pageCode=PG11&journal=NJOU00557104
    + http://www.ndsl.kr/ndsl/commons/util/ndslOriginalView.do?dbt=JAKO&cn=JAKO201913649329455&oCn=JAKO201913649329455&pageCode=PG11&journal=NJOU00431883


## 평가방법
> F1 Score

## 이후 연구 목표
- 빅데이터 분석 기법을 이용한 실시간 대중교통 경로 안내 시스템의 설계 및 구현
    +  http://www.ndsl.kr/ndsl/commons/util/ndslOriginalView.do?dbt=JAKO&cn=JAKO201909469054746&oCn=JAKO201909469054746&pageCode=PG11&journal=NJOU00292001

- 자동차 번호판 인식기 - Python, 이미지 프로세싱
    > 이미지 프로세싱과 AgensGraph 의 데이터 시각화 이미지를 결합한 실시간 분석
    + https://github.com/kairess/movie_recommendation_engine.git


## 테스트가 필요한 내용들
### 앙상블 방법론
#### Bagging
> Bagging은 샘플을 여러번 뽑아 각 모델을 학습시켜 결과 집계(Aggregation) 하는 방법
#### Boosting
> Bagging 은 일반적인 모델을 만드는데 집중되었다면 Boosting 은 맞추기 어려운 문제를 맞추는데 초점이 맞춰져 있다
1. Single > 1 iteration
2. Bagging > Parallel
3. Boosting > Sequential
- AdaBoost, XGBoot, GradientBoost 등 다양한 모델이 있다. 그중에서 XGBoost는 강력한 성능을 보여준다.<br />
  최근 Kaggle 에서 대부분의 우승 알고리즘이기도 하다.
#### Stacking
> Meta Modeling 이라고 불리기도 하는 이 방법은 "Two heads are better than one" 이라는 아이디어에서 출발<br />
  두개의 다른 모델을 조합하여 최고의 성능을 내는 모델을 생성<br />
  여기서 사용되는 모델은 SVM, RendomForest, KNN 등 다양한 알고리즘을 사용.<br />
  어마어마한 연산량