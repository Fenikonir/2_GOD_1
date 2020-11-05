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


def get_guests_and_answers(quest):
    con = sqlite3.connect("handler/tests.db")
    cur = con.cursor()
    result = cur.execute("""SELECT t.id, q.id, q.question, a.answer, a.correct FROM tests t 
    left join questions q on q.test = t.id 
    left join answers a on a.question = q.id 
    WHERE t.name = ? 
        order by q.question, a.answer""", (quest,)).fetchall()

    testId = result[0][0]
    questionId = 0
    questionGroup = ""
    questionsList = []
    answersList = []
    count_correct_answers = 0
    for r in result:
        if (questionGroup != r[2]):
            if questionGroup != "":
                random.shuffle(answersList)
                questionsList.append(Question(testId, questionId, questionGroup, count_correct_answers, answersList))
                answersList = []
                count_correct_answers = 0
            questionId = r[1]
            questionGroup = r[2]
        answersList.append(Answer(r[3], r[4], False))
        if r[4] == "True":
            count_correct_answers += 1

    if (questionGroup != ""):
        questionsList.append(Question(testId, questionId, questionGroup, count_correct_answers, answersList))

    cur.close()
    con.close()
    return questionsList


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
    def __init__(self, test, questionId, question, count_correct_answers, answers):
        self.test = test
        self.questionId = questionId
        self.question = question
        self.count_correct_answers = count_correct_answers
        self.answers = answers


# quest_and_answer = get_guests_and_answers("Финансовая культура")
# for q in quest_and_answer:
#     print("==============================================")
#     print(q.question, q.questionId, len(q.answers))
#     for a in q.answers:
#         print(a.answer, a.correct, a.checked)
