export async function logout() {
    try {
        const response = await fetch('http://localhost:8080/api/auth/jwt/logout', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            credentials: 'include'
        });
        window.location.href = '/';
    } catch (error) {
        console.error('Error:', error);
        alert('Произошла ошибка. Попробуйте еще раз.');
    }
}
