# RecommendSystem
## 테스트가 필요한 내용들
### 앙상블 방법론
#### Bagging
> Bagging은 샘플을 여러번 뽑아 각 모델을 학습시켜 결과 집계(Aggregation) 하는 방법
#### Boosting
> Bagging 은 일반적인 모델을 만드는데 집중되었다면 Boosting 은 맞추기 어려운 문제를 맞추는데 초점이 맞춰져 있다
1. Single > 1 iteration
2. Bagging > Parallel
3. Boosting > Sequential
- AdaBoost, XGBoot, GradientBoost 등 다양한 모델이 있다. 그중에서 XGBoost는 강력한 성능을 보여준다.
    최근 Kaggle 에서 대부분의 우승 알고리즘이기도 하다.
#### Stacking
> Meta Modeling 이라고 불리기도 하는 이 방법은 "Two heads are better than one" 이라는 아이디어에서 출발
    두개의 다른 모델을 조합하여 최고의 성능을 내는 모델을 생성
    여기서 사용되는 모델은 SVM, RendomForest, KNN 등 다양한 알고리즘을 사용.
    어마어마한 연산량