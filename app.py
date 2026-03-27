from flask import Flask, request, jsonify, render_template
import joblib

app = Flask(__name__)

model = joblib.load("model.pkl")

@app.route("/")    # Home route to render the UI
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])    # Route to handle prediction requests - using Postman testing or form submission (JSON data)
def predict():
    data = request.get_json()

    alcohol = data["alcohol"]
    malic_acid = data["malic_acid"]
    color_intensity = data["color_intensity"]
    
    input_data = [[alcohol, malic_acid, color_intensity]]
    prediction = model.predict(input_data)

    return jsonify({
        "prediction": int(prediction[0])
    })

if __name__ == "__main__":
    app.run(debug=True)