from flask import Flask, render_template, request, redirect, url_for
import pandas as pd

app = Flask(__name__, template_folder="html")

@app.route('/')
def landing():
    return render_template("first.html")

@app.route('/login_rest')
def login_rest():
    return render_template("login_rest.html")

@app.route('/login_cust')
def login_cust():
    return render_template("login_cust.html")

@app.route('/login_rest_post', methods=['POST'])
def login_rest_post():
    rests_df = pd.DataFrame({"Name": [], "Cuisine": [], "Seats": []})
    rest_name = request.form["name"]
    rest_cuisines = request.form["cuisines"]
    rest_seats = request.form["seats"]
    print(rest_name, rest_cuisines, rest_seats)
    restaurant = pd.DataFrame({"Name": [rest_name], "Cuisine": [rest_cuisines], "Seats": [rest_seats]})
    rests_df = pd.concat([rests_df, restaurant], ignore_index=True)
    rests_df.to_csv("./csv/rests.csv")
    return render_template("test.html")

@app.route('/login_cust_post', methods=['POST'])
def login_cust_post():
    cust_name = request.form["name"]
    cust_cuisines = request.form["cuisines"]
    cust_seats = request.form["seats"]
    return render_template("test.html")

if __name__ == '__main__':
    app.run(debug=True)
