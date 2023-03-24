from flask import Flask
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

csrf = CSRFProtect(app)

@app.route("/")
def pagina_inicial():
    return '''
    <html>
        <head><title> App Fiap Fase 5</title></head>
        <body> Olá Mundo!</body>

    </html>
    '''

if __name__ == '__main__':
    app.run()