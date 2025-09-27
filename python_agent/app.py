from flask import Flask, request, jsonify
import pandas as pd
import joblib
from datetime import datetime

app = Flask(__name__)

# Load the pre-trained model pipeline
try:
    model = joblib.load('churn_model.joblib')
    print("Model loaded successfully.")
except FileNotFoundError:
    print("Error: Model file 'churn_model.joblib' not found.")
    print("Please run 'train_model.py' first to create the model file.")
    model = None

@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return jsonify({'error': 'Model not loaded'}), 500

    # Get JSON data from the request
    data = request.get_json()
    print(f"Received data for prediction: {data}")

    # --- Feature Engineering ---
    # The input data needs to have the same features as the training data.
    # We create a pandas DataFrame from the incoming JSON.
    df = pd.DataFrame([data])

    # Calculate 'days_since_last_login'
    today = datetime.strptime('2025-09-26', '%Y-%m-%d')
    df['LastLoginDate'] = pd.to_datetime(df['LastLoginDate'])
    df['days_since_last_login'] = (today - df['LastLoginDate']).dt.days

    # Ensure all required columns are present for the model
    required_features = ['PlanLevel', 'MonthlySpend', 'TicketCategory', 'days_since_last_login']
    df = df[required_features]

    # --- Prediction ---
    # Use the model to predict the probability of churn
    # model.predict_proba returns probabilities for [class 0, class 1]
    # We want the probability of class 1 (Churned)
    churn_probability = model.predict_proba(df)[0][1]
    print(f"Predicted churn probability: {churn_probability}")

    # --- Response ---
    # Return the prediction as a JSON response
    return jsonify({
        'customer_id': data.get('CustomerID'),
        'churn_probability': churn_probability
    })

if __name__ == '__main__':
    # Run the Flask app on port 5001
    app.run(port=5001, debug=True)