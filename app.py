from flask import Flask, render_template, request
import pickle
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "model.pkl")
vectorizer_path = os.path.join(BASE_DIR, "vectorizer.pkl")

model = pickle.load(open(model_path, "rb"))
vectorizer = pickle.load(open(vectorizer_path, "rb"))


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    text = request.form['news']
    vect = vectorizer.transform([text])
    pred = model.predict(vect)[0]
    label = "Real News" if pred == 1 else "Fake News"
    return render_template('index.html', prediction=label)

if __name__ == '__main__':
    app.run(debug=True)
