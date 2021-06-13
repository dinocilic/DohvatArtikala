from flask import Flask, render_template, request
import requests
from requests.auth import HTTPBasicAuth

app = Flask(__name__)
app.debug = True

@app.template_filter()
def currencyFormat(value):
    value = float(value)
    return "{:,.2f} KN".format(value)

@app.route('/', methods=['GET', 'POST'])
def home():
    res = requests.get('http://apidemo.luceed.hr/datasnap/rest/artikli/naziv', auth=HTTPBasicAuth('luceed_mb', '7e5y2Uza'), params={'q': request.form.get('query')})
    results = res.json()
    podaci = results['result']
    
    return render_template("home.html", podaci=podaci)

if __name__ == "__main__":
    app.run(debug=True)