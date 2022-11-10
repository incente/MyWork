let form = document.getElementById('form');
let textInput = document.getElementById('textInput');
let dateInput = document.getElementById('dateInput');
let textarea = document.getElementById('textarea');
let msg = document.getElementById('msg');

form.addEventListener('submit', (e) =>  {
    e.preventDefault();
    formValidaiton();
});

let formValidaiton = () => {
    if (textInput.value === ''){
        console.log('faliure');
        msg.innerHTML = "Task cannot be blank"
    } else {
        console.log('success');
        msg.innerHTML = "";
        acceptdata();
    }
};

let data = {};

let acceptdata = () => {
    data['text'] = textInput.value;
    data['date'] = dateInput.value;
    data['description'] = textarea.value;

    console.log(data);
};