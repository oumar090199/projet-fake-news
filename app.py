from flask import Flask, render_template, request
from TextCleaner import TextCleaner

# Chargez le modèle
import pickle

model = pickle.load(open('fake_news_detection.pkl', 'rb'))

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/detecter', methods=['POST'])
def verifier_article():
    if request.method == 'POST':
        # Obtenez les données entrées par l'utilisateur
        article_title = request.form['texte']

        # Utilisez le modèle pour prédire
        prediction = model.predict([article_title])

        # Renvoyez le résultat à l'utilisateur
        return render_template('resultat.html', prediction=prediction)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
