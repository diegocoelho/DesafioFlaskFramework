from desafio.database import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), unique=True, nullable=False)
    password = db.Column(db.Text(), nullable=False)

    def __repr__(self) -> str:
        return 'User>>> {self.username}'
