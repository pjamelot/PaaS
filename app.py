from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/')
def hello_world():
     return "Hello World!"

@app.route('/add_two_nums', methods=["POST"])
def add_two_nums():
    # Get x,y from the posted data
    dataDict = request.get_json()
#    return jsonify(dataDict)
 
    if "y" not in dataDict:
        return "Error", 305

    x = dataDict["x"]
    y = dataDict["y"]


    #Add Z=x+y
    z = x+y

    #Prepare JSON
    retJSON = {
        "z":z
    }

    #return jsonify(map_prepared)
    return jsonify(retJSON), 200



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