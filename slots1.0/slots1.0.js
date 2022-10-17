// at first i need 25 random numbers 
const random = (max) => {
    return Math.floor(Math.random() * max);
}
// this function compares two arrays
const compare = (a, b) => {
    return JSON.stringify(a) === JSON.stringify(b);
}

const amount_values = 10; // how many different values can u cat
const row_length = 5; // length of one row
const amount_rows = 3; // amount of rows

const winningconditions = {
    full_row: { 
        one: [1, 1, 1, 1, 1], two: [2, 2, 2, 2, 2], three: [3, 3, 3, 3, 3], four: [4, 4, 4, 4, 4], five: [5, 5, 5, 5, 5], 
        six: [6, 6, 6, 6, 6], seven: [7, 7, 7, 7, 7], eight: [8, 8, 8, 8, 8], nine: [9, 9, 9, 9, 9], ten: [0, 0, 0, 0, 0]
    },
    four_row: {

    }
}

const spin = () => {
    const spin_values = []; // an array with max_fields times a random number till amount_values
    for (let i = 0; i < amount_rows; i++) { // this loop gives an array with amount_rows times array positions
        const spin_values_row = [];
        for (let j = 0; j < row_length; j++) { // this loop gives every position row_length times array positions
            spin_values_row.push(random(amount_values));
        }
        spin_values.push(spin_values_row);
    }

    console.log(spin_values); // console.log the three arrays with 5 numbers each

    for (let i = 0; i < amount_rows; i++)  { 
        for (let property in winningconditions.full_row) {
            console.log(compare(spin_values[i], property)); // compares a row in the array with a winning row in the object (atm just winning with a row full of zeros)
        }
     
    }
}
