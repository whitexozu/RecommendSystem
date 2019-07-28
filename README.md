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