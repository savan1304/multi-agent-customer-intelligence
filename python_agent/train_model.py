import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import joblib
from datetime import datetime

print("Starting model training process...")

# --- 1. Load and Prepare Data ---
# Load the dataset
df = pd.read_csv('../data/customer_data.csv')

# Feature Engineering: Calculate 'days_since_last_login'
# We use a fixed 'today' for reproducibility
today = datetime.strptime('2025-09-26', '%Y-%m-%d')
df['LastLoginDate'] = pd.to_datetime(df['LastLoginDate'])
df['days_since_last_login'] = (today - df['LastLoginDate']).dt.days

# Define features (X) and target (y)
# We will use these features to predict 'Churned'
features = ['PlanLevel', 'MonthlySpend', 'TicketCategory', 'days_since_last_login']
target = 'Churned'

X = df[features]
y = df[target]

# --- 2. Define Preprocessing and Model Pipeline ---
# Define categorical features for one-hot encoding
categorical_features = ['PlanLevel', 'TicketCategory']
numerical_features = ['MonthlySpend', 'days_since_last_login']

# Create a preprocessor to handle categorical data
preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
    ],
    remainder='passthrough' # Keep numerical features as they are
)

# Create the model pipeline
# This pipeline will first preprocess the data, then train the model
model_pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', LogisticRegression(random_state=42, class_weight='balanced'))
])

# --- 3. Train the Model ---
# Split data for training and testing (though we train on all data for the final model)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Training the model...")
model_pipeline.fit(X_train, y_train)
print(f"Model accuracy on test set: {model_pipeline.score(X_test, y_test):.2f}")


# --- 4. Save the Model ---
# Save the trained pipeline to a file so our API can use it
model_filename = 'churn_model.joblib'
joblib.dump(model_pipeline, model_filename)

print(f"Model training complete. Model saved as '{model_filename}'.")