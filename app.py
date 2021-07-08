from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/query', methods=['POST'])
def get_bot_response():
    try:
        res="Hello"

        return jsonify({"OK":"true","data":{"message":res}}),200

    except Exception as e:
        return jsonify({"OK":"false","data":{"error":str(e)}}),400



if __name__ == '__main__':
  
    app.run(debug=True) 


