from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/shiori'
db = SQLAlchemy(app)

from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

class BaseModel(db.Model):
    """Base data model for all objects"""
    __abstract__ = True

    def __init__(self, *args):
        super().__init__(*args)

    def __repr__(self):
        """Define a base way to print models"""
        return '%s(%s)' % (self.__class__.__name__, {
            column: value
            for column, value in self._to_dict().items()
        })

    def json(self):
        """
                Define a base way to jsonify models, dealing with datetime objects
        """
        return {
            column: value if not isinstance(value, datetime.date) else value.strftime('%Y-%m-%d')
            for column, value in self._to_dict().items()
        }


class Site(BaseModel, db.Model):
    """Model for the stations table"""
    __tablename__ = 'sites'

    id = db.Column(db.Integer, primary_key = True)
    url = db.Column(db.string, primary_key = True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return 'Natalie Loh'

if __name__ == '__main__':
    app.run()
    manager.run()
