export async function logout() {
    try {
        const response = await fetch('/api/auth/jwt/logout', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
        });
        window.location.href = '/';
    } catch (error) {
        console.error('Error:', error);
        alert('Произошла ошибка. Попробуйте еще раз.');
    }
}
