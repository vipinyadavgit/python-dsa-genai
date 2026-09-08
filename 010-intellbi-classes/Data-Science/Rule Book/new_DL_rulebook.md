# Deep Learning Rule Book â€” End-to-End Guide

Version: draft  
Purpose: Practical, runnable guide to build, evaluate, tune, save and deploy deep learning models for classification, regression and timeâ€‘series (RNN) problems. This document synthesizes general best practices and concrete patterns extracted from three example projects: an ANN churn classifier, a simple perceptron tutorial, and a Bikeâ€‘Demand RNN forecasting project.

<!-- The purpose line tells the reader what this document is for and why it exists. -->

---

## Quick summary â€” what this document contains
- An end-to-end checklist and practical instructions for building deep learning models.
- Target audiences: data scientists building Keras/TensorFlow models for tabular classification/regression and time-series forecasting.
- Includes runnable code patterns, common pitfalls, and a preâ€‘deployment checklist.

<!-- This summary helps the reader decide quickly whether the guide matches their task. -->

---

## 1) Project setup & reproducibility

- Recommended repository structure:
  - data/ (raw csv)
  - src/ (preprocess.py, model.py, train.py, predict.py)
  - models/ or artifacts/ (saved models & scalers)
  - notebooks/
  - README.md, pyproject.toml or requirements.txt
- Use a virtual environment (venv/conda) and a lockfile; keep dependency versions pinned.
- Set seeds for reproducibility:
  - numpy: `np.random.seed(42)`
  - tensorflow: `tf.random.set_seed(42)`
  - python `random.seed(42)`
- Log experiments (MLflow / Weights & Biases / basic CSV logs).

<!-- This section is needed so experiments can be repeated later with the same code, same dependencies, and the same random initialization. -->

---

## 2) Problem definition & metrics

- Decide problem type and primary metric before modeling:
  - Binary classification (churn): ROC-AUC, precision, recall, F1
  - Multi-class classification: accuracy, per-class precision/recall, macro/micro F1
  - Regression (demand forecasting): RMSE, MAE, MAPE, R2
  - Time-series forecasting: rolling validation; horizon-specific RMSE/MAPE
- Note operational constraints: latency, model size, inference environment.

<!-- Defining the task and metric early avoids optimizing for the wrong goal and makes later evaluation meaningful. -->

---

## 3) Data ingestion & validation

- Store raw data in `data/` and never overwrite it.
- Validate presence of required columns early and raise helpful errors.
- For time-series, parse datetime and sort by date.

<!-- This step protects the pipeline from missing files, renamed columns, or incorrect row ordering before training starts. -->

Example guard:

```python
from pathlib import Path
DATA_PATH = Path("data/bike.csv")
if not DATA_PATH.exists():
    raise FileNotFoundError(f"{DATA_PATH} missing")
```

<!-- This guard fails fast with a readable error instead of allowing later steps to break in less obvious ways. -->

---

## 4) Exploratory Data Analysis (EDA)

- High-level checks: `df.shape`, `df.info()`, `df.describe()`, `df.head()`
- Missing values: `df.isnull().sum()`
- Duplicates: `df.duplicated().sum()` â†’ drop if needed
- Univariate & bivariate visualizations: histograms, boxplots, correlations, pairplots
- Outliers: IQR method or domain-driven decisions
- Time-series: trend/seasonality plots, ACF/PACF

<!-- EDA is needed to understand data quality and spot patterns or problems before model building starts. -->

---

## 5) Preprocessing & feature engineering

- Split columns into numerical, categorical, and datetime groups.
- Missing value strategies:
  - Numeric: median (robust) or mean
  - Categorical: mode or explicit "missing" value
- Categorical encoding:
  - Low-cardinality: `OneHotEncoder(sparse=False)` for dense arrays
  - High-cardinality: frequency/target encoding or embeddings (preferred in neural nets)
- Scaling:
  - `StandardScaler` or `MinMaxScaler` (MinMax often used for RNNs and scaled targets)
  - Fit scalers on training data only and save them for inference
- Pipelines:
  - Use `ColumnTransformer` / `Pipeline` to encapsulate preprocessing

<!-- Preprocessing converts raw data into consistent model input and ensures the same transformations can be reused at inference time. -->

Important: `OneHotEncoder` default returns sparse matrices â€” convert to dense (`sparse=False`) before feeding into Keras.

---

## 6) Splitting data (train / val / test)

