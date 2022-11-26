let reviews = {
    review_0 : {
             img: "placeholderPic.png",
            name: "Vincent Hoehne", 
        position: "web developer",
            more: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. Sed nisi. Nulla quis sem at nibh elementum imperdiet. Duis sagittis ipsum. Praesent mauris. Fusce nec tellus sed augue semper porta. Mauris massa. Vestibulum lacinia arcu eget nulla. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Curabitur sodales ligula in libero."
    },
    review_1 : {
             img: "placeholderPic.png",
            name: "Simon Jokanic", 
        position: "web3 developer",
            more: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. Sed nisi. Nulla quis sem at nibh elementum imperdiet. Duis sagittis ipsum. Praesent mauris. Fusce nec tellus sed augue semper porta. Mauris massa. Vestibulum lacinia arcu eget nulla. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Curabitur sodales ligula in libero."
    },
    review_2 : {
             img: "placeholderPic.png",
            name: "Manuel Neuer", 
        position: "profi fußballspieler",
            more: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. Sed nisi. Nulla quis sem at nibh elementum imperdiet. Duis sagittis ipsum. Praesent mauris. Fusce nec tellus sed augue semper porta. Mauris massa. Vestibulum lacinia arcu eget nulla. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Curabitur sodales ligula in libero."
    }
}

let arrObj = [reviews.review_0, reviews.review_1, reviews.review_2]
let current = 0;
let last = arrObj.length - 1;

let show = () => {
    document.getElementById("image").src = (arrObj[current].img);
    document.getElementById("name").innerHTML = (arrObj[current].name);
    document.getElementById("position").innerHTML = (arrObj[current].position);
    document.getElementById("more").innerHTML = (arrObj[current].more);
}

let left = () => {
    if (current === 0) {current = (last);} 
    else {current--;}
    console.log(current);
    show();
}

let right = () => {
    if (current === last) {current = 0;}
    else {current++;}
    console.log(current);
    show();
}
