import sqlite3
from db import db

class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(100))
    userpassword = db.Column(db.String(100))

    def __init__(self,id,username,userpassword):
        self.id = id
        self.username = username
        self.userpassword = userpassword

    @classmethod
    def find_by_name(cls,name):
        return cls.query.filter_by(username=name).first()

    def save_to_db(self):
            db.session.add(self)
            db.session.commit()
    def delete_to_db(self):
            db.session.delete(self)
            db.session.commit()
            # return {'entered name':self.username}
            
            # return {'messasge':"Some Error to Add Record"}




