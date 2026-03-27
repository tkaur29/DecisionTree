# Wine Class Predictor (Decision Tree) 🍷

<img width="700" height="430" alt="image" src="https://github.com/user-attachments/assets/62aaf4e5-3129-4c00-96b5-95c618d317c2" />

This project is a small end-to-end machine learning web app that predicts a wine class using a trained Decision Tree model.

## Features ✨

- Trains a multiclass Decision Tree classifier on Wine dataset from scikit-learn. (`train_model.ipynb`)
- Uses three input features for prediction:
	- `alcohol`
	- `malic_acid`
	- `color_intensity`
- Saves the trained model as `model.pkl` with `joblib`.
- A Flask backend (`app.py`) that loads the trained model and exposes a prediction API `POST /predict`.
- Includes an interactive frontend that calls the API and displays predicted class (`Class 0`, `Class 1`, or `Class 2`).

## Tech Stack 👩🏻‍💻

- Python
- Flask
- scikit-learn
- pandas
- joblib
- HTML, CSS, JavaScript

## How It Works

1. `train_model.ipynb` loads the Wine dataset and selects three features.
2. The notebook splits data into train/test sets.
3. A `DecisionTreeClassifier` is trained and evaluated.
4. The trained model is exported to `model.pkl`.
5. `app.py` loads `model.pkl` on startup.
6. The UI sends feature values to `POST /predict`, and the backend returns the predicted class.

## Setup instructions ⚙️
### Train the Model

If `model.pkl` is missing or you want to retrain:

1. Open `train_model.ipynb`.
2. Run all cells from top to bottom.
3. Confirm the notebook prints: `Model saved as model.pkl`.

### Run the Flask App

From the project root:

```powershell
python app.py
```

Then open your browser at:

`http://127.0.0.1:5000/`



> Pro tip (optional) : Use ngrok tunneling to get instant public link for your localhost

