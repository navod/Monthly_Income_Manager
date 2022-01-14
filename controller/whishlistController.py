from flask import Blueprint, request,Response
from sqlalchemy.util.langhelpers import constructor_copy
from model.whishlist import Whishlist
from model import db
from model.whishlistDetail import WhishListDetail
from flask_cors import cross_origin
import json
from sqlalchemy import text

blue_print = Blueprint("whislist",__name__)
blue_print_2 = Blueprint("whishlistDetail",__name__)

@blue_print.route("/api/whilist/add", methods=["POST"])
@cross_origin()
def whishlist_add():
    try :
        whishlist_id = get_last_id()
        whishlist = Whishlist()
        whishlist.whishId = whishlist_id
        whishlist.description = request.json['description']
        whishlist.saveTo = request.json['saveTo']
        whishlist.color = request.json["color"]
        whishlist.saveType = request.json['saveType']
        whishlist.startSaveDate = request.json['startSaveDate']

        db.session.add(whishlist)
        db.session.flush()
        db.session.refresh(whishlist)
        is_added = whishlist_detail_add(whishlist.whishId)
        if is_added :
            db.session.commit()
            return Response(
                response= json.dumps({"message":"whishlist added"}),
                status=200,
                mimetype="application/json"
            )
    except Exception as ex :
        print(ex)
        return Response(
                response= json.dumps({"message":"Cannot add whishlist"}),
                status=500,
                mimetype="application/json"
        )
        


def whishlist_detail_add(whishlistId):
    wshDetail = WhishListDetail()
    wshDetail.whishId = whishlistId
    wshDetail.userId = request.json['userId']
    wshDetail.savedAmount = request.json['savedAmount']
    wshDetail.savedDate = request.json['savedDate']
    db.session.add(wshDetail)
    db.session.commit()
    return True


def get_last_id():
    whishlistId=""
    sql = text("select * from whishlist ORDER BY whishId DESC LIMIT 1")
    result = db.session.execute(sql)
    
    for row in result:
        whishlistId = row.whishId
    
    if whishlistId == "":
        return "W0001"
    else:
        x = whishlistId.split("W")
        whishlistId = int(x[1])
        whishlistId = whishlistId +1
        if (whishlistId < 10) :
            whishlistId = "W000" + str(whishlistId)
        elif (whishlistId < 100) :
            whishlistId = "W00" + str(whishlistId)    
        elif (whishlistId < 1000) :
            whishlistId = "W0" + str(whishlistId)    
        else:
            whishlistId = "W" + str(whishlistId)
        return whishlistId

@blue_print.route("/api/whishlistGet",methods=["GET"])
@cross_origin()
def get_whislist_Details():
    try:
        whishlist_items=[]
        id = request.args.get('userId')
        whishlistDetails = db.session.query(WhishListDetail).filter(WhishListDetail.userId == id).all()
        for whishlist in whishlistDetails :
            result = db.session.query(Whishlist).filter(Whishlist.whishId == whishlist.whishId).all()
            for whishlistDetail in result:
                whishlist_items.append({"whishlistId":whishlistDetail.whishId,
            "description":whishlistDetail.description,
            "saveTo":whishlistDetail.saveTo,
            "color":whishlistDetail.color,
            "saveType":whishlistDetail.saveType,
            "startSaveDate":whishlistDetail.startSaveDate,
            "savedAmount":whishlist.savedAmount,
            "savedDate":whishlist.savedDate})
        return Response(
                response= json.dumps(whishlist_items),
                status=200,
                mimetype="application/json"
         )


    except Exception as ex :
         return Response(
                response= json.dumps({"message":"Cannot get whishlist"}),
                status=500,
                mimetype="application/json"
        )

@blue_print.route("/api/updateWhishlit/<whishId>",methods=["PUT"])
@cross_origin()
def update_whishlist(whishId):
    try :
        whishlisDetail = db.session.query(WhishListDetail).filter(WhishListDetail.whishId==whishId).first()
        whishlisDetail.savedAmount = int(whishlisDetail.savedAmount) + int(request.json['savedAmount'])
        whishlisDetail.savedDate = request.json['savedDate']
        db.session.commit()

        return Response(
                response= json.dumps({"message":"whishlist updated"}),
                status=200,
                mimetype="application/json"
            )
    
    except Exception as ex :
       
        return Response(
                response= json.dumps({"message":"Cannot update whishlit"}),
                status=500,
                mimetype="application/json"
        )

@blue_print.route("/api/deletewhishlist/<whishId>",methods=["DELETE"])
@cross_origin()
def delete_whishlist(whishId):
    try :
        db.session.query(WhishListDetail).filter(WhishListDetail.whishId==whishId).delete()
        db.session.query(Whishlist).filter(Whishlist.whishId==whishId).delete()
        db.session.commit()
        
        return Response(
                response= json.dumps({"message":"whishlist deleted"}),
                status=200,
                mimetype="application/json"
            )
    
    except Exception as ex :
       
        return Response(
                response= json.dumps({"message":"Cannot delete whishlit"}),
                status=500,
                mimetype="application/json"
        )