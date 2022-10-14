// at first i need 25 random numbers 
const random = (max) => {
    return Math.floor(Math.random() * max);
}

const max_fields = 25; // amount of fields that are showed
const amount_values = 5; // how many different values can u cat
const row_length = 5; // length of one row
const amount_rows = 5; // amount of rows

const spin = () => {
    const spin_values = []; // an array with max_fields times a random number till amount_values
    for (let i = 0; i < amount_rows; i++) {
        const spin_values_row = [];
        for (let j = 0; j < row_length; j++) {
            spin_values_row.push(random(amount_values));
        }
        spin_values.push(spin_values_row);
    }
    console.log(spin_values);
}
