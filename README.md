
# House Price Prediction Web Application

This is a Flask web application that predicts house prices based on input features such as the number of bedrooms, bathrooms, area (in square feet), and the location that whether the house is located on a main road. The application uses a simple machine learning model to make predictions based on user input.

## Features
- **Input**: Users can input details such as the number of bedrooms, bathrooms, area, and location of the house(whether the house is located on a main road or not).
- **Prediction**: The model predicts the house price based on the provided features.
- **Web Interface**: The app provides a  user-friendly interface for users to input data and receive predictions.


## Steps followed to build this project:
1.)Collected Housing datast from kaggle.
2.)Some preprocessing and dimension reduction of the dataset, which included only relevant features.
3.)Built the model using simple Linear Regression and saved it under model as .pkl 
4.)Setup the flask application to process on the user inputs from frontend. Also Load
5.)Prepare the input as np array to send it as input to the trained model
6.)Make the predction and return it as output to the user.



## Project Setup

Follow these steps to set up and run the application locally:

### 1. Clone the Repository
Clone the repository to your local machine:
git clone https://github.com//house-price-predictor.git
cd house-price-predictor


### 2. Create and Activate a Virtual Environment
Create and Activate a Virtual Environment
1. python -m venv venv
2. venv\Scripts\activate

### 3. Install Required Dependencies
Once the virtual environment is activated, install the required Python libraries
1. pip install -r requirements.txt


### 4. Running the Flask App
To run the Flask web application, use the following command:
1. python app.py

By default, the application will be accessible at http://127.0.0.1:5000/.

Click on the link to run it on your local machine.
