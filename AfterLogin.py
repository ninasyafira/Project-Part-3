from flask import Flask, render_template, request, session
from wtforms import Form, StringField, validators
import Process
import datetime


app = Flask(__name__)


@app.route('/')
def home():
    session['userid'] = 'Jeff'
    now = datetime.datetime.now()
    todayMonth = now.month
    todayYear = now.year
    months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November','December')

    if todayMonth == 1:
        prevMonth = 12
    else:
        prevMonth = todayMonth - 1

    if todayYear == 2018 :
        prevYear = 2017
    else :
        prevYear = now.year - 1

    usersList = []
    usersList = Process.processUser(session['userid'], todayMonth, todayYear)
    savings = []
    totalLeft = Process.savingsLeft(session['userid'], todayMonth, todayYear)
    limit = []
    limit = Process.limit(session['userid'],todayMonth,todayYear)
    over = Process.over(session['userid'],todayMonth,todayYear)
    return render_template('homepage.html', users=usersList,saving=savings,todayMonth=todayMonth, prevMonth=prevMonth, todayYear=todayYear, prevYear=prevYear, left=totalLeft,limits=limit,over=over)

@app.route('/hey')
def hey():
    return render_template('homepage2.html')


@app.route('/dec')
def dec():
    session['userid'] = 'Jeff'

    now = datetime.datetime.now()
    todayMonth = now.month
    todayYear = now.year
    months = ('January','February','March','April','May','June','July','August','September','October','November','December')

    if todayMonth == 1:
        prevMonth = 12
    else :
        prevMonth = todayMonth - 1

    if todayYear == 2018 :
        prevYear = 2017
    else :
        prevYear = now.year - 1
    usersList = []
    usersList = Process.processUser(session['userid'],prevMonth,prevYear)
    totalLeft = Process.savingsLeft(session['userid'], prevMonth, prevYear)
    limit = []
    limit = Process.limit(session['userid'], prevMonth, prevYear)
    over = Process.over(session['userid'], prevMonth, prevYear)

    return render_template('dec.html',users=usersList,todayMonth=todayMonth, prevMonth=prevMonth, todayYear=todayYear, prevYear=prevYear,left=totalLeft,limits=limit,over=over)

@app.route('/nov')
def nov():
    usersList = []
    usersList = Process.processUser()
    return render_template('nov.html',mary=usersList)

@app.route('/dec2016')
def dec2016():
    return render_template('dec2016.html')

@app.route('/nov2016')
def nov2016():
    return render_template('nov2016.html')

@app.route('/views')
def views():
    return render_template('views.html')

@app.route('/graph')
def graph():
    return render_template('Graph.html')

@app.route('/details')
def details():
    return render_template('Details.html')


if __name__ == '__main__':
    app.secret_key = 'secret123'
    app.run()

