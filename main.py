from flask import Flask, render_template

app = Flask(__name__)
specialities = [
    "инженер-исследователь",
    "пилот",
    "строитель",
    "экзобиолог",
    "врач",
    "инженер по терраформированию",
    "климатолог",
    "специалист по радиационной защите",
    "астрогеолог",
    "гляциолог",
    "инженер жизнеобеспечения",
    "метеоролог",
    "оператор марсохода",
    "киберинженер",
    "штурман",
    "пилот дронов",
]


@app.route("/")
@app.route("/index")
def index():
    return render_template("base.html", title="Шаблон",)


@app.route("/training/<speciality>")
def training(speciality):
    return render_template("training.html", title="Схема", speciality=speciality)


@app.route("/list_prof/<tag>")
def list_prof(tag):
    return render_template("list_prof.html", title="Список профессий", tag=tag, specialities=specialities)


@app.route("/answer")
@app.route("/auto_answer")
def auto_answer():
    answer = {
        "Имя": "Marco",
        "Фамилия": "Marega",
        "Образование": "Начальное",
        "Профессия": "Программист",
        "Пол": "male",
        "Мотивация": "фвылорфлоафылврафафоырва",
        "Готовы остаться на Марсе?": False
    }
    return render_template("auto_answer.html", title="Анкета", answer=answer)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)
