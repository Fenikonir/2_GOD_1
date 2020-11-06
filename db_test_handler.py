import sqlite3
import random
import loging

# Добавление, Проверка и Авторизация
uncorrect = []


def get_tests():
    con = sqlite3.connect("handler/tests.db")
    cur = con.cursor()
    result = cur.execute("""SELECT * FROM tests ORDER BY NAME""").fetchall()
    cur.close()
    con.close()
    return result


def get_guests_and_answers(test):
    con = sqlite3.connect("handler/tests.db")
    cur = con.cursor()
    result = cur.execute("""SELECT t.id, q.id, q.question, a.answer, a.correct FROM tests t 
    left join questions q on q.test = t.id 
    left join answers a on a.question = q.id 
    WHERE t.name = ? 
        order by q.question, a.answer""", (test,)).fetchall()

    test_id = result[0][0]
    question_id = 0
    question_group = ""
    questionsList = []
    answersList = []
    count_correct_answers = 0
    for r in result:
        if (question_group != r[2]):
            if question_group != "":
                random.shuffle(answersList)
                questionsList.append(Question(test_id, question_id, question_group, count_correct_answers, answersList))
                answersList = []
                count_correct_answers = 0
            question_id = r[1]
            question_group = r[2]
        answersList.append(Answer(r[3], r[4], False))
        if r[4] == "True":
            count_correct_answers += 1

    if (question_group != ""):
        questionsList.append(Question(test_id, question_id, question_group, count_correct_answers, answersList))

    cur.close()
    con.close()
    return questionsList


def write_quest(test, check_test, question, answers):
    con = sqlite3.connect("handler/tests.db")
    cur = con.cursor()
    if not check_test:
        cur.execute("""INSERT INTO Tests(name) VALUES(?)""", (test,))
    test_id = cur.execute("""SELECT id FROM tests WHERE name=?""", (test,)).fetchall()[0][0]
    cur.execute("""INSERT INTO questions(test, question) VALUES(?, ?)""", (test_id, question))
    question_id = cur.execute("""SELECT id FROM questions WHERE question=?""", (question,)).fetchall()[0][0]
    for i in range(len(answers)):
        cur.execute("""INSERT INTO answers(question, answer, correct) VALUES(?, ?, ?)""",
                    (question_id, answers[i][0], answers[i][1]))
    cur.close()
    con.commit()


def update_quest(test, check_test, question, answers):
    con = sqlite3.connect("handler/tests.db")
    cur = con.cursor()
    question_id = cur.execute("""SELECT id FROM questions WHERE question=?""", (question,)).fetchall()[0][0]
    cur.execute("""DELETE from answers WHERE question=?""", (question_id,))
    for i in range(len(answers)):
        cur.execute("""INSERT INTO answers(question, answer, correct) VALUES(?, ?, ?)""",
                    (question_id, answers[i][0], answers[i][1]))
    cur.close()
    con.commit()


def write_result(test, user, date_time, all_quests, correct_quests):
    con = sqlite3.connect("handler/tests.db")
    cur = con.cursor()
    cur.execute("""INSERT INTO results(test, user, data_time, all_quests, correct_quests) VALUES(?, ?, ?, ?, ?)""",
                (test, user, date_time, all_quests, correct_quests))
    result = cur.execute("""SELECT id FROM results WHERE test=? and user=? and data_time=?""",
                         (test, user, date_time,)).fetchall()
    id = result[0][0]
    for q in uncorrect:
        cur.execute("""INSERT INTO uncorrect_quests(result, quest) VALUES(?, ?)""", (id, q,))
    cur.close()
    con.commit()


class Answer:
    def __init__(self, answer, correct, checked):
        self.answer = answer
        self.correct = correct
        self.checked = checked


class Question:
    def __init__(self, test, question_id, question, count_correct_answers, answers):
        self.test = test
        self.question_id = question_id
        self.question = question
        self.count_correct_answers = count_correct_answers
        self.answers = answers

    # quest_and_answer = get_guests_and_answers("Финансовая культура")
    # for q in quest_and_answer:
    #     print("==============================================")
    #     print(q.question, q.questionId, len(q.answers))
    #     for a in q.answers:
    #         print(a.answer, a.correct, a.checked)
