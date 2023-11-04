from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_post():
    username = request.form['username']
    password = request.form['password']
    # Here, you should implement your own logic for user authentication
    if username == 'admin' and password == 'admin123':
        return redirect(url_for('success'))
    else:
        return redirect(url_for('login'))

@app.route('/success')
def success():
    return "Login successful!"

if __name__ == '__main__':
    app.run(debug=True)
