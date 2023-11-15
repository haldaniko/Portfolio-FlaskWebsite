from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/portfolio/<project_number>")
def home2(project_number):
    return render_template(f"portfolio/{project_number}.html")


if __name__ == "__main__":
    app.run(debug=True)
