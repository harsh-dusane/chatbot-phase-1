import functools, json, requests
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash


bp = Blueprint('bot', __name__)


@bp.route('/')
def index():
    """
        Index view to load UI to communicate with ChatBot
    """
    return render_template('bot/index.html')


@bp.route('/get')
def get_bot_response():
    """
        Endpoint which gets user input from frontend and requests 
        rasa for processing and provide response
    """
    val = request.args.get('msg')
    data = json.dumps({"sender": "Rasa","message": val})
    
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    res = requests.post('http://localhost:5005/webhooks/rest/webhook', data= data, headers = headers)
    
    res = res.json()
    val = res[0]['text']

    return str(val)

