// Vnořené podmínky
let isLoggedIn = true;
let isAdmin = false;

if (isLoggedIn) {
    console.log("Vítej na stránce!")
    if (isAdmin) {
        console.log("Přistup do panelu admin povolen")
    } else {
        console.log("Přístup jako uživatel povolen!")
    }
}

// Operátory

let age = 20;
let hasDriverLicense = true;

if (age >= 18 && hasDriverLicense) {
    console.log("Můžeš řídit!");    
} else {
    console.log("Řídit nemůžeš")
}

let isHoliday = false;
let isWeekend = true;

if (isHoliday || isWeekend) {
    console.log("Je čas relaxovat!")
} else {
    console.log("Musíme pracovat.")
}


