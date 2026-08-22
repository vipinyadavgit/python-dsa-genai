# Deep Learning Rule Book — End-to-End Guide

Version: draft  
Purpose: Practical, runnable guide to build, evaluate, tune, save and deploy deep learning models for classification, regression and time‑series (RNN) problems. This document synthesizes general best practices and concrete patterns extracted from three example projects: an ANN churn classifier, a simple perceptron tutorial, and a Bike‑Demand RNN forecasting project.

---

## Quick summary — what this document contains
- An end-to-end checklist and practical instructions for building deep learning models.
- Target audiences: data scientists building Keras/TensorFlow models for tabular classification/regression and time-series forecasting.
- Includes runnable code patterns, common pitfalls, and a pre‑deployment checklist.

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

---

## 2) Problem definition & metrics

- Decide problem type and primary metric before modeling:
  - Binary classification (churn): ROC-AUC, precision, recall, F1
  - Multi-class classification: accuracy, per-class precision/recall, macro/micro F1
  - Regression (demand forecasting): RMSE, MAE, MAPE, R2
  - Time-series forecasting: rolling validation; horizon-specific RMSE/MAPE
- Note operational constraints: latency, model size, inference environment.

---

## 3) Data ingestion & validation

- Store raw data in `data/` and never overwrite it.
- Validate presence of required columns early and raise helpful errors.
- For time-series, parse datetime and sort by date.

Example guard:

```python
from pathlib import Path
DATA_PATH = Path("data/bike.csv")
if not DATA_PATH.exists():
    raise FileNotFoundError(f"{DATA_PATH} missing")
```

---

## 4) Exploratory Data Analysis (EDA)

- High-level checks: `df.shape`, `df.info()`, `df.describe()`, `df.head()`
- Missing values: `df.isnull().sum()`
- Duplicates: `df.duplicated().sum()` → drop if needed
- Univariate & bivariate visualizations: histograms, boxplots, correlations, pairplots
- Outliers: IQR method or domain-driven decisions
- Time-series: trend/seasonality plots, ACF/PACF

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

Important: `OneHotEncoder` default returns sparse matrices — convert to dense (`sparse=False`) before feeding into Keras.

---

## 6) Splitting data (train / val / test)

- Tabular problems: stratified split for classification (`train_test_split(..., stratify=y)`)
- Typical: 70–80% train, 20–30% test. Use validation split or a separate validation set.
- Time-series: do not random split.
- Use chronological split and prefer walk-forward (rolling-origin) validation for robust estimates.

---

## 7) Model choices & architecture patterns

A. Dense feedforward models (tabular)
- Input: preprocessed feature vector
- Hidden layers: start small (e.g., 64 → 32), add `BatchNormalization()` and `Dropout()` if needed
- Output/activation/loss:
  - Binary: `Dense(1, activation='sigmoid')` + `binary_crossentropy`
  - Multi-class: `Dense(n_classes, activation='softmax')` + `categorical_crossentropy`
  - Regression: `Dense(1, activation='linear')` + `MSE` or `MAE`

B. RNNs / LSTMs / GRUs (time-series)
- For short sequential patterns `SimpleRNN` might suffice; for long-range dependencies prefer `LSTM` or `GRU`.
- Stacked RNNs: set `return_sequences=True` on all but the last recurrent layer.
- Scale inputs and targets; create sliding windows for sequences (e.g., last 7 days → predict next day).

C. Embeddings for categorical features
- Map categories to integer IDs and use `Embedding` layers in Keras for high-cardinality categorical variables.

---

## 8) Keras model factory & training template

- Use a builder function for reproducibility and for hyperparameter tuning.

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

Training with callbacks:

```python
callbacks = [
    EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True),
    ModelCheckpoint('models/best.h5', save_best_only=True),
    ReduceLROnPlateau(monitor='val_loss', factor=0.5, patience=3)
]
history = model.fit(X_train, y_train, validation_data=(X_val, y_val), epochs=100, batch_size=32, callbacks=callbacks)
```

