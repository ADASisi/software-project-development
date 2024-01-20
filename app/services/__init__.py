from app.model.user import User
from app import db

class AuthService:
    def register_user(self, username, password):
        new_user = User(username=username)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        return new_user

    def authenticate_user(self, username, password):
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            return user
        return None
    
