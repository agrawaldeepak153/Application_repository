from distutils.log import debug
from flask import Flask, jsonify,request
from flask_restful import Resource,Api
from flask_sqlalchemy import SQLAlchemy
#from models import user
from models.user import UserModel

#from models import user

app = Flask(__name__)
app.config['SQLALCHEMY__DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

class User(Resource):
    def get(self,name):
        _user = UserModel.find_by_name(name)
        if _user:
            return jsonify({'User Record':_user}) #_user.json()
        return {'message':"the User Name {} Not Found ".format(name)}
        


api.add_resource(User,'/ShowUser/<string:name>')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000,debug = True)