---

## 9) Regularization & stabilization

- Dropout, L2 weight decay (`kernel_regularizer`), BatchNormalization
- EarlyStopping, ReduceLROnPlateau
- Gradient clipping if large spikes in gradients occur

---

## 10) Handling class imbalance

- Class weights in `model.fit(...)`
- Oversampling (SMOTE) only on training folds
- Focal loss for severe imbalance
- Use appropriate metrics (precision/recall/F1, PR-AUC)

---

## 11) Hyperparameter tuning

- Options:
  - `GridSearchCV` / `RandomizedSearchCV` with `scikeras.wrappers.KerasClassifier` for small grids
  - Keras Tuner (Hyperband, Bayesian) for larger search spaces — recommended for neural nets
- If using `scikeras` ensure parameter names match the wrapper's expectations (check `get_params()`)
- Prefer `Randomized` or Bayesian search when resources are limited

---

## 12) Evaluation and visualization

- Plot training vs validation curves (loss & metrics)
- Classification: confusion matrix, ROC curve, precision-recall curve
- Regression: residual plots, actual vs predicted, RMSE/MAE
- Time-series: visualize predictions across time and errors by horizon

---

## 13) Save artifacts and build inference pipeline

- Save model: `model.save('models/model.h5')` or `tf.saved_model.save`
- Save preprocessors/scalers: `joblib.dump(preprocessor, 'models/preprocessor.pkl')`
- Save metrics & run metadata to a JSON or pickle

Inference steps:
1. Load preprocessor
2. Preprocess new data (same feature order)
3. Load model
4. `model.predict()` → inverse-transform outputs if scaled

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

---

## 14) Deployment considerations

- Use TF Serving / FastAPI / Streamlit / Docker depending on latency and throughput needs
- Export to TF Lite or ONNX for constrained environments
- Include model metadata and sample inputs with the deployment
- Monitor for drift and set up periodic re-training

---

## 15) Troubleshooting & code review notes (project-specific suggestions)

A. From the ANN churn example:
- Make sure `OneHotEncoder` uses `sparse=False` when feeding into Keras unless you convert to dense.
- When using `scikeras.KerasClassifier` with `GridSearchCV`, parameter names sometimes need `model__paramname`; verify with `estimator.get_params()`.
- Save metrics to a file alongside models.

B. From BikeDemand RNN project:
- Create `models/` before trying to save with `joblib.dump` or `model.save`.
- Add callbacks (EarlyStopping and ModelCheckpoint) to `train.py` so you save the best model during training.
- Validate shapes and feature order in `predict_from_array` — the function is fine but consider strict validation for production use.

C. General:
- Avoid data leakage: fit scalers/encoders only on training data.
- Confirm feature order stability across training and inference.

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

B. Ensure models directory exists:

```python
from pathlib import Path
Path('models').mkdir(parents=True, exist_ok=True)
```

C. RNN training example with ModelCheckpoint:

```python
callbacks = [
    EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True),
    ModelCheckpoint('models/bike_rental_model.h5', save_best_only=True)
]
model.fit(X_train, y_train, epochs=50, batch_size=32, validation_data=(X_test, y_test), callbacks=callbacks)
```

---

## 17) Pre-deployment checklist

- [ ] Preprocessor & scalers saved and versioned
- [ ] Best model saved via `ModelCheckpoint`
- [ ] Test set kept entirely unseen until final evaluation
- [ ] Unit tests for prediction function (input schema & shapes)
- [ ] Basic monitoring/telemetry plan for production

---

## Appendix: Useful references
- TensorFlow docs: https://www.tensorflow.org/
- scikit-learn docs: https://scikit-learn.org/
- Keras Tuner: https://keras.io/keras_tuner/
- SHAP for explainability: https://github.com/slundberg/shap

---

## Acknowledgements
This rulebook was compiled by synthesizing project examples and standard deep learning practices to produce a single, actionable guide for building ANN and RNN models for classification, regression, and time-series forecasting.
