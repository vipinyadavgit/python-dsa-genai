### Supervised Learning Algorithms (use labeled data)

Linear Regression → Predict continuous values (e.g., house prices).

Logistic Regression → Binary/multi-class classification (e.g., spam detection).

Decision Trees → Rule-based splits for classification/regression.

Random Forest → Ensemble of decision trees for higher accuracy.

Support Vector Machines (SVM) → Finds hyperplanes to separate classes.

K-Nearest Neighbors (KNN) → Classifies based on closest neighbors.

Naive Bayes → Probabilistic classifier, often used in text/spam filtering.

Gradient Boosting / XGBoost / LightGBM → Powerful ensemble methods for tabular data.

----------------------------------------------------------------------------------------------

### Unsupervised Learning Algorithms (use unlabeled data)

K-Means Clustering → Groups data into clusters.

Hierarchical Clustering → Builds nested clusters.

Principal Component Analysis (PCA) → Dimensionality reduction, visualization.

Autoencoders → Neural networks for feature learning and anomaly detection.

Association Rule Learning → Market basket analysis (e.g., “people who buy bread also buy butter”).

---------------------------------------------------------------------------------------------------

### Reinforcement Learning Algorithms (trial & error with rewards)

Q-Learning → Learns optimal actions via reward feedback.

SARSA → Similar to Q-learning but updates based on actual actions taken.

Deep Q-Networks (DQN) → Combines Q-learning with deep neural networks.

Policy Gradient Methods → Directly optimize decision policies.

------------------------------------------------------------------------------------------------

| Category            | Algorithms                                                                                   | Example Use Case                            |
|---------------------|----------------------------------------------------------------------------------------------|---------------------------------------------|
| **Supervised**      | Linear Regression, Logistic Regression, Decision Trees, Random Forest, SVM, KNN, Naive Bayes | Predicting house prices, spam detection     |
| **Unsupervised**    | K-Means, Hierarchical Clustering, PCA, Autoencoders, Association Rules                       | Customer segmentation, anomaly detection    |
| **Reinforcement**   | Q-Learning, SARSA, DQN, Policy Gradient                                                      | Self-driving cars, game AI                  |
| **Semi-Supervised** | Self-training, Semi-supervised SVMs, Graph-based                                             | Medical diagnosis with limited labeled data |

    Supervised → labeled data, prediction/classification.
    
    Unsupervised → unlabeled data, clustering/patterns.
    
    Reinforcement → trial & error with rewards.
    
    Semi-supervised → mix of labeled + unlabeled.

--------------------------------------------------------------------------------------------
🧭 Step 1: Identify the Type of Problem

--------------------------------
👉 In short:
--------------------------------
>   Predicting values → Regression.

>   Predicting categories → Classification.

>   Finding groups → Clustering.

>   Learning by trial & reward → Reinforcement.

------------------------------------------------------------------------------------------------
Regression → Predicting a continuous number.

Classification → Predicting categories/labels.

Clustering → Grouping unlabeled data.

Reinforcement → Learning by trial & reward.

------------------------------------------------------------------------------------------------

### 📘 Supervised Learning Examples

| Problem Statement                       | Algorithm             | Why                                              |
|-----------------------------------------|-----------------------|--------------------------------------------------|
| **Predict house prices**                | [Linear Regression]   | Output is continuous (price).                    |
| **Predict if a customer will churn**    | [Logistic Regression] | Binary classification (churn / not churn).       |
| **Loan approval decision**              | [Decision Tree]       | Rule-based, interpretable decisions.             |
| **Fraud detection in transactions**     | [Random Forest]       | Complex classification, robust against noise.    |
| **Handwriting recognition**             | [KNN]                 | Classifies based on similarity to known samples. |
| **Text spam filtering**                 | [Naive Bayes]         | Works well with word probabilities in text.      |
| **Image classification (cats vs dogs)** | [SVM]                 | Finds optimal boundary between classes.          |

------------------------------------------------------------------------------------------------------

### 📗 Unsupervised Learning Examples

| Problem Statement                                  | Algorithm           | Why                                  |
|----------------------------------------------------|---------------------|--------------------------------------|
| **Group customers by buying behavior**             | [K-Means]           | Clusters unlabeled data.             |
| **Reduce dataset dimensions for visualization**    | [PCA]               | Projects data into fewer dimensions. |
| **Market basket analysis (items bought together)** | [Association Rules] | Finds item co-occurrence patterns.   |

----------------------------------------------------------------------------------------------------------------------------------

###     📙 Reinforcement Learning Examples

| Problem Statement               | Algorithm         | Why                                   |
|---------------------------------|-------------------|---------------------------------------|
| **Self-driving car navigation** | [Q-Learning]      | Learns by trial & reward.             |
| **Game AI (chess, Go)**         | [Policy Gradient] | Optimizes strategies through rewards. |

---------------------------------------------------------------------------------------------------------------------------------------

### 🚀 Practical Rule of Thumb

Ask: What is the output?

-   Number → Regression.

-   Category → Classification.

-   Groups/patterns → Clustering.

-   Actions with feedback → Reinforcement.

Ask: Do I need interpretability or accuracy?
-   Interpretability → Decision Tree, Logistic Regression.
-   Accuracy/robustness → Random Forest, Gradient Boosting.

Ask: Is the dataset labeled?

-   Labeled → Supervised.
-   Unlabeled → Unsupervised.

--------------------------------
👉 In short:
--------------------------------
>   Predicting values → Regression.

>   Predicting categories → Classification.

>   Finding groups → Clustering.

>   Learning by trial & reward → Reinforcement.

    Numbers → Regression

    Categories → Classification

    Groups → Clustering

    Trial & reward → Reinforcement
------------------------------------------------------------------------------------------------------------------------
![img.png](img.png)