from fastapi import FastAPI

from api.models.user_model import UserModel

app = FastAPI()


# @app.post("/add-users")
@app.put("/add-users")
def add_users(model: UserModel):
    return [f"My name is {model.name} and my skills are {model.skills}"]
