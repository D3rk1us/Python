from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():

    # Busca index.html dentro del directorio /templates
    return render_template('index.html', message='Hello Flask!')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
