# K-Nearest Neighbor Algorithm
>  K-최근접이웃(K-Nearest Neighbor, KNN) 알고리즘

## 모델 개요
> Instance-based Learning
> KNN은 새로운 데이터가 주어졌을 때 기존 데이터 가운데 가장 가까운 k개 이웃의 정보로 새로운 데이터를 예측하는 방법론
> k의 값은 홀수

## 거리 지표
> KNN은 거리 측정 방법에 따라 그 결과가 크게 달라지는 알고리즘
- Euclidean Distance
- Manhattan Distance
- Mahalanobis Distance
- Correlation Distance
- Rank Correlation Distance

## best K 찾기
> 학습데이터로 k 를 1부터 n개 까지 1씩 증가시키면서 오분류율을 점검
> 테스트 데이러로 k 를 1부터 n개 까지 1씩 증가시키면서 오차율을 비교
> 두 선의 거리가 가장 가까운 지점을 찾아서 선택

## KNN 의 장점과 한계
### 장점
> 데이터 노이즈의 영향을 크게 받지 않으며, 특히 Mahalanobis Distance와 같이 데이터의 분산을 고려할 경우 강건함
> 학습 데이터의 수가 많을 경우 효과적임

### 한계점
> k 값을 설정해야함
> 어떤 거리 척도가 분석에 적합한지 불분명하며, 따라서 데이터의 특성에 맞는 알고리즘을 선정해야함
> 새로운 관측자와 각각의 학습데이터 간 거리를 전부 측정해야 하므로 계산사간이 오래 걸리는 단점이 있음

## Weight KNN
> k 거리 정보에 가중치를 주어 분류


참고
https://ratsgo.github.io/machine%20learning/2017/04/17/KNN/
https://www.youtube.com/watch?v=W-DNu8nardo