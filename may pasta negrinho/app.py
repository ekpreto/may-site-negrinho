  #importando a biblioteca do flask para fazer um site dinâmico
from flask import Flask, render_template, request 

app = Flask(__name__)

  # definindo a rota principal do site
@app.route('/')
def home():
    return render_template('index.html')

    # parte principal do programa em python
if __name__ == '__main__':
    app.run(debug=True)
