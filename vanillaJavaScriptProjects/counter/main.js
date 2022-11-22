let counter = 0;
let results = [];

let declare = () => {
    document.getElementById("number").innerHTML = counter;
    document.getElementById("results").innerHTML = results;
}

let increase = () => {
    counter++;
    declare();
}

let decrease = () => {
    counter--;
    declare();
}

let reset = () => {
    results.push(counter);
    counter = 0;
    declare();
}