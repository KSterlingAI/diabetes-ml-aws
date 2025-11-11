# Diabetes ML + AWS

Proyecto de ejemplo: Entrenamiento de un modelo de ML para predecir diabetes y despliegue en AWS (S3 + Lambda).

## Contenidos
- `data/diabetes.csv` — dataset (o `diabetes.csv` en la raíz)
- `notebook/diabetes_ml.ipynb` — notebook de entrenamiento
- `app/lambda_function.py` — código para AWS Lambda
- `deploy_guide.md` — pasos de despliegue

## Ejecución local
1. Instala dependencias:
   `pip install -r requirements.txt`
2. Ejecuta notebook o script para entrenar y generar `model.pkl` y `scaler.pkl`.

## Deploy rápido
1. Subir `model.pkl` y `scaler.pkl` a S3.
2. Crear Lambda y asociar role que permita GetObject en S3.
3. Crear API Gateway y probar con POST JSON:
```json
{"features":[6,148,72,35,0,33.6,0.627,50]}
