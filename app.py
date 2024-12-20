from flask import Flask, request, jsonify
import joblib
import pandas as pd

# Load the pre-trained model
model = joblib.load('shipment_delay_model.pkl')

# Create Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return "Shipment Delay Prediction API is Running"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get JSON data from the request
        data = request.get_json()

        # Convert data to DataFrame
        input_data = pd.DataFrame([data])

        # Make prediction
        prediction = model.predict(input_data)
        prediction_label = 'Delayed' if prediction[0] == 1 else 'On Time'

        # Return the result
        return jsonify({
            'prediction': prediction_label
        })

    except Exception as e:
        return jsonify({
            'error': str(e)
        }), 400

if __name__ == '__main__':
    app.run(debug=True)
