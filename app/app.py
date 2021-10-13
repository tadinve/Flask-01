from flask import Flask, request, make_response
from datetime import datetime as dt

from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object(Config)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://test:test@db/test"
db = SQLAlchemy(app)
migrate = Migrate(app, db) # this

class Account(db.Model):
    """Model for accounts."""

    __tablename__ = 'account'

    id = db.Column(db.Integer,
                   primary_key=True)
    name = db.Column(db.String(64),
                     index=False,
                     unique=True,
                     nullable=False)
    created_at = db.Column(db.DateTime,
                        index=False,
                        unique=False,
                        nullable=False)

    def __repr__(self):
        return '<Account {}>'.format(self.name)
 
@app.route('/')
def hello_whale():
    return ("Whale, Hello there! Glad to see you!")


@app.route('/accounts/', methods=['POST'])
def create_user():
    """Create an account."""
    data = request.get_json()
    name = data['name']
    if name:
        new_account = Account(name=name,
                              created_at=dt.now())
        db.session.add(new_account)  # Adds new User record to database
        db.session.commit()  # Commits all changes
        return make_response(f"{new_account} successfully created!")
    else:
        return make_response(f"Name can't be null!")
 
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')