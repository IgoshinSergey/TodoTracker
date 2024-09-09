export async function logout() {
    const response = await fetch('http://localhost:8888/api/auth/jwt/logout', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
    });
    return response.status;
}
