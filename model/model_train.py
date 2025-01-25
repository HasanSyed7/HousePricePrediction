import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import joblib
from sklearn.preprocessing import LabelEncoder

# Load dataset
data = pd.read_csv("housing.csv")  # Replace with your dataset

data['mainroad'] = LabelEncoder().fit_transform(data['mainroad'])

# Preprocessing
X = data[["bedrooms", "bathrooms", "area", "mainroad"]]  # Example columns
y = data["price"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Save the trained model
joblib.dump(model, "model/house_price_model.pkl")
