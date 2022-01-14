from flask import Blueprint, json, request, Response

from model.users import Users
from model import db
from flask_cors import CORS, cross_origin
from sqlalchemy import text

blue_print = Blueprint("users",__name__)

@blue_print.route("/api/users/save", methods=["POST"])
@cross_origin()
def users_add():
    try :
        userId = get_last_id()
        users = Users()
        users.userId = userId
        users.username = request.json['username']
        users.contact = request.json['contact']

        db.session.add(users)
        db.session.commit()

        return Response(
                response= json.dumps(users.userId),
                status=200,
                mimetype="application/json"
            )
    except Exception as ex :
        print(ex)
        return Response(
                response= json.dumps({"message":"user cannot add"}),
                status=500,
                mimetype="application/json"
            )

@blue_print.route("/api/users/login",methods=["POST"])
@cross_origin()
def login_user():
   
    try:
        username = request.json["username"]
        conatact = request.json["contact"]
        result = db.session.query(Users).filter(Users.username == username, Users.contact == conatact)
        data = result.first()
        # print(data)

        return Response(response= json.dumps(data.userId),status=200,mimetype="application/json")

    except Exception as ex:
        print(ex)
        return Response(
            response= json.dumps({"message":"Cannot get data"}),
            status=500,
            mimetype="application/json"
        )

def get_last_id():
    userId=""
    sql = text("select * from users ORDER BY userId DESC LIMIT 1")
    result = db.session.execute(sql)
    for row in result:
        userId = row.userId
    
    if userId == "":
        return "U0001"
    else:
        x = userId.split("U")
        userId = int(x[1])
        userId = userId +1
        if (userId < 10) :
            userId = "U000" + str(userId)
        elif (userId < 100) :
            userId = "U00" +str(userId)    
        elif (userId < 1000) :
            userId = "U0" + str(userId)    
        else:
            userId = "U" + str(userId)
        return userId
 
