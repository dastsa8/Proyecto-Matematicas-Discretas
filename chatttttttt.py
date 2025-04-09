import random

def saludar():
    print("¡Hola! Soy tu chatbot de psicología. Estoy aquí para hacerte algunas preguntas que te ayudarán a reflexionar sobre tu vida universitaria.")

def hacer_preguntas():
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

    random.shuffle(preguntas)

    for i, pregunta in enumerate(preguntas[:5], 1):  # hace 5 preguntas aleatorias
        input(f"\nPregunta {i}: {pregunta}\nTu respuesta: ")

def despedirse():
    print("\nGracias por compartir. Recuerda que cuidar tu salud mental es igual de importante que tus estudios.")
    print("Si alguna vez necesitas hablar con alguien, no dudes en buscar apoyo profesional.")

def main():
    saludar()
    hacer_preguntas()
    despedirse()

if __name__ == "__main__":  
    main()
