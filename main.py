from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from data import db_session
from data.jobs import Jobs
from data.users import User

app = Flask(__name__)
app.config["SECRET_KEY"] = "marcomaregasecretkey"

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
        "Готовы остаться на Марсе?": False,
    }
    return render_template("auto_answer.html", title="Анкета", answer=answer)


class LoginForm(FlaskForm):
    astronaut_id = StringField("id астронавта", validators=[DataRequired()])
    astronaut_password = PasswordField("Пароль астронавта", validators=[DataRequired()])
    captain_id = StringField("id капитана", validators=[DataRequired()])
    captain_password = PasswordField("Пароль капитана", validators=[DataRequired()])
    submit = SubmitField("Войти")


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect("/")
    return render_template("login.html", title="Аварийный доступ", form=form)


@app.route("/works_log")
def works_log():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs)
    return render_template("works_log.html", title="Works log", jobs=jobs)


if __name__ == "__main__":
    db_session.global_init("db/mars.db")
    app.run(host="127.0.0.1", port=8080)
