import { register } from './scripts/register.js';
import { login } from './scripts/login.js';

function validateUsername(username) {
    if (username.length < 3 || username.length > 20) {
        return {valid: false, message: "Никнейм должен содержать от 3 до 20 символов."};
    }

    const regex = /^[a-zA-Z0-9_]+$/;
    if (!regex.test(username)) {
        return {valid: false, message: "Никнейм может содержать только буквы, цифры и подчеркивания."};
    }
    return { valid: true, message: "" };
}
document.getElementById('registerForm').addEventListener('submit', async function(event) {
    event.preventDefault();

    const email = document.getElementById('registerEmail').value;
    const password = document.getElementById('registerPassword').value;
    const username = document.getElementById('registerUsername').value;

    const validationResult = validateUsername(username);
    if (!validationResult.valid) {
        alert("Ошибка: " + validationResult.message);
        return;
    }

    const { status, response } = await register(email, password, username);
    if (status === 201) {
        alert('Регистрация успешна!');
        await login(email, password);
        window.location.href = '/tracker/';
    } else if (status === 422) {
        alert('Некорректный email');
    } else {
        alert('Неверные данные');
    }
});

document.getElementById('loginForm').addEventListener('submit', async function(event) {
    event.preventDefault(); // Предотвращаем перезагрузку страницы

    const email = document.getElementById('loginEmail').value;
    const password = document.getElementById('loginPassword').value;

    const status = await login(email, password);
    if (status === 204) {
        alert('Авторизация прошла успешно!');
        window.location.href = '/tracker/';
    } else {
        alert('Неверные данные.');
    }
});
