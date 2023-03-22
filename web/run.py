# from flask import Flask, render_template

# app=Flask(__name__, template_folder='templates')
# app.debug = True

# @app.route("/")
# def helloWorld():
#     return "<p>Hello, World!</p>"

# @app.route("/home")
# def home():
#     return render_template('home.html')

# if __name__ == '__main__':
#     app.run(host='localhost', port=8080)

# from flask import Flask,render_template

# app=Flask(__name__,template_folder='templates')
# app.debug = True

# @app.route("/")
# def helloworld():
#     return "<p>Hello, World!</p>"

# @app.route("/home")
# def home():
#     return render_template('home.html')

# @app.route("/form")
# def form():
#     return render_template('form.html')

# @app.route("/image")
# def image():
#     return render_template('image.html')

# if __name__ == '__main__':
#     app.run(host='localhost', port=5050)

# Importing necessary modules from Flask library
from flask import Flask, render_template, request

# Creating an instance of Flask class and defining the directory of templates
app = Flask(__name__, template_folder='templates')

# Setting the debugging mode on for development purposes
app.debug = True

# Setting up a route to the root directory of the application
@app.route("/")
def index():
    return render_template('index.html')

# Setting up a route for the form submission which calculates BMI
@app.route('/calculate', methods=['GET', 'POST'])
def calculate():
    # Checking if the method is POST, meaning that the form was submitted
    if request.method == 'POST':
        # Extracting data from the form
        gender = request.form['gender']
        weight = float(request.form['weight'])
        height = float(request.form['height'])
        
        # Calculating the BMI and rounding it to two decimal places
        bmi = round((weight / (height ** 2)), 2)
        
        # Checking if the user is male or female and determining the BMI category accordingly
        if gender == 'male':
            if bmi < 20.7:
                result = 'Underweight'
            elif bmi >= 20.7 and bmi < 26.4:
                result = 'Normal'
            elif bmi >= 26.4 and bmi < 27.8:
                result = 'Overweight'
            else:
                result = 'Obese'
        else:
            if bmi < 19.1:
                result = 'Underweight'
            elif bmi >= 19.1 and bmi < 25.8:
                result = 'Normal'
            elif bmi >= 25.8 and bmi < 27.3:
                result = 'Overweight'
            else:
                result = 'Obese'
        
        # Rendering the result template with the calculated BMI and BMI category
        return render_template('result.html', bmi=bmi, result=result)
    
    # If the method is GET, which means the user has not submitted the form yet
    else:
        # Render the index.html file containing the BMI calculator form
        return render_template('index.html')

# Starting the Flask application on a local server
if __name__ == '__main__':
    app.run(host='localhost', port=5050)
