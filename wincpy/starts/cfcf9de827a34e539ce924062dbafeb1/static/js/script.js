let accessKey = "";

const todoContainer = document.getElementById("todos-section");

// Add event listeners
document.getElementById("add-button").addEventListener('click', function() {
    event.preventDefault();
    addTodo();
});

document.getElementById("login-form").addEventListener('submit', function() {
    event.preventDefault();
    requestLogin();
});

function handleErrors(response) {
    console.log(response);
    if (!response.ok) {
        throw Error(response.statusText);
    }
    return response;
}

function formToJson(formData) {
    const formJson = {};
    formData.forEach(formInput => {
        formJson[formInput['name']] = formInput['value'];
    });
    return formJson;
}

function loadTodos() {
    fetch('/api/todos', {
        method: 'GET',
        headers: {
            'Authorization': accessKey
        }
    })
    .then(handleErrors)
    .then(response => response.json())
    .then(function(jsonResponse) {
        console.log(jsonResponse);
        jsonResponse['todos'].map(todo => addTodoToDom(todo));
    })
    .catch(function(error) {
        console.log(error);
        alert(error);
    });
}

function requestLogin() {
    const formData = $("#login-form").serializeArray();

    let json = formToJson(formData);

    fetch('/api/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(json)
    })
    .then(handleErrors)
    .then(response => response.json())
    .then(function(jsonResponse) {
        accessKey = jsonResponse.access_key;
        loadTodos();
        document.getElementById("login-box").style.display = "none";
    })
    .catch(function(error) {
        console.log(error);
        alert(error);
    });
}

function completeTodo(todo_id) {
    fetch(`/api/todos/${todo_id}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': accessKey
        },
        body: JSON.stringify({
            todo: {
                "completed": true
            }
        })
    })
    .then(handleErrors)
    .then(response => response.json())
    .then(function(jsonResponse) {
        console.log(jsonResponse);
        let completeButton = document.getElementById(`complete-${todo_id.toString()}`);

        completeButton.style.backgroundColor = "lightblue";
        completeButton.style.cursor = "not-allowed";
    })
    .catch(function(error) {
        console.log(error);
        alert(error);
    });
}

function deleteTodo(todo_id) {
    fetch(`/api/todos/${todo_id}`, {
        method: 'DELETE',
        headers: {
            'Authorization': accessKey
        }
    })
    .then(handleErrors)
    .then(document.getElementById(todo_id).remove())
    .catch(function(error) {
        console.log(error);
        alert(error);
    });
}

function addTodoToDom(todo) {
    let todoDiv = document.createElement("div");
    todoDiv.setAttribute("id", todo.id.toString());
    todoDiv.setAttribute("class", "todo-card");

    let completedStyle = todo['completed'] ? "background-color:lightblue;cursor:not-allowed;" : "";
    console.log("STYLE");
    console.log(completedStyle)
    todoDiv.innerHTML = `<h4 class="todo-heading">${todo.title}</h4><p class="paragraph">${todo.description}</p><div class="todo-footer-container"><div class="dates-container"><div>${todo['start-date']}</div><div>${todo['due-date']}</div></div><a href="#" id="complete-${todo.id.toString()}" class="complete-button w-button" style=${completedStyle}>Complete</a><a href="#" id=delete-${todo.id.toString()} class="delete-button w-button">delete</a></div>`;

    todoContainer.appendChild(todoDiv);

    // Add complete & delete event listeners

    document.getElementById(`delete-${todo.id.toString()}`).addEventListener('click', function() {
        deleteTodo(todo.id);
    })
    document.getElementById(`complete-${todo.id.toString()}`).addEventListener('click', function() {
        completeTodo(todo.id);
    })
}

function addTodo() {
    const formData = $("#todo-form").serializeArray();

    let todoJson = formToJson(formData);

    fetch('/api/todos', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': accessKey
        },
        body: JSON.stringify({
            'todo': todoJson
        })
    })
    .then(handleErrors)
    .then(response => response.json())
    .then(function(jsonResponse) {
        console.log(jsonResponse);
        addTodoToDom(jsonResponse);
    })
    .catch(function(error) {
        console.log(error);
        alert(error);
    });
}
