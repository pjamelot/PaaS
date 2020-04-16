from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
     return "Hello World!"

@app.route('/bye')
def bye():
     age = 2*5
     retJson = {
         'Name':'toto',
         'Age': age,
         "phones":[
             {
                "phoneName": "iphone7",
                "phoneNumber": 1111
             },
             {
                 "phoneName": "Nokia",
                 "phoneNumber": 2222
             }   
          ]
    }
     return jsonify(retJson)

if __name__=="__main__":
  app.run(debug=True)