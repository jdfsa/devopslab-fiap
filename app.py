from flask import flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Hello World"

if __name__ == '__main__':
    app.run()