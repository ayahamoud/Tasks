from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

#----------root's route-------------
@app.route("/")
def Hello_world():
    return "Hello, Flask!"

#----------additional routes----------
app.add_url_rule('/hello','hello',Hello_world)

@app.route("/India")
def india():
    return 'Namaste!'

@app.route("/Spain")
def spain():
    return 'Hola!'

#-----------dynamic content-----------
@app.route("/Germany/<capital>")
def germany(capital):
    return 'Hallo '+capital+'!'

@app.route('/user/<country>')
def display_user(country):
    if country=='India':
        return redirect(url_for('india'))
    elif country == 'Germany':
        return redirect(url_for('germany',capital = 'Frankfurt'))
    elif country == 'Spain':
        return redirect(url_for('spain'))

#-------------------------------
@app.route('/success/<name>')
def success(name):
    return "Welcome %s" % name

@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name = user))
    else:
        return render_template('login.html')

if __name__ == '__main__':
    app.run()
