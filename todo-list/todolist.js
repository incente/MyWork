const tasks = {};

let amount = 0;

const add = () => {
    let task = document.getElementById("task").value;
    tasks[amount] = task;
    document.getElementById("output").innerHTML += tasks[amount] + "<br>";
    amount++;
}

const remove = () => {
    let remove = document.getElementById("delete").value;
    delete tasks[remove];
    amount--;
}
