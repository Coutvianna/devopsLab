from flask import Flask
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

csrf = CSRFProtect(app)

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()