document.getElementById('passwordForm').addEventListener('submit', function (event) {
    event.preventDefault();

    const length = parseInt(document.getElementById('length').value);

    if (isNaN(length) || length < 6 || length > 50) {
        alert('La longitud de la contraseña debe ser un número entre 6 y 50.');
        return;
    }

    const lowercase = document.getElementById('lowercase').checked;
    const uppercase = document.getElementById('uppercase').checked;
    const numbers = document.getElementById('numbers').checked;
    const specials = document.getElementById('specials').checked;

    if (!lowercase && !uppercase && !numbers && !specials) {
        alert('Debe seleccionar al menos un tipo de caracter.');
        return;
    }

    let characters = '';
    if (lowercase) characters += 'abcdefghijklmnopqrstuvwxyz';
    if (uppercase) characters += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    if (numbers) characters += '0123456789';
    if (specials) characters += '!@#$%^&*()-_=+[]{}|;:,.<>?';

    let password = '';
    for (let i = 0; i < length; i++) {
        const randomIndex = Math.floor(Math.random() * characters.length);
        password += characters[randomIndex];
    }

    document.getElementById('passwordResult').textContent = 'Contraseña generada: ' + password;
});
