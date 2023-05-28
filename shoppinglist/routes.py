from flask import render_template
from shoppinglist import app, db
from shoppinglist.models import List, Item


@app.route("/")
def home():
    return render_template("base.html")

@app.route('/login')
def login():
    return render_template('login.html')


# @app.route('/auth', methods=['POST'])
# def auth():
#     token = request.form['id_token']
#     try:
#         # Verify the Google ID token
#         id_info = id_token.verify_oauth2_token(
#             token, requests.Request(), CLIENT_ID)
#         if id_info['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
#             raise ValueError('Invalid issuer.')

#         # You can access the user information from the id_info dictionary
#         email = id_info['email']
#         name = id_info['name']
#         # Add your own logic to handle the authenticated user

#         return 'Authentication successful!'
#     except ValueError:
#         return 'Authentication failed!'
