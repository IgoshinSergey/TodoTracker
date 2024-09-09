import { fetchUserData } from "./scripts/user_data.js";
import { fetchTasks, createTask } from "./scripts/tasks.js";
import { logout } from "./scripts/logout.js";


document.addEventListener('DOMContentLoaded', fetchUserData);
document.addEventListener('DOMContentLoaded', fetchTasks);
document.addEventListener('DOMContentLoaded', () => {
    const logoutButton = document.getElementById("logout-button");
    logoutButton.addEventListener("click", logout);
});

document.addEventListener('DOMContentLoaded', () => {
    const createButton = document.getElementById("create-task-button");
    createButton.addEventListener("click", () => {
        const description = document.getElementById("task-description").value;

        if (!description) {
            alert("Пожалуйста, введите описание задачи.");
            return;
        }

        createTask(description);
        document.getElementById("task-description").value = '';
    });
});

// document.addEventListener("DOMContentLoaded", () => {
//     const usernameElement = document.getElementById("username");
//     const taskListElement = document.getElementById("tasks");
//     const createTaskButton = document.getElementById("create-task-button");
//     const logoutButton = document.getElementById("logout-button");
//
//     // Mock user data
//     const user = { id: 12, name: "John Doe" };
//     usernameElement.textContent = user.name;
//
//     // Fetch user data from the server
//
//     // Fetch tasks from the server
//     async function fetchTasks() {
//         const response = await fetch(`/tasks?user_id=${user.id}`);
//         const tasks = await response.json();
//         renderTasks(tasks);
//     }
//
//     // Render tasks
//     function renderTasks(tasks) {
//         taskListElement.innerHTML = "";
//         tasks.forEach(task => {
//             const li = document.createElement("li");
//             li.innerHTML = `
//                 <span>${task.description} - ${task.completed ? "Completed" : "Pending"}</span>
//                 <button onclick="updateTask(${task.id})">Edit</button>
//             `;
//             taskListElement.appendChild(li);
//         });
//     }
//
//     // Create a new task
//     createTaskButton.addEventListener("click", async () => {
//         const description = document.getElementById("task-description").value;
//         const response = await fetch("/tasks", {
//             method: "POST",
//             headers: {
//                 "Content-Type": "application/json"
//             },
//             body: JSON.stringify({ description, user_id: user.id })
//         });
//         if (response.ok) {
//             document.getElementById("task-description").value = "";
//             fetchTasks();
//         }
//     });
//
//     // Update a task
//     window.updateTask = async (taskId) => {
//         const newDescription = prompt("Enter new description:");
//         const completed = confirm("Is this task completed?");
//         const response = await fetch(`/tasks/${taskId}`, {
//             method: "PUT",
//             headers: {
//                 "Content-Type": "application/json"
//             },
//             body: JSON.stringify({ description: newDescription, completed, user_id: user.id })
//         });
//         if (response.ok) {
//             fetchTasks();
//         }
//     };
//
//     // Logout
//     logoutButton.addEventListener("click", () => {
//         window.location.href = "/";
//     });
//
//     // Initial fetch of tasks
//     fetchTasks();
// });
