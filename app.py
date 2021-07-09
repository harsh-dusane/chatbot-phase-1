from flask import Flask, request, jsonify
import requests

app = Flask(__name__)


@app.route('/query', methods=['POST'])
def get_bot_response():
    """
    this function is fetching query from the request body and then will get response from 
    rasa chatbot

    [ get query variable from the request body ]

    Returns:
        [json]: [response from the rasa]
    """
    try:
        data=request.get_json()
        query=data.get('query',None)

        if query==None or query==' ':
            raise Exception('Please provide query to chatbot')

        response=requests.post('http://localhost:5005/webhooks/rest/webhook',json={"message":query})    
        res=response.json()
        res=res[0]['text']

        return jsonify({"data":{"message":res}}),200

    except Exception as e:
        return jsonify({"data":{"error":str(e)}}),400

if __name__ == '__main__':
    app.run(debug=True) 