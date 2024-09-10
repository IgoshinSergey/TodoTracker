import { fetchUserData } from "./scripts/user_data.js";
import { fetchTasks, createTask, fetchTaskStatistics } from "./scripts/tasks.js";
import { logout } from "./scripts/logout.js";


document.addEventListener('DOMContentLoaded', fetchUserData);
document.addEventListener('DOMContentLoaded', fetchTasks);
document.addEventListener('DOMContentLoaded', fetchTaskStatistics);
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
