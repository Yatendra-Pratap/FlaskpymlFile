from flask import Flask, render_template, request, redirect, url_for
import os
import yaml

app = Flask(__name__)

# Define the directory where user data files will be stored
USER_DATA_DIR = 'user_data'

# Create the user data directory if it doesn't exist
os.makedirs(USER_DATA_DIR, exist_ok=True)

@app.route('/')
def login_page():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']

        # Create a file for the user's data
        user_data_file = os.path.join(USER_DATA_DIR, f'{username}.pyml')
        data = {'username': username, 'email': email}
        with open(user_data_file, 'w') as file:
            yaml.dump(data, file, default_flow_style=False)

        return redirect(url_for('success', username=username))

@app.route('/success/<username>')
def success(username):
    return render_template('success.html', username=username)

if __name__ == '__main__':
    app.run(debug=True)
