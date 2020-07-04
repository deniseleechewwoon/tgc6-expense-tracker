from flask import Flask, render_template, request, redirect, url_for, flash
import pymongo
from dotenv import load_dotenv
from bson import ObjectId
import os
import datetime

# load in the variables in the .env file into our operating system environment
load_dotenv()

app = Flask(__name__)

# connect to mongo
MONGO_URI = os.environ.get('MONGO_URI')
client = pymongo.MongoClient(MONGO_URI)

# define my db_name
DB_NAME = "expensetracker"

# read in the SESSION_KEY variable from the operating system environment
SESSION_KEY = os.environ.get('SESSION_KEY')

# set the session key
app.secret_key = SESSION_KEY

# START WRITING YOUR CODE


@app.route('/')
def home():
    return"Welcome Home"

# collect Income and expenditure data


@app.route('/ie/create')
def show_create_form():
    return render_template('create_expenses.template.html')


@app.route('/ie/create', methods=['POST'])
def create_ie():
    ie_name = request.form.get('ie_name')
    ie_amount = request.form.get('ie_amount')
    ie_date = request.form.get('ie_date')
    transaction_type = request.form.get('transaction_type')
    transaction_reconciled = request.form.get('transaction_reconciled')

    client[DB_NAME].incomeandexpenditure.insert_one({
        'ie_name': ie_name,
        'ie_amount': ie_amount,
        'ie_date': datetime.datetime.strptime(ie_date, "%Y-%m-%d"),
        'transaction_type': transaction_type,
        'transaction_reconciled': transaction_reconciled
    })

    return "Income and expenditure created successfully"


# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
