export async function fetchTasks() {
    try {
        const response = await fetch('/api/tasks', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
            },
        });
        if (!response.ok) {
            window.location.href = '/';
        }
        const tasks = await response.json();
        displayTasks(tasks);
    } catch (error) {
        console.error('Error fetching tasks:', error);
    }
}


export async function createTask(description) {
    try {
        const newTask = {
            description: description,
        };
        const response = await fetch('/api/tasks', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(newTask),
        });
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        await fetchTasks();
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
        console.log(updatedTask);
        const response = await fetch(`/api/tasks/${taskId}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(updatedTask),
        });
        if (!response.ok) {
            throw new Error(`Ошибка ${response.status}: ${JSON.stringify(errorDetails)}`);
        }

        // await fetchTasks();
    } catch (error) {
        console.error('Error updating task:', error);
    }
}

function displayTasks(tasks) {
    const tasksList = document.getElementById('tasks');
    tasksList.innerHTML = ''; // Clear existing tasks
    tasks.forEach(task => {
        const li = document.createElement('li');

        const checkbox = document.createElement('input');
        checkbox.type = 'checkbox';
        checkbox.checked = task.completed;
        checkbox.addEventListener('change', () => {
            updateTask(task.id, task.description, checkbox.checked);
        });

        const label = document.createElement('label');
        label.textContent = task.description;

        // Append checkbox and label to the list item
        li.appendChild(checkbox);
        li.appendChild(label);
        tasksList.appendChild(li);
    });
}
