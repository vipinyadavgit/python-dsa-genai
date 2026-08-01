### 1. Identify the Problem Type

| Output Type         | Problem Type     | Goal                       |
|---------------------|------------------|----------------------------|
| **Numeric value**   | [Regression]     | Predict continuous numbers |
| **Category/Label**  | [Classification] | Predict discrete classes   |
| **Groups/Patterns** | [Clustering]     | Group unlabeled data       |
| **Trial & Reward**  | [Reinforcement]  | Learn optimal actions      |


### 2️. Choose Candidate Algorithms

| Problem Type       | Common Algorithms                                                                                               | Example Use Case                     |
|--------------------|:----------------------------------------------------------------------------------------------------------------|--------------------------------------|
| **Regression**     | [Linear Regression], [Polynomial Regression], [Decision Tree Regression], [Random Forest Regression], [XGBoost] | Predict house prices, forecast sales |
| **Classification** | [Logistic Regression], [Decision Tree], [Random Forest], [SVM], [KNN], [Naive Bayes]                            | Spam detection, churn prediction     |
| **Clustering**     | [K-Means], [Hierarchical Clustering], [PCA], [Association Rules]                                                | Customer segmentation                |
| **Reinforcement**  | [Q-Learning], [SARSA], [DQN], [Policy Gradient]                                                                 | Game AI, self‑driving cars           |


### 3. Pick the Right Evaluation Metric

| Problem Type       | Key Metrics                                   | When to Use                                                     |
|--------------------|-----------------------------------------------|-----------------------------------------------------------------|
| **Regression**     | [MAE], [MSE], [RMSE], [R² Score]              | MAE/RMSE → measure error size; R² → explain variance            |
| **Classification** | [Accuracy], [Precision], [Recall], [F1‑Score] | Accuracy → balanced data; Precision/Recall/F1 → imbalanced data |


### 4. Match Metric to Business Impact

| Scenario                   | Best Metric | Reason                         |
|----------------------------|-------------|--------------------------------|
| **House price prediction** | RMSE        | Average error in same units    |
| **Sales forecasting**      | MAE         | Easy to interpret for business |
| **Energy consumption**     | R²          | Explains variance              |
| **Employee attrition**     | F1‑Score    | Balances precision & recall    |
| **Fraud detection**        | Recall      | Missing fraud is costly        |
| **Spam filtering**         | Precision   | Avoid false positives          |
| **Medical diagnosis**      | Recall      | Missing disease is dangerous   |
| **Sentiment analysis**     | Accuracy    | Balanced classes               |


### 5.  Decision Checklist (Quick Flow)

Is output numeric? → Regression → MAE/RMSE/R²

Is output categorical? → Classification →

Balanced → Accuracy

Imbalanced → Recall / Precision / F1

Is data unlabeled? → Clustering → K‑Means, PCA

Is learning by reward? → Reinforcement → Q‑Learning, DQN

--------------------------------------------------------------------------------------------------------------------------

✅ In Short
--------------
Regression → MAE, RMSE, R²

Classification → Accuracy, Precision, Recall, F1

Clustering → Silhouette Score, Davies–Bouldin Index

Reinforcement → Reward Function (custom metric)

------------------------------------------------------------------------------------------------------------------------

###     🧭 Quick Reference

>   Regression → Predict numbers → Linear Regression, Random Forest Regression → Metrics: MAE, RMSE, R².

>   Classification → Predict categories → Logistic Regression, Random Forest, SVM → Metrics: Accuracy, Precision, Recall, F1‑Score.

>   Clustering → Group unlabeled data → K‑Means, PCA → Metrics: Silhouette Score, Davies–Bouldin Index.

>   Reinforcement → Learn by reward → Q‑Learning, DQN → Metric: Reward Function.