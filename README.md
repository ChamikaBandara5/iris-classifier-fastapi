**ML Model API**

**Problem Description**

This API provides a way to make predictions using a trained machine learning model. The model is designed for classification tasks, such as predicting sentiment (positive, negative, neutral) from input features. The API allows users to send data and receive predictions with optional confidence scores.

**Model Information**

Model Type: RandomForestClassifier (example)

Problem Type: Classification

Input Features: feature1, feature2 (adjust according to your dataset)

Note: The trained model must be saved as model.pkl in the repository.

**API Usage**
**1. Health Check**
GET /


**Response:**

{
  "status": "healthy",
  "message": "ML Model API is running"
}

**2. Make a Prediction**
POST /predict


**Request Body:**

{
  "feature1": 5.2,
  "feature2": 3.8
}

**3. Get Model Information**
GET /model-info


**Response:**

{
  "model_type": "RandomForestClassifier",
  "problem_type": "classification",
  "features": ["feature1", "feature2"]
}


**Response:**

{
  "prediction": "positive",
  "confidence": 0.87
}


**Assumptions and Limitations**

Input features must match the features used during model training.

Confidence/probability is only available if the model has a predict_proba method.

Missing values or categorical features are not handled by this API — all inputs must be numeric.

The trained model file must be named model.pkl and present in the project directory.

**Repository Structure**
your-repo/
├── main.py          # FastAPI application
├── model.pkl        # Trained ML model
├── requirements.txt # Python dependencies
└── README.md        # Project documentation
