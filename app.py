# Import Flask and render_template for rendering HTML templates
from flask import Flask, render_template, request

# Create Flask application
app = Flask(__name__)

# Route for Home Page

@app.route('/')
def home():
    # Passing a dynamic message and a list of items to the template
    message = "Welcome to Flask Dynamic Page!"
    items = ["Python", "Flask", "HTML", "CSS"]
    return render_template('index.html', msg=message, tech_list=items)

# Route for Greeting Page (Dynamic Input from User)
@app.route('/greet', methods=['POST'])
def greet():
    # Get the name entered by the user from the form
    user_name = request.form.get('username')
    return render_template('index.html', msg=f"Hello, {user_name}!", tech_list=[])

# Run the app in debug mode for development
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000, debug=True)
