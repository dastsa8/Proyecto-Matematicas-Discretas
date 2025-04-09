document.getElementById('sendBtn').addEventListener('click', sendMessage);
document.getElementById('userInput').addEventListener('keypress', function (e) {
    if (e.key === 'Enter') sendMessage();
});

function addMessage(sender, text) {
    const messages = document.getElementById('messages');
    const msgDiv = document.createElement('div');
    msgDiv.classList.add('mb-2');
    msgDiv.innerHTML = <strong>${sender}:</strong>; {text};
    messages.appendChild(msgDiv);
    messages.scrollTop = messages.scrollHeight;
}

async function sendMessage() {
    const input = document.getElementById('userInput');
    const text = input.value.trim();
    if (!text) return;

    addMessage('Tú', text);
    input.value = '';

    try {
        const response = await fetch('https://TU-REPLIT-URL/chat', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ message: text })
        });

        const data = await response.json();
        addMessage('ChatBot', data.reply);
    } catch (error) {
        addMessage('ChatBot', 'Error al conectar con el servidor.');
    }
}