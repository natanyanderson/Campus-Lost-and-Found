from flask import Flask,  render_template,request, redirect

app = Flask(__name__)

water_bottle = {"name": "water bottle", "description": "pink 32oz owala with flower sticker",
                "date_found": "10/18/26", "location": "classroom 42B", "claimed": False}
found_items = []
found_items.append(water_bottle)
found_items.append({"name": "calculator", "description": "texas instrument ti-84 plus ce",
                "date_found": "10/13/26", "location": "classroom 307", "claimed": False})
found_items.append({"name": "id card", "description": "school id card with name stephanie lee",
                "date_found": "10/09/26", "location": "3rd floor women's bathroom", "claimed": False})

@app.route("/")
def home():
    return "Welcome to the Campus Lost & Found!"

@app.route("/items")
def items():
    return render_template("items.html", found_items=found_items)

@app.route("/report", methods=["GET", "POST"])
def report():
    if request.method == "POST":
        new_item = {
            "name": request.form["name"],
            "description": request.form["description"],
            "location": request.form["location"],
            "date_found": request.form["date_found"],
            "claimed": False
        }
        found_items.append(new_item)
        return redirect("/items")
    return render_template("report.html")


if __name__ == "__main__":
    app.run(debug=True)