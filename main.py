from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import os
from datetime import datetime
from typing import Optional

# Initialize FastAPI app
app = FastAPI()

# Pydantic model for input data
class PredictionInput(BaseModel):
    features: list[float]  # Adjust based on your model's expected input

# Pydantic model for model metadata
class ModelMetadata(BaseModel):
    model_name: str
    version: str
    created_at: str
    last_updated: str
    performance_metrics: Optional[dict] = None

# Load your model (replace with actual model loading)
try:
    # Example: model = pickle.load(open("model.pkl", "rb"))
    model = None  # Placeholder for your actual model
    MODEL_METADATA = ModelMetadata(
        model_name="sample_model",
        version="1.0.0",
        created_at="2023-01-01",
        last_updated=datetime.now().isoformat(),
        performance_metrics={"accuracy": 0.95, "precision": 0.93}
    )
except Exception as e:
    print(f"Error loading model: {e}")
    model = None
    MODEL_METADATA = None

@app.get("/")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "message": "Service is running",
        "timestamp": datetime.now().isoformat()
    }

@app.post("/predict")
async def predict(input_data: PredictionInput):
    """Main prediction endpoint"""
    if model is None:
        return {"error": "Model not loaded"}
    
    try:
        # Make prediction (adjust based on your model's predict method)
        prediction = model.predict([input_data.features])[0]
        return {
            "prediction": float(prediction),  # Convert numpy types to native Python
            "status": "success",
            "timestamp": datetime.now().isoformat()
        }
    except Exception as e:
        return {"error": str(e), "status": "error"}

@app.get("/model-info")
async def get_model_info():
    """Return model metadata"""
    if MODEL_METADATA is None:
        return {"error": "Model metadata not available"}
    return MODEL_METADATA

# For development
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)