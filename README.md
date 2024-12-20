# Shipment Delay Prediction API

## Overview
This API predicts whether a shipment will be delayed or arrive on time based on shipment details such as origin, destination, vehicle type, weather, and traffic conditions.

---

## Features
- Predict shipment delay status (`On Time` or `Delayed`).
- Accepts input data in JSON format.
- Lightweight and fast API built with Flask.

---

## Prerequisites
1. Python 3.7 or higher.
2. Required Python libraries:
   - Flask
   - pandas
   - joblib
   - scikit-learn

Install dependencies with:
```bash
pip install flask pandas joblib scikit-learn

## Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/your-repo/shipment-delay-prediction-api.git
cd shipment-delay-prediction-api
```

### 2. Place the Model File
Model file can be obtained by running the p1_mopel.py. It creates a pickle file called `shipment_delay_model.pkl`. 
Ensure the `shipment_delay_model.pkl` file is in the same directory as `app.py`.

### 3. Run the Flask Application
Start the server with:

```bash
python app.py
```

The API will be available at [http://127.0.0.1:5000](http://127.0.0.1:5000).

## Endpoints

### 1. Health Check
**URL:** `/`

**Method:** `GET`

**Description:** Checks if the API is running.

**Response:**
```json
{
  "message": "Shipment Delay Prediction API is Running"
}
```

### 2. Predict Shipment Delay
**URL:** `/predict`

**Method:** `POST`

**Headers:**
- `Content-Type: application/json`

**Request Body:** JSON containing shipment details:
```json
{
    "Origin": "Mumbai",
    "Destination": "Delhi",
    "Shipment Date": "2024-12-20",
    "Vehicle Type": "Truck",
    "Distance": 1500,
    "Weather Conditions": "Clear",
    "Traffic Conditions": "Moderate"
}
```

**Response:**
```json
{
    "prediction": "Delayed"
}
```

## Example Usage

### Using Curl
```bash
curl -X POST http://127.0.0.1:5000/predict \
-H "Content-Type: application/json" \
-d '{
    "Origin": "Mumbai",
    "Destination": "Delhi",
    "Shipment Date": "2024-12-20",
    "Vehicle Type": "Truck",
    "Distance": 1500,
    "Weather Conditions": "Clear",
    "Traffic Conditions": "Moderate"
}'
```

### Using Postman
1. Open Postman.
2. Create a new `POST` request to `http://127.0.0.1:5000/predict`.
3. Add `Content-Type: application/json` in the Headers.
4. Add the JSON request body with shipment details.
5. Click **Send** to get the prediction.

## Notes
- Ensure the Flask server is running locally on port `5000`.
- Input JSON should match the model's expected features.
- If `shipment_delay_model.pkl` is updated, retrain and save the model using the correct pipeline.
