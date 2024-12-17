# app.py
from flask import Flask, render_template, request # type: ignore

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def mai():
    result = ""
    if request.method == "POST":
        try:
            # Get the expression from the form
            expression = request.form["expression"]
            # Evaluate the expression
            result = eval(expression)
        except Exception as e:
            result = "Error"
    return render_template("mai.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)