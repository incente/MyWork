const tasks = [];

function create() {
    let newTask = document.getElementById("newTask").value;
    tasks.push(newTask);
    document.getElementById("tasks").innerHTML = tasks;
}

function erase() {
    let taskErase = (parseInt(document.getElementById("erase").value) - 1);
    tasks.splice(taskErase, 1);
    document.getElementById("tasks").innerHTML = tasks;
}
