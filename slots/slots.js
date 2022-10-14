let bet = 1;
let currentbet = bet;
let currentmode = 1;
let wallet = 3000;

const currentvalue = () => {
    bet = document.getElementById("bet-input").value;
    currentbet = currentmode * bet;
    document.getElementById("current-bet").innerHTML = 
        currentbet + " USD";
}

const changemode = () => {
    if (currentmode == 5)   {
        currentmode -= 4;
    } else {
        currentmode++
    }
    document.getElementById("current-mode").innerHTML =
        currentmode;
    document.getElementById("multi").innerHTML = 
        currentmode + "x";
    currentbet = currentmode * bet;
    document.getElementById("current-bet").innerHTML = 
        currentbet + " USD";
}

const spin = () => {
    if ((wallet - currentbet) < 0)    {
        prompt("Maximum bet for this spin: " + wallet)
    } else {
    wallet -= currentbet;
    document.getElementById("wallet").innerHTML =
        wallet + " USD";
    }
}


