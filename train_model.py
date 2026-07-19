import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder

import joblib


# Load dataset

data = pd.read_csv("dataset/houses.csv")


# Convert city text into numbers

encoder = LabelEncoder()

data["city"] = encoder.fit_transform(data["city"])



# Separate input and output

X = data.drop("price", axis=1)

y = data["price"]



# Split data

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)



# Create model

model = LinearRegression()


# Train model

model.fit(X_train, y_train)



# Save model

joblib.dump(model, "models/price_model.pkl")


joblib.dump(
    encoder,
    "models/city_encoder.pkl"
)


print("Model trained successfully!")