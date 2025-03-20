import boto3
from botocore.exceptions import NoCredentialsError

# AWS DynamoDB 設定
TABLE_NAME = "AI_Models_DB"

# DynamoDB クライアントのセットアップ
dynamodb = boto3.resource("dynamodb", region_name="us-east-1")
table = dynamodb.Table(TABLE_NAME)

def get_all_models():
    """AIモデル一覧を取得"""
    try:
        response = table.scan()
        return response.get("Items", [])
    except NoCredentialsError:
        return {"error": "AWS credentials not found"}

def update_model(ai_name, update_data):
    """AIモデルの情報を更新"""
    try:
        response = table.update_item(
            Key={"AI_Name": ai_name},
            UpdateExpression="SET " + ", ".join(f"{k} = :{k}" for k in update_data.keys()),
            ExpressionAttributeValues={f":{k}": v for k, v in update_data.items()},
            ReturnValues="ALL_NEW",
        )
        return response.get("Attributes", {})
    except NoCredentialsError:
        return {"error": "AWS credentials not found"}
