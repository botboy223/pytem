from flask import Flask, render_template

app = Flask(__name__)

# Define the index route
@app.route('/')
def index():
    return render_template('index.html')

# Start the Flask development server
if __name__ == '__main__':
    app.run(debug=True)
