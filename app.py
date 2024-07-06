from flask import Flask, render_template, request, jsonify, redirect, url_for
from joblib import load
import nltk
from nltk.corpus import stopwords
from string import punctuation

nltk.download("stopwords")
application = Flask(__name__)
sgd_ppl_clf = load('AI/model.joblib')

russian_stopwords = stopwords.words("russian")
dop_stopwords = ['это', 'которые', 'который', 'очень'] + [str(i) for i in range(10)]
table = {33: ' ', 34: ' ', 35: ' ', 36: ' ', 37: ' ', 38: ' ', 39: ' ', 40: ' ', 41: ' ', 42: ' ', 43: ' ', 44: ' ',
         45: ' ', 46: ' ', 47: ' ', 58: ' ', 59: ' ', 60: ' ', 61: ' ', 62: ' ', 63: ' ', 64: ' ', 91: ' ', 92: ' ',
         93: ' ', 94: ' ', 95: ' ', 96: ' ', 123: ' ', 124: ' ', 125: ' ', 126: ' ', 8211: ' ', 8212: ' '}


# Удаление знаков пунктуации из текста
def remove_punct(text):
    return text.translate(table)


def clean_text(text: str) -> str:
    text = remove_punct(text.lower())
    text = [token for token in text.split() if token not in russian_stopwords \
            and token != " " \
            and token not in dop_stopwords \
            and token.strip() not in punctuation]
    text = ' '.join(text)
    return text


@application.route('/')
@application.route('/index')
def index():
    return render_template("index.html")


@application.route('/get_word', methods=['POST'])
def get_word():
    text = request.form['text']
    text = clean_text(text)
    print("text:", text)
    ans = sgd_ppl_clf.predict([text])[0]
    print("ans: ", ans)
    # Обработка текста и получение слова
    return ans

if __name__ == '__main__':
    # Сохраняем модель
    application.run(host='0.0.0.0')