- Tabular problems: stratified split for classification (`train_test_split(..., stratify=y)`)
- Typical: 70â€“80% train, 20â€“30% test. Use validation split or a separate validation set.
- Time-series: do not random split.
- Use chronological split and prefer walk-forward (rolling-origin) validation for robust estimates.

<!-- Proper splitting keeps evaluation honest by ensuring the model is tested on data it did not effectively learn from. -->

---

## 7) Model choices & architecture patterns

A. Dense feedforward models (tabular)
- Input: preprocessed feature vector
- Hidden layers: start small (e.g., 64 â†’ 32), add `BatchNormalization()` and `Dropout()` if needed
- Output/activation/loss:
  - Binary: `Dense(1, activation='sigmoid')` + `binary_crossentropy`
  - Multi-class: `Dense(n_classes, activation='softmax')` + `categorical_crossentropy`
  - Regression: `Dense(1, activation='linear')` + `MSE` or `MAE`

B. RNNs / LSTMs / GRUs (time-series)
- For short sequential patterns `SimpleRNN` might suffice; for long-range dependencies prefer `LSTM` or `GRU`.
- Stacked RNNs: set `return_sequences=True` on all but the last recurrent layer.
- Scale inputs and targets; create sliding windows for sequences (e.g., last 7 days â†’ predict next day).

C. Embeddings for categorical features
- Map categories to integer IDs and use `Embedding` layers in Keras for high-cardinality categorical variables.

<!-- This section matches the architecture to the data type so the model design is deliberate rather than arbitrary. -->

---

## 8) Keras model factory & training template

- Use a builder function for reproducibility and for hyperparameter tuning.

<!-- A model factory keeps the architecture in one place, which makes experiments easier to reproduce and tune. -->

Example builder:

```python
def build_model(input_dim, hidden_layers=[64,32], activation='relu', output_activation='sigmoid', lr=1e-3, dropout=0.0):
    model = Sequential()
    model.add(Input(shape=(input_dim,)))
    for units in hidden_layers:
        model.add(Dense(units, activation=activation))
        if dropout:
            model.add(Dropout(dropout))
    model.add(Dense(1, activation=output_activation))
    model.compile(optimizer=tf.keras.optimizers.Adam(lr), loss=LOSS, metrics=METRICS)
    return model
```

<!-- This builder centralizes the model definition so it can be reused across notebooks, scripts, and tuning runs. -->

Training with callbacks:

```python
callbacks = [
    EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True),
    ModelCheckpoint('models/best.h5', save_best_only=True),
    ReduceLROnPlateau(monitor='val_loss', factor=0.5, patience=3)
]
history = model.fit(X_train, y_train, validation_data=(X_val, y_val), epochs=100, batch_size=32, callbacks=callbacks)
```

<!-- Callbacks save compute, keep the best checkpoint, and reduce the chance of training far beyond the useful point. -->

---

## 9) Regularization & stabilization

- Dropout, L2 weight decay (`kernel_regularizer`), BatchNormalization
- EarlyStopping, ReduceLROnPlateau
- Gradient clipping if large spikes in gradients occur

<!-- These controls reduce overfitting and unstable training, which are common failure modes in neural networks. -->

---

## 10) Handling class imbalance

- Class weights in `model.fit(...)`
- Oversampling (SMOTE) only on training folds
- Focal loss for severe imbalance
- Use appropriate metrics (precision/recall/F1, PR-AUC)

<!-- Class imbalance can make accuracy misleading, so the training strategy must force the model to pay attention to minority classes. -->

---

## 11) Hyperparameter tuning

- Options:
  - `GridSearchCV` / `RandomizedSearchCV` with `scikeras.wrappers.KerasClassifier` for small grids
  - Keras Tuner (Hyperband, Bayesian) for larger search spaces â€” recommended for neural nets
- If using `scikeras` ensure parameter names match the wrapper's expectations (check `get_params()`)
- Prefer `Randomized` or Bayesian search when resources are limited

<!-- Tuning is where you systematically search for a better configuration instead of guessing layer sizes, learning rates, and dropout values. -->

---

## 12) Evaluation and visualization

- Plot training vs validation curves (loss & metrics)
- Classification: confusion matrix, ROC curve, precision-recall curve
- Regression: residual plots, actual vs predicted, RMSE/MAE
- Time-series: visualize predictions across time and errors by horizon

<!-- Evaluation plots show whether the model is learning the right signal, overfitting, or missing a specific range of values. -->

---

## 13) Save artifacts and build inference pipeline

