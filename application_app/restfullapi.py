
from flask import Flask,jsonify,request
from flask_restful import Resource,Api

app = Flask(__name__)
api = Api(app)

#app.debug =True
# class Employee(Resource):
#     def get(self,name):
#         return {"Employee Name":name}

#     def post(self, name):
#         return {}

# api.add_resource(Employee,'/employee/<string:name>')
list1 = ["abc","bbc","ccc"]
#itemList =[]
# class Items(Resource):
#     def get(self,name):
#         if filter(lambda x:x['name']==name,ItemList):
#             return {'Item Name are': name}
#         else:
#             return {'Item Name Not Found': name}

class Items(Resource):
    def get(self,name):
        return {'Item':name}
        # _item = next(filter(lambda x: x['name']==name,list1),None)
        # return jsonify({'Item':_item})
            

api.add_resource(Items,'/showitem/<string:name>')
app.run(port=5000)



