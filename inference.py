
import pickle
from flask import Flask, request, jsonify
import numpy as np

app = Flask(__name__)

# Load the trained model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    
    
    features = np.array(data['features']).reshape(1, -1)  # Reshape for model input
    
    # Make a prediction
    prediction = model.predict(features)
    
    # Return the prediction
    return jsonify({'anomaly': prediction[0].item()})

if __name__ == '__main__':
    app.run(debug=True)
