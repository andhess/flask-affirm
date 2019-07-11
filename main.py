from flask import Flask, render_template, request
from flask_assets import Bundle, Environment
import requests
from requests.auth import HTTPBasicAuth

import secret

app = Flask(__name__)
assets = Environment(app)

# add JS contents
js = Bundle('js/*')
assets.register('js_all', js)

# add less CSS
css = Bundle('main.less', filters='less', output='main.css')
assets.register('css_all', css)


# home page and product page
@app.route('/')
def product_page():
  return render_template('product.html')


# the checkout page to trigger Affirm
@app.route('/checkout')
def checkout_page():
  return render_template('checkout.html')


# Affirm will trigger this page on success
@app.route('/success', methods=['POST'])
def purchase_success():
  auth = HTTPBasicAuth(secret.AFFIRM_PUBLIC, secret.AFFIRM_PRIVATE)
  checkout_token = request.form['checkout_token']
  payload = {'checkout_token': checkout_token}

  # make request
  r = requests.post('https://sandbox.affirm.com/api/v2/charges', auth=auth, json=payload)
  charge_id = r.json()['id']

  if r.status_code == 200:
    return render_template('success.html', checkout_token=checkout_token, charge_id=charge_id)

  else:
    return render_template('cancel.html')


# Affirm will trigger this page on fail
@app.route('/cancel')
def purchase_fail():
  return render_template('cancel.html')

