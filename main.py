from flask import Flask, render_template
from flask_assets import Bundle, Environment

app = Flask(__name__)
assets = Environment(app)

# add JS contents
js = Bundle('main.js')
assets.register('js_all', js)

# add less CSS
css = Bundle('main.less', filters='less', output='main.css')
assets.register('css_all', css)


@app.route('/')
def product_page():
  return render_template('product.html')


@app.route('/checkout')
def checkout_page():
  return render_template('checkout.html')