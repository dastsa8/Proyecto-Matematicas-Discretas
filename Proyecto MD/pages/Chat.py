from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# Lista de preguntas que el chatbot puede hacer
preguntas = [
    "¿Cómo te has sentido últimamente con respecto a tu rendimiento académico?",
    "¿Qué haces cuando te sientes abrumado por tus responsabilidades?",
    "¿Sientes que tienes un buen equilibrio entre tu vida social y tus estudios?",
    "¿Tienes alguien con quien hablar cuando te sientes estresado o ansioso?",
    "¿Cuál ha sido tu mayor fuente de motivación durante este semestre?",
    "¿Cómo manejas el miedo al fracaso?",
    "¿Qué actividades haces para cuidar tu salud mental?",
    "¿Te sientes apoyado por tus amigos o familia?",
    "¿Has considerado hablar con un profesional sobre tus emociones o estrés?",
    "¿Qué significa para ti tener éxito como estudiante?"
]

respuestas_iniciales = [
    "¡Hola! Estoy aquí para escucharte.",
    "Gracias por confiar en mí. ¿Puedo hacerte una pregunta para reflexionar?",
    "Estoy listo para charlar. ¿Quieres comenzar con una pregunta?"
]

despedidas = [
    "Gracias por compartir. Recuerda que tu salud mental es importante.",
    "Estoy aquí cuando me necesites. No olvides buscar ayuda profesional si lo necesitas.",
    "Fue un gusto escucharte. Cuídate mucho."
]

# Memoria sencilla para la sesión
estado_usuario = {}

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_msg = data.get('message', '').lower()

    if user_msg in ['hola', 'hey', 'buenas', 'qué tal']:
        return jsonify(reply=random.choice(respuestas_iniciales))
    elif any(x in user_msg for x in ['gracias', 'adiós', 'bye']):
        return jsonify(reply=random.choice(despedidas))
    else:
        
        pregunta = random.choice(preguntas)
        return jsonify(reply=pregunta)

if __name__ == '_main_':
    app.run(debug=True)