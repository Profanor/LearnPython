from flask import Flask, render_template

# Initialize Flask instance
app = Flask(__name__)

# Define a route and its handler function
@app.route('/')
def home():
    return render_template('index.html')

# Run the application if this script is executed directly
if __name__ == '__main__':
    app.run(debug=True)
