# 🏗️ LCCAI — Life Cycle Cost AI

A simple machine learning system that predicts long-term building costs from day-one data.

LCCAI estimates:

* annual maintenance cost
* annual energy cost

using basic building parameters.

No complex simulations.
Just data → prediction.

---

## 💡 what it does

Given initial building inputs like:

* area
* age
* material quality
* construction cost
* climate severity

LCCAI predicts:

* 🧾 **Annual Maintenance Cost**
* ⚡ **Annual Energy Cost**

---

## 🧠 idea

Most cost decisions are made early.

But actual expenses show up later.

This project tries to answer:

> *“How expensive will this building be to run?”*

before it's even used.

---

## ⚙️ how it works

1. Load dataset (`dummy_building_data.csv`)
2. Split into:

   * inputs (features)
   * outputs (targets)
3. Train two models:

   * maintenance model
   * energy model
4. Evaluate performance (MAE + R²)
5. Export models as `.pkl`

---

## 🧪 features

* dual-model system (separate predictions)
* simple, interpretable features
* Random Forest regression
* evaluation metrics included
* model export (ready for integration)

---

## 🛠 tech stack

* Python
* pandas / numpy
* scikit-learn

---

## 🚀 usage

### 1. install dependencies

```bash
pip install pandas numpy scikit-learn
```

### 2. add dataset

Place:

```
dummy_building_data.csv
```

in the project root.

### 3. run training

```bash
python main.py
```

### 4. output

* model_maintenance.pkl
* model_energy.pkl

---

## 📊 metrics

The script prints:

* Mean Absolute Error (₹)
* R² Score (accuracy)

Example:

```
Maintenance MAE: ₹12,000
Energy MAE: ₹8,500
R²: 0.85+
```

---

## ⚠️ limitations

* uses dummy dataset
* no real-world validation yet
* no UI / API
* model accuracy depends on data quality

---

## 🧭 roadmap

* real dataset integration
* API / web interface
* better feature engineering
* try advanced models (XGBoost, etc.)

---

## 🤔 why this exists

Because long-term costs are usually:

* underestimated
* ignored
* or discovered too late

This project is a small step toward predicting them earlier.

---

## 📌 status

🚧 early-stage / experimental

---

