# deploy_guide.md

## Requisitos AWS
- Cuenta AWS con permisos para S3 y Lambda.
- AWS CLI configurado (aws configure).

## Pasos rápidos
1. Crear bucket S3: `aws s3 mb s3://tu-bucket-ml`
2. Subir modelos:
   `aws s3 cp model.pkl s3://tu-bucket-ml/model.pkl`
   `aws s3 cp scaler.pkl s3://tu-bucket-ml/scaler.pkl`
3. Crear función Lambda (Python 3.9+) y pegar `app/lambda_function.py`.
4. Configurar role IAM con permiso para leer S3.
5. Crear API Gateway para exponer la Lambda vía POST.
