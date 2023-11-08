from flask import Flask, render_template, jsonify
import sqlite3 as sq

app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/')
def index():
    # list = ['Мы крутой портал', [
    #     'lorem iopsum dolor sit amet lorem iopsum dolor sit amet lorem iopsum dolor sit amet lorem iopsum dolor sit amet']]
    list =['Добро пожаловать', "Здесь мы исследуем удивительные возможности Arduino и предлагаем вам множество примеров проектов, которые вы можете создать самостоятельно. Наш блог предлагает три уровня сложности, чтобы соответствовать вашим навыкам и интересам."]
    return render_template('index.html', title='Главная', index_content=list)


@app.route('/course-<num>/lesson-<num2>/')
def lesson(num, num2):
    with sq.connect("6743database.db") as con:
        cur = con.cursor()
        db_array = cur.execute(f"SELECT course_num, lesson_num, video_link, text, picture, code FROM lesson_content WHERE course_num={num} AND lesson_num={num2}").fetchall()
        last_lesson = cur.execute(f'SELECT count(distinct(lesson_num)) from bdtable WHERE course_num={num}').fetchall()
        db_array = list(db_array)

        for t in db_array:
            print(t)

        last_lesson = int(last_lesson[0][0])
        print(last_lesson)
        if last_lesson == int(num2):
            last_lesson = 1
        else:
            last_lesson = 0

        print(last_lesson)
    return render_template('index.html', title='Главная', lesson_page=db_array, content_title=f'Курс {num}, урок {num2}', last_lesson=last_lesson)


@app.route('/course-<num>/')
def course(num):
    with sq.connect("6743database.db") as con:
        cur = con.cursor()
        db_array = cur.execute(
            f"SELECT course_num, lesson_num, title, reading_time, preview_text FROM bdtable WHERE course_num={num}").fetchall()

    return render_template('index.html', title=f'Курс {num}', list=db_array, content_title=f'Курс {num}')


@app.route('/gallery/')
def gallery():
    with sq.connect("6743database.db") as con:
        cur = con.cursor()
        db_array = cur.execute(
            "SELECT picture FROM lesson_content WHERE lesson_num='' ").fetchall()
        print(db_array[0])
    return render_template('index.html', gallery_arr=db_array)



##################### НЕ ТРОГАТЬ #####################
if __name__ == "__main__":
    # app.run( host='192.168.0.105',debug=True, port=5000)
    app.run(debug=True)
#######################################################
