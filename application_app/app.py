'''
from flask import Flask
app = Flask(__name__)

@app.route('/')

def home():
    return "Hellow"

app.run(port = 8000)
DEBUG=True
'''
'''
from mymodule import divide
x = divide(50,2)
print(f"Divide is : {x}")
'''
'''
list = (10,20,30,40)
def divident(div,divby):
    return div / divby

print(divident(sum(list),5))
'''

# from flask import Flask,jsonify,request
# from flask_restful import Resource,Api

# app = Flask(__name__)
# api = Api(app)

from distutils.log import debug

import re
from typing import List
from flask import Flask, jsonify,request
from flask_restful import Resource,Api,reqparse
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer
#from models import user
from models.user import UserModel


#from models import user

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config.setdefault('SQLALCHEMY_BINDS', None)
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()



class showUser(Resource):
    def get(self,name):
        _user = UserModel.find_by_name(name)
        if _user:
            return [_user.id,_user.username,_user.userpassword] #_user.userpassword
            #return {'User Name':name} #return jsonify({'User Record':_user}) #_user.json()
        return {'message':"the User Name {} Not Founded ".format(name)}
        


class addUser(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('id', type = int)
    parser.add_argument('username', type = str)
    parser.add_argument('userpassword', type = str)



    def post(self):
        #return {'Kuch bhi':"noo"}
        data = addUser.parser.parse_args()
        _data = UserModel(data['id'],data['username'],data['userpassword'])
        _data.save_to_db()
        return {'message':"Data Save Successfully"}
        #return {'Kuch bhi':"noo"}
        #user_model = UserModel(**data)
        #return jsonify(user_model)
        #user_model = UserModel(data['id'],data['username'],data['userpassword'])
        #user_model.save_to_db()

    

class deleteUser(Resource):
    def delete(self,name):
        user_deleted = UserModel.find_by_name(name)
        _message = "Record Not Found"
        if user_deleted:
            user_deleted.delete_to_db()
            _message = "Record Delete Successfully"

        return {'message':_message}
        
        
api.add_resource(showUser,'/ShowUser/<string:name>')
api.add_resource(addUser,'/AddUser')
api.add_resource(deleteUser,'/DeleteUser/<string:name>')

if __name__ == '__main__':
    
    from db import db
    db.init_app(app)
    app.run(port=5000,debug = True)




