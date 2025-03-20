from fastapi import FastAPI
from db import get_all_models, update_model

app = FastAPI()

@app.get("/get-ai-models")
def get_models():
    """AIモデル一覧を取得"""
    return {"models": get_all_models()}

@app.post("/update-ai-model")
def update_model_data(ai_name: str, update_data: dict):
    """AIモデルの情報を更新"""
    return update_model(ai_name, update_data)
