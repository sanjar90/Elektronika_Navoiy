import uvicorn
from fastapi import FastAPI
from sqladmin import Admin, ModelView
from models import engine, User

app1 = FastAPI()
admin = Admin(app1, engine)


class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.name, User.image]


admin.add_view(UserAdmin)

if __name__ == "__main__":
    uvicorn.run(app1, host="127.0.0.1", port= 8001)