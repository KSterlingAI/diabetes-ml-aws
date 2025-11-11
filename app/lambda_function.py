# app/lambda_function.py
import json
import boto3
import joblib
import numpy as np
from io import BytesIO

BUCKET = "tu-bucket-ml"
MODEL_KEY = "model.pkl"
SCALER_KEY = "scaler.pkl"

def load_model_from_s3():
    s3 = boto3.client('s3')
    model_obj = s3.get_object(Bucket=BUCKET, Key=MODEL_KEY)
    scaler_obj = s3.get_object(Bucket=BUCKET, Key=SCALER_KEY)
    model = joblib.load(BytesIO(model_obj['Body'].read()))
    scaler = joblib.load(BytesIO(scaler_obj['Body'].read()))
    return model, scaler

model, scaler = None, None

def lambda_handler(event, context):
    global model, scaler
    if model is None or scaler is None:
        model, scaler = load_model_from_s3()
    body = json.loads(event.get('body', '{}'))
    features = np.array(body['features']).reshape(1, -1)
    features_scaled = scaler.transform(features)
    prediction = int(model.predict(features_scaled)[0])
    return {'statusCode': 200, 'body': json.dumps({'prediction': prediction})}
