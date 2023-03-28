from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    return render_template("base.html", title="Шаблон")


@app.route("/training/<speciality>")
def training(speciality):
    return render_template("training.html", title="Схема", speciality=speciality)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)
