document.getElementById('send-btn').addEventListener('click', function() {
    const userInput = document.getElementById('user-input').value;
    const chatbox = document.getElementById('chatbox');
    
    chatbox.innerHTML += `<div class="user-message">${userInput}</div>`;
    
    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ features: userInput.split(',').map(Number) })
    })
    .then(response => response.json())
    .then(data => {
        const anomalyStatus = data.anomaly ? 'Anomaly Detected!' : 'No Anomaly';
        chatbox.innerHTML += `<div class="bot-message">${anomalyStatus}</div>`;
    })
    .catch(error => {
        console.error('Error:', error);
    });

    document.getElementById('user-input').value = '';
});
