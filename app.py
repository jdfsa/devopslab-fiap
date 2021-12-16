from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "ambiente de teste rodando no heroku"

if __name__ == '__main__':
    app.run()