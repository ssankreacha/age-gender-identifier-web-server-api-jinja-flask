from flask import Flask, render_template
import random
from datetime import date

app = Flask(__name__)
today_date = date.today()
current_year = today_date.year
# print(current_year)

@app.route('/')
def home():
    # Send current_year into index.html
    return render_template("index.html", year=current_year)     # Contains many arguments **

if __name__ == '__main__':
    app.run(debug=True)
