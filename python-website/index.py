from flask import Flask, render_template

app = Flask(__name__)

# Routes to Render Something

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about')
def about():
    return render_template("about.html")

# Make sure this we are executing this file
if __name__ == '__main__':
    app.run(debug=True)