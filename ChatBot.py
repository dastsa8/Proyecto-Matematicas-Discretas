import flask 
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    mensaje_usuario = data['mensaje']

    # Aquí va tu "lógica" de respuesta
    respuesta = f"Recibí tu mensaje: {mensaje_usuario}"

    return jsonify({'respuesta': respuesta})

if __name__ == '__main__':
    app.run(debug=True)
