from flask import Flask, render_template, redirect, url_for, request, session
# import mlab
import re
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/xich-du-nhun-nhay-jumperkids')
def sp():
    return render_template('page_sp.html')

if __name__ == '__main__':
  app.run(debug=True)
