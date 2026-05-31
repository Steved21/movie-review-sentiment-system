async function analyzeSentiment() {
    const review = document.getElementById('reviewInput').value;

    if (review.trim() === '') {
        alert('Please enter a review');
        return;
    }

    const response = await fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            review: review
        })
    });

    const data = await response.json();

    const resultDiv = document.getElementById('result');

    if (data.sentiment === 'positive') {
        resultDiv.innerHTML =
            'Sentiment: <span class="positive">Positive 😊</span>';
    } else {
        resultDiv.innerHTML =
            'Sentiment: <span class="negative">Negative 😞</span>';
    }
}

async function loadHistory() {
    const response = await fetch('/history');
    const data = await response.json();

    const historyDiv = document.getElementById('history');

    historyDiv.innerHTML = '';

    data.reverse().forEach(item => {
        historyDiv.innerHTML += `
            <div class="review-card">
                <p><strong>Review:</strong> ${item.review}</p>
                <p><strong>Prediction:</strong> ${item.prediction}</p>
                <p><strong>Date:</strong> ${item.date}</p>
            </div>
        `;
    });
}


async function getRecommendations() {

    const movie = document.getElementById('movieInput').value;

    const response = await fetch('/recommend', {

        method: 'POST',

        headers: {
            'Content-Type': 'application/json'
        },

        body: JSON.stringify({
            movie: movie
        })

    });

    const data = await response.json();

    const recommendationsDiv =
        document.getElementById('recommendations');

    recommendationsDiv.innerHTML = '';

    data.recommendations.forEach(movie => {

        recommendationsDiv.innerHTML += `
            <div class="recommend-card">
                ${movie}
            </div>
        `;
    });
}