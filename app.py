from flask import Flask, render_template, request, jsonify 
from utils.logic import improve_commit 
app = Flask(__name__) 
@app.route("/") 
def home(): 
return render_template("index.html") 
@app.route("/improve", methods=["POST"]) 
def improve(): 
data = request.get_json() 
msg = data.get("msg", "") 
result = improve_commit(msg) 
return jsonify({"result": result}) 
if __name__ == "__main__": 
app.run(debug=True)