- Save model: `model.save('models/model.h5')` or `tf.saved_model.save`
- Save preprocessors/scalers: `joblib.dump(preprocessor, 'models/preprocessor.pkl')`
- Save metrics & run metadata to a JSON or pickle

<!-- Saving the full artifact chain is required because inference must use the exact same preprocessing and model version as training. -->

Inference steps:
1. Load preprocessor
2. Preprocess new data (same feature order)
3. Load model
4. `model.predict()` â†’ inverse-transform outputs if scaled

Example inference:

```python
X_scaler = joblib.load('models/X_scaler.pkl')
y_scaler = joblib.load('models/y_scaler.pkl')
model = tf.keras.models.load_model('models/bike_rental_model.h5')
X = X_scaler.transform(last_7days)
X = X.reshape(1, 7, n_features)
pred = model.predict(X)
pred = y_scaler.inverse_transform(pred)
```

<!-- This example shows the production pattern: load preprocessing, shape the input correctly, predict, then undo target scaling. -->

---

## 14) Deployment considerations

- Use TF Serving / FastAPI / Streamlit / Docker depending on latency and throughput needs
- Export to TF Lite or ONNX for constrained environments
- Include model metadata and sample inputs with the deployment
- Monitor for drift and set up periodic re-training

<!-- Deployment choice depends on runtime constraints, operational ownership, and how the model will be consumed. -->

---

## 15) Troubleshooting & code review notes (project-specific suggestions)

A. From the ANN churn example:
- Make sure `OneHotEncoder` uses `sparse=False` when feeding into Keras unless you convert to dense.
- When using `scikeras.KerasClassifier` with `GridSearchCV`, parameter names sometimes need `model__paramname`; verify with `estimator.get_params()`.
- Save metrics to a file alongside models.

B. From BikeDemand RNN project:
- Create `models/` before trying to save with `joblib.dump` or `model.save`.
- Add callbacks (EarlyStopping and ModelCheckpoint) to `train.py` so you save the best model during training.
- Validate shapes and feature order in `predict_from_array` â€” the function is fine but consider strict validation for production use.

C. General:
- Avoid data leakage: fit scalers/encoders only on training data.
- Confirm feature order stability across training and inference.

<!-- These review notes capture mistakes that often look minor in code but cause broken predictions, bad metrics, or hard-to-debug deployment issues later. -->

---

## 16) Minimal runnable templates (practical snippets)

A. Preprocessing ColumnTransformer (dense output):

```python
preprocessor = ColumnTransformer(
    transformers=[
        ("num", StandardScaler(), numerical_features),
        ("cat", OneHotEncoder(drop="first", sparse=False), categorical_features)
    ],
    remainder="drop"
)
X_train_processed = preprocessor.fit_transform(X_train)
X_test_processed = preprocessor.transform(X_test)
```

<!-- This template gives a ready-to-use preprocessing pattern that can be copied into a working project. -->

B. Ensure models directory exists:

```python
from pathlib import Path
Path('models').mkdir(parents=True, exist_ok=True)
```

<!-- Creating the directory first prevents save-time errors when the output folder does not exist yet. -->

C. RNN training example with ModelCheckpoint:

```python
callbacks = [
    EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True),
    ModelCheckpoint('models/bike_rental_model.h5', save_best_only=True)
]
model.fit(X_train, y_train, epochs=50, batch_size=32, validation_data=(X_test, y_test), callbacks=callbacks)
```

<!-- This is the smallest useful training setup that still preserves the best model automatically. -->

---

## 17) Pre-deployment checklist

- [ ] Preprocessor & scalers saved and versioned
- [ ] Best model saved via `ModelCheckpoint`
- [ ] Test set kept entirely unseen until final evaluation
- [ ] Unit tests for prediction function (input schema & shapes)
- [ ] Basic monitoring/telemetry plan for production

<!-- This checklist is the final gate before shipping because missing one of these items often causes production failures. -->

---

## Appendix: Useful references
- TensorFlow docs: https://www.tensorflow.org/
- scikit-learn docs: https://scikit-learn.org/
- Keras Tuner: https://keras.io/keras_tuner/
- SHAP for explainability: https://github.com/slundberg/shap

<!-- These references are included for follow-up implementation details when the guide is not enough on its own. -->

---

## Acknowledgements
This rulebook was compiled by synthesizing project examples and standard deep learning practices to produce a single, actionable guide for building ANN and RNN models for classification, regression, and time-series forecasting.

<!-- The acknowledgement states the document's intent: unify practical patterns into one usable guide. -->
