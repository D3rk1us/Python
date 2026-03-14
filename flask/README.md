# Configuración básica

## Instalación:

```bash

sudo apt update

sudo apt install python3-pip python3-venv


```

### Crear entorno virtual:

```bash

python3 -m venv mi_entorno

# Activar entorno
source mi_entorno/bin/activate

```

### Instalar Flask:

```bash

pip install Flask

```

## Aplicación básica ("Hola Mundo"):

```bash

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "¡Hola Mundo!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

```
 
