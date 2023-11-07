from flask import Flask, render_template
from montecarlo import montecarlo

app = Flask(__name__)

#landing page
@app.route('/')
def hello_world():
    return 'Hello World!'

#monte carlo page
#the extension will be the number of simulations and the function provides pi to the template
@app.route('/montecarlo/<int:numsims>')
def calcpi(numsims):
    return render_template('calcpi.html', numsims = numsims, pi = float(montecarlo(numsims)))

if __name__ == '__main__':
    app.run()
