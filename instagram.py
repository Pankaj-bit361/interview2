from flask import Flask,request,jsonify

app = Flask(__name__)

@app.route("/",methods=["GET"])
def get():
   return "hello"

@app.route("/post",methods=["POST"])
def post():
   data=request.get_json()
   data["id"]=data["name"]
   return jsonify("hello")

if __name__ == '__main__':
    app.run(port=8080)
