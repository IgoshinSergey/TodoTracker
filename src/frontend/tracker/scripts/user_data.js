export async function fetchUserData() {
    const response = await fetch(`http://localhost:8080/api/user`, {
        method: 'GET',
        credentials: 'include'
    });
    if (response.ok) {
        const userData = await response.json();
        renderUserData(userData);
        return userData.username;
    } else {
        alert("Failed to fetch user data");
        // window.location.href = '/';
    }
}

function renderUserData(userData) {
    const usernameElement = document.getElementById('username');
    const emailElement = document.getElementById('email');

    usernameElement.textContent = userData.username;
    emailElement.textContent = userData.email;
}
