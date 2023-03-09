from flask import Flask, render_template

app=Flask(__name__, template_folder='templates')
app.debug = True

@app.route("/")
def helloWorld():
    return "<p>Hello, World!</p>"

@app.route("/home")
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(host='localhost', port=8080)