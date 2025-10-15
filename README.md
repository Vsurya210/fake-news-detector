The Fake News Detector project uses Machine Learning and Natural Language Processing (NLP) techniques to identify whether a given news article is real or fake. The system is built in Python and deployed through a simple Flask web application.

1. 🧠 Data Collection and Preprocessing

A labeled dataset containing news articles and their truth labels (Fake/Real) is used.

The text data is cleaned by removing punctuation, stop words, URLs, numbers, and special characters.

All text is converted to lowercase to ensure consistency.

Tokenization and vectorization (using TF-IDF Vectorizer or CountVectorizer) transform the raw text into numerical form so that it can be used by the ML model.

2. ⚙️ Model Training

Various machine learning models (such as Logistic Regression, Naive Bayes, or Passive Aggressive Classifier) can be trained to classify fake and real news.

The model learns patterns and relationships between word usage and news authenticity.

The trained model and text vectorizer are saved using pickle (model.pkl and vectorizer.pkl) for later use.

3. 💻 Flask Web Application

The Flask framework is used to build the user interface and backend logic.

When a user inputs a news headline or article text into the web form, the following happens:

The input text is sent to the Flask backend.

The text is transformed using the pre-trained vectorizer.

The trained model predicts whether the news is Fake or Real.

The result is displayed instantly on the web page.

4. 🌐 Frontend Design

The web interface is designed using HTML, CSS, and Bootstrap for a clean, responsive layout.

Users can simply enter a piece of news text and click the “Check” button to get results in real time.

5. 📊 Output

The app displays one of the following:

✅ Real News — if the model predicts the news is genuine.

❌ Fake News — if the model detects it as misleading or false.
