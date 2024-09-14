export async function fetchTasks() {
    try {
        const response = await fetch('http://localhost:8080/api/tasks', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
            },
            credentials: 'include'
        });
        if (!response.ok) {
            window.location.href = '/';
        }
        const tasks = await response.json();
        renderTasks(tasks);
    } catch (error) {
        console.error('Error fetching tasks:', error);
    }
}

export async function fetchTaskStatistics() {
    try {
        const response = await fetch('http://localhost:8080/api/tasks/statistics', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
            },
            credentials: 'include'
        });
        if (response.ok) {
            const data = await response.json();
            renderTaskStatistics(data);
        }
    } catch (error) {
        console.error('Error fetching task statistics:', error);
    }
}


export async function createTask(description) {
    try {
        const newTask = {
            description: description,
        };
        const response = await fetch('http://localhost:8080/api/tasks', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(newTask),
            credentials: 'include',
        });
        if (!response.ok) {
            window.location.href = '/';
        }
        await fetchTasks();
        await fetchTaskStatistics();
    } catch (error) {
        console.error('Error creating task:', error);
    }
}

async function updateTask(taskId, description, completed) {
    try {
        const updatedTask = {
            description: description,
            completed: completed
        };
        const response = await fetch(`http://localhost:8080/api/tasks/${taskId}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(updatedTask),
            credentials: 'include'
        });
        await fetchTaskStatistics();
    } catch (error) {
        console.error('Error updating task:', error);
    }
}

async function renderTasks(tasks) {
    const tasksList = document.getElementById('tasks');
    tasksList.innerHTML = '';
    tasks.forEach(task => {
        const li = document.createElement('li');
        li.style.display = 'flex';
        li.style.justifyContent = 'space-between';
        li.style.alignItems = 'center';

        const checkbox = document.createElement('input');
        checkbox.type = 'checkbox';
        checkbox.checked = task.completed;
        checkbox.addEventListener('change', () => {
            updateTask(task.id, task.description, checkbox.checked);
            li.remove();
        });

        const input = document.createElement('input');
        input.type = 'text';
        input.value = task.description;
        input.style.flexGrow = 1;

        input.addEventListener('blur', () => {
            const newDescription = input.value;
            updateTask(task.id, newDescription, checkbox.checked);
        });

        li.appendChild(input);
        li.appendChild(checkbox);

        tasksList.appendChild(li);
    });
}

function renderTaskStatistics(statistics) {
    const totalTasksElement = document.getElementById('total-tasks');
    const completedTasksElement = document.getElementById('completed-tasks');
    totalTasksElement.textContent = statistics.total_tasks;
    completedTasksElement.textContent = statistics.completed_tasks;
}
