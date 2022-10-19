import * as winningconditionsJs from './winningconditions.js'; // imports a object with all winningconditions 

// at first i need 25 random numbers 
const random = (max) => {
    return Math.floor(Math.random() * max);
}
// this function compares two arrays
const compare = (a, b) => {
    return JSON.stringify(a) === JSON.stringify(b);
}

const amount_values = 2; // how many different values can u cat
const row_length = 5; // length of one row
const amount_rows = 3; // amount of rows

const spin = (a, b, c) => {
    const spin_values = []; // an array with max_fields times a random number till amount_values
    for (let i = 0; i < c; i++) { // this loop gives an array with amount_rows times array positions
        const spin_values_row = [];
        for (let j = 0; j < b; j++) { // this loop gives every position row_length times array positions
            spin_values_row.push(random(a));
        }
        spin_values.push(spin_values_row);
    }

    console.log(spin_values); // console.log the three arrays with 5 numbers each

    for (let i = 0; i < c; i++)  {
        for (let j = 0; j < full_row.length; j++) {
            console.log(compare(spin_values[i], winningconditionsJs.full_row[j])); // compares a row in the array with a winning row in the object
        }
    }
}

const push = () => {
    spin(amount_values, row_length, amount_rows); // if pressed starts spin() with these values
}