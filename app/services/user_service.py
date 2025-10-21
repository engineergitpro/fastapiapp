from app.models.user_model import User

def get_all_users():
    return [
        User(id=1, name="Sagar"),
        User(id=2, name="Aarti"),
        User(id=3, name="Alok")
    ]
