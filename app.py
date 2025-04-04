from flask import Flask, request, render_template
import pickle
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

nltk.download('punkt')
nltk.download('stopwords')

# Load model and vectorizer
model = pickle.load(open('model.pkl', 'rb'))
tfidf = pickle.load(open('vectorizer.pkl', 'rb'))

# Text preprocessing
ps = PorterStemmer()
def transform_messages(messages):
    messages = messages.lower()
    messages = nltk.word_tokenize(messages)
    y = []
    for i in messages:
        if i.isalnum():
            y.append(i)
    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)

# Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    input_message = request.form['message']
    transformed_message = transform_messages(input_message)
    vector_input = tfidf.transform([transformed_message])
    prediction = model.predict(vector_input)[0]
    output = "Spam" if prediction == 1 else "Not Spam"
    
    return render_template('index.html', prediction_text='Prediction: {}'.format(output))

if __name__ == "__main__":
    app.run(debug=True)
