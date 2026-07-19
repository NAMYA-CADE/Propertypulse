from flask import Flask, render_template, request

from model import predict_price, investment_score


app = Flask(__name__)



@app.route("/")
def home():

    return render_template("home.html")




@app.route("/predict", methods=["GET", "POST"])
def predict():

    if request.method == "POST":

        city = request.form["city"]
        area = int(request.form["area"])
        bedrooms = int(request.form["bedrooms"])
        bathrooms = int(request.form["bathrooms"])
        age = int(request.form["age"])



        # Predict property price
        price = predict_price(
            city,
            area,
            bedrooms,
            bathrooms,
            age
        )


        formatted_price = "₹{:,.0f}".format(price)



        # Investment score
        stars, reasons = investment_score(
            area,
            age,
            bedrooms
        )



        return render_template(
            "result.html",
            price=formatted_price,
            stars=stars,
            reasons=reasons
        )



    return render_template("prediction.html")





if __name__ == "__main__":

    app.run(debug=True)