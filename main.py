from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import os

app = Flask(__name__, template_folder="html")
rests_df = pd.DataFrame({"Name": [], "Cuisine": [], "Seats": []})


@app.route('/')
def landing():
    return render_template("first.html")

@app.route('/login_rest')
def login_rest():
    return render_template("login_rest.html")

@app.route('/login_cust')
def login_cust():
    return render_template("login_cust.html")

@app.route('/login_rest_post', methods=['GET', 'POST'])
def login_rest_post():
    if request.method == "GET":
        rest_name = request.form["name"]
        rest_cuisines = request.form["cuisines"]
        rest_seats = request.form["seats"]
    restaurant = {"Name": rest_name, "Cuisines": rest_cuisines, "Seats": rest_seats}
    rests_df.append(restaurant)
    rest_df.to_csv("./csv/rests.csv")

@app.route('/login_cust_post', methods=['GET', 'POST'])
def login_cust_post():
    if request.method == "GET":
        cust_name = request.form["name"]
        cust_cuisines = request.form["cuisines"]
        cust_seats = request.form["seats"]

if __name__ == '__main__':
    app.run(debug=True)
