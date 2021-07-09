# from flask import Flask, request, jsonify
# import requests

# app = Flask(__name__)


# @app.route('/query', methods=['POST'])
from flask_app import create_app


app = create_app()


if __name__ == '__main__':
    app.run(debug=True)