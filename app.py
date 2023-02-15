from flask import Flask, render_template, request

app = Flask(__name__)

@app.get('/fizzbuzz')
def fiz_app():
     return render_template('my_htm.html')