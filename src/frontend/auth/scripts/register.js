export async function register(email, password, username) {
    const userData = {
        email: email,
        password: password,
        username: username,
    };

    const response = await fetch('http://localhost:8888/api/auth/register', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(userData),
    });

    return {
        status: response.status,
        data: await response.json(),
    };
}

