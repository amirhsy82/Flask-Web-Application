from Blog import db
from datetime import datetime


class test_paids(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, primary_key=True)
    test_id = db.Column(db.Integer, primary_key=True)
    result_id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, nullable=False)

class Psychology_tests(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text, nullable=False)
    title = db.Column(db.String(40))
    price = db.Column(db.Integer)
    description = db.Column(db.String)
    image = db.Column(db.String)
    question_count = db.Column(db.Integer)

class test_results(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    test_id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Text, nullable=False)
    title = db.Column(db.String(120), nullable=False)
    short_answer = db.Column(db.String(150), nullable=False)
    long_answer = db.Column(db.Text, nullable=False)
