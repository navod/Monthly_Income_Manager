# from flask import Flask,request,Response
# from flask.templating import render_template
# from flask_sqlalchemy import SQLAlchemy
# from werkzeug.utils import secure_filename
# import os
# import boto3
# from io import StringIO
# from flask_cors import CORS, cross_origin


# application = Flask(__name__)
# # DB_URI = os.environ.get("DB_URI")
# # DB_URI = "mysql+pymysql://admin:navod2000@aaio2anxazhoo8.ckqyp22eptyw.us-east-2.rds.amazonaws.com:3306/ebdb"
# # application.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
# # db = SQLAlchemy(application)

# # bucket_name = "testprofileuploadnavod"

# # class User(db.Model):
# #     id = db.Column(db.Integer, primary_key=True)
# #     username = db.Column(db.String(80), unique=True, nullable=False)
# #     email = db.Column(db.String(120), unique=True, nullable=False)

# #     def __repr__(self):
# #         return '<User %r>' % self.username

# # db.create_all()

# @application.route("/whishlist",methods=["POST"])
# @cross_origin()
# def create_user():
#     try:
#         print(request)
#         # user={"name":request.form["name"],"lastName":request.form["lastName"]}
#         # dbResponse = db.users.insert_one(user)
#         # # print(dbResponse.inserted_id)

#         return Response(
#             response= json.dumps({"message":"user created","id": f"{id:1}"}),
#             status=200,
#             mimetype="application/json"
#         )
#         # user={"userName":request.json['userName'],"email":request.json["email"],"salary":request.json["salary"],"address":request.json["salary"]}
#         # dbResponse = db.users.insert_one(user)
#         # return Response(
#         #     response= json.dumps({"message":"user created","id": f"{dbResponse.inserted_id}"}),
#         #     status=200,
#         #     mimetype="application/json"
#         # )

#     except Exception as ex:
#         print(ex)
# # @application.route("/user/add")
# # def user_add():
# #     admin = User(username='admin', email='admin@example.com')
# #     db.session.add(admin)
# #     db.session.commit()
# #     return "Item add"

# # @application.route("/upload_image",methods=["GET","POST"])
# # def upload_image():
# #     print(request.method)
# #     if request.method =='POST':
# #         file = request.files['profile_pic']
# #         file_name = secure_filename(file.filename)
# #         print(file_name)
# #         print(file_name)
# #         file.save(file_name)
        
        
# #         response = client.upload_file(file_name, bucket_name,file_name)
# #         print(response)
# #     return render_template("upload_image_form.html")


# # @application.route("/view_image",methods=["GET"])
# # def save_image():
# #     response = client.download_file(bucket_name, "Untitled.png", "Untitled.png")
# #     return _serve_pil_image(response)
#     # print(response)
#     # return _serve_pil_image(response)

# # def _serve_pil_image(pil_img):
# #     img_io = StringIO()
# #     pil_img.save(img_io, 'PNG')
# #     img_io.seek(0)
# #     return send_file(img_io, mimetype='image/png', cache_timeout=0)

# # def send_file(a):
# #     print(a)
    
# # client = boto3.client(
# #     's3',
# #     aws_access_key_id = "AKIAV3MCP2ZA6AC77WRK",
# #     aws_secret_access_key = "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"
# # )



# # @application.route("/user/list")
# # def get_all_users():
# #     all = User.query.all()
# #     return f"{[u.email for u in all]}"

# # @application.route("/")
# # def index():
# #     return render_template("index.html")


# # @application.route("/item")
# # def item_add():
# #     return "Item add"

# if __name__=="__main__":
#     application.run(debug=True)





from network import create_app


application = create_app()

if __name__=="__main__":
    application.run(debug=True)