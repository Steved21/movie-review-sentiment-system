from flask import Flask, render_template, request, jsonify
import pickle
import json
from datetime import datetime

app = Flask(__name__)

# Load trained model
model = pickle.load(open('model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    review = data['review']

    review_vector = vectorizer.transform([review])
    prediction = model.predict(review_vector)[0]

    review_data = {
        "review": review,
        "prediction": prediction,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    try:
        with open('reviews.json', 'r') as file:
            reviews = json.load(file)
    except:
        reviews = []

    reviews.append(review_data)

    with open('reviews.json', 'w') as file:
        json.dump(reviews, file, indent=4)

    return jsonify({
        "sentiment": prediction
    })

@app.route('/history')
def history():
    try:
        with open('reviews.json', 'r') as file:
            reviews = json.load(file)
    except:
        reviews = []

    return jsonify(reviews)

if __name__ == '__main__':
    app.run(debug=True)
