from flask import Flask, render_template, request, redirect, url_for
import csv
import urllib.parse

app = Flask(__name__)

# Route: homepage
@app.route("/")
def home():
    return render_template("index.html")

# Route: form (supports GET to display and POST to receive)
@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        # Get form values
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        number = request.form.get("number", "").strip()

        # Optional: validate numeric field (basic)
        try:
            number_val = float(number)
        except ValueError:
            number_val = number  # keep raw if not numeric

        # After POST, redirect to GET with query params so GET displays the data
        params = {
            "name": name,
            "email": email,
            "number": number
        }
        query = urllib.parse.urlencode(params)
        return redirect(url_for("form") + "?" + query)

    # GET: show the form and any submitted data passed via query params
    submitted = {
        "name": request.args.get("name"),
        "email": request.args.get("email"),
        "number": request.args.get("number")
    }
    # If there is at least one non-empty param, consider it a submission to display
    has_submission = any(submitted.values())
    return render_template("form.html", submitted=submitted, has_submission=has_submission)

# Route: data — reads CSV and displays it
@app.route("/data")
def data_page():
    products = []
    try:
        with open("data.csv", newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                products.append(row)
    except FileNotFoundError:
        products = []
    return render_template("data.html", products=products)

if __name__ == "__main__":
    app.run(debug=True)
