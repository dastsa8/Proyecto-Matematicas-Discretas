document.getElementById("sendBtn").addEventListener("click", async () => {
    const input = document.getElementById("userInput");
    const message = input.value.trim();
    const chatbox = document.getElementById("messages");

    if (message === "") return;

    // Mostrar mensaje del usuario
    chatbox.innerHTML += `<div><strong>Tú:</strong> ${message}</div>`;

    // Enviar a Flask
    const response = await fetch('/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ mensaje: message })
    });

    const data = await response.json();

    // Mostrar respuesta del bot
    chatbox.innerHTML += `<div><strong>Bot:</strong> ${data.respuesta}</div>`;
    input.value = '';
    chatbox.scrollTop = chatbox.scrollHeight;
});
