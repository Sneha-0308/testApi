import json
from flask import Flask,jsonify,request,Response
from googletrans import Translator

app = Flask(__name__)



translator = Translator()


@app.route("/translate", methods=['GET','POST'])
def translateKN():
    # if request.method=='POST':
    content = request.get_json()
    value=content.get('content')
    result=translator.translate(value, src='en', dest='kn')
    result=result.text
        # result.text 
    return result
        # return Response(json.dumps(result))
        

if __name__ == "__main__":
    app.run()


