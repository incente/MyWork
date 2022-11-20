let hexArr = ["a", "b", "c", "d", "e", "f", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9];

let len = (hexArr.length - 1);

let random = () => {
    return Math.floor(Math.random()*((len - 1) - 0 + 1)) + 0;
};

let hexCode = () => {
    let code = ["#"];
    for (let i = 0; i < 6; i++) {
        code.push(hexArr[random()]);
    };
    let codeString = code.join("");
    console.log(codeString);
    document.getElementById("body-color").style.backgroundColor = codeString;
    document.getElementById("hex").innerHTML = codeString;
};


