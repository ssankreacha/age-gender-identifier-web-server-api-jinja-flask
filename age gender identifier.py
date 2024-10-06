from flask import Flask, render_template
from datetime import datetime
import requests

# TODO: Use Genderize & Agify API To Extract Age & Gender For Given Name, and Place Into Website Using Jinja.

# Current Year
current_year = datetime.today().year

# Constants
NAME = "Jason"
AGE_URL = f"https://api.agify.io?name={NAME}"
GENDER_URL = f"https://api.genderize.io?name={NAME}"

# Get code data from APIs
age_response = requests.get(url=AGE_URL)
gender_response = requests.get(url=GENDER_URL)

# Convert to JSON
age_info = age_response.json()
gender_info = gender_response.json()

# Extract age and gender from the JSON
age = age_info.get("age")
gender = gender_info.get("gender")

# print(f"Age: {age}, Gender: {gender}")

# Initialise Flask Web Server
# Homepage
app = Flask(__name__)
@app.route('/')
def home():
    # Send information into identifier.html
    return render_template("identifier.html", year=current_year, name=NAME,
                           age=age, gender=gender)     # Contains many arguments **

# Run Web Server
if __name__ == '__main__':
    app.run(debug=True)
