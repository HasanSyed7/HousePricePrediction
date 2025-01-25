from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model
model = joblib.load("model/house_price_model.pkl")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        # Get form inputs
        bedrooms = int(request.form["bedrooms"])
        bathrooms = int(request.form["bathrooms"])
        sqft = float(request.form["sqft"])
        location = request.form["mainroad"]

        if location=='Yes':
            location_code=1
        else:
            location_code=0

        # Prepare input for the model
        features = np.array([[bedrooms, bathrooms, sqft, location_code]])

        # Predict
        prediction = model.predict(features)[0]
        return render_template("result.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
