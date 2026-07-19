import joblib
import pandas as pd


# Load trained model
model = joblib.load("models/price_model.pkl")

# Load city encoder
encoder = joblib.load("models/city_encoder.pkl")


# Show available cities in terminal
print("Available cities:", encoder.classes_)



def predict_price(city, area, bedrooms, bathrooms, age):

    # Convert city into lowercase
    city = city.lower()


    # Encode city
    if city in encoder.classes_:
        city_encoded = encoder.transform([city])[0]
    else:
        # If city is not present in dataset
        city_encoded = 0


    # Create input dataframe
    input_data = pd.DataFrame(
        [[
            city_encoded,
            area,
            bedrooms,
            bathrooms,
            age
        ]],
        columns=[
            "city",
            "area",
            "bedrooms",
            "bathrooms",
            "age"
        ]
    )


    # Predict price
    price = model.predict(input_data)[0]


    return round(price)




def investment_score(area, age, bedrooms):

    score = 0
    reasons = []


    # Area check
    if area >= 1500:
        score += 2
        reasons.append("Large property area")
    else:
        score += 1
        reasons.append("Average property area")



    # Age check
    if age <= 5:
        score += 2
        reasons.append("Newly constructed property")

    elif age <= 10:
        score += 1
        reasons.append("Moderately old property")

    else:
        reasons.append("Older property")



    # Bedroom check
    if bedrooms >= 3:
        score += 2
        reasons.append("Suitable for family living")

    else:
        score += 1
        reasons.append("Compact living space")



    # Rating calculation
    if score >= 6:
        stars = "★★★★★"

    elif score >= 4:
        stars = "★★★★☆"

    elif score >= 2:
        stars = "★★★☆☆"

    else:
        stars = "★★☆☆☆"



    return stars, reasons