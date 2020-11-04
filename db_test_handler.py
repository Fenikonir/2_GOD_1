import sqlite3
import random


# Добавление, Проверка и Авторизация
def get_tests():
    con = sqlite3.connect("handler/tests.db")
    cur = con.cursor()
    result = cur.execute("""SELECT * FROM tests ORDER BY NAME""").fetchall()
    cur.close()
    con.close()
    return result


def get_questions(tests):
    con = sqlite3.connect("handler/tests.db")
    cur = con.cursor()
    result = cur.execute("""SELECT * FROM questions WHERE test=(
    SELECT id FROM tests
        WHERE name =?)""", (tests,)).fetchall()
    cur.close()
    con.close()
    return result


def get_answers(quest):
    con = sqlite3.connect("handler/tests.db")
    cur = con.cursor()
    result = cur.execute("""SELECT * FROM answer WHERE question=(
    SELECT id FROM questions
        WHERE question =?)""", (quest,)).fetchall()
    cur.close()
    con.close()
    return result


def get_guests_and_answers(quest):
    con = sqlite3.connect("handler/tests.db")
    cur = con.cursor()
    result = cur.execute("""SELECT q.question, a.answer, a.type FROM tests t 
    left join questions q on q.test = t.id 
    left join answer a on a.question = q.id 
    WHERE t.name = ? 
        order by q.question, a.answer""", (quest,)).fetchall()

    questionGroup = ""
    questionsList = []
    answersList = []
    for r in result:
        if (questionGroup != r[0]):
            if questionGroup != "":
                random.shuffle(answersList)
                questionsList.append(Question(questionGroup, answersList))
                answersList = []
            questionGroup = r[0]
        answersList.append(Answer(r[1], r[2], False))

    if (questionGroup != ""):
        questionsList.append(Question(questionGroup, answersList))

    cur.close()
    con.close()
    return questionsList


class Answer:
    def __init__(self, answer, type, checked):
        self.answer = answer
        self.type = type
        self.checked = checked


class Question:
    def __init__(self, question, answers):
        self.question = question
        self.answers = answers


question = get_guests_and_answers('Финансовая культура')
for q in question:
    print("==========================================")
    print(q.question, len(q.answers))
    for a in q.answers:
        print(a.answer, a.type, a.checked)

