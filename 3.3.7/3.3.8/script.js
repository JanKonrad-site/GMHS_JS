function dejMi3() {
    return 3;
}

console.log(dejMi3())

// funkce s logem
function nasobic(a,b) {
    console.log(a*b);
}

let r = nasobic(5,3)
console.log(r)

// Funkce s return

function nasobic2(a,b) {
    return a * b;
}

let r2 = nasobic2(5,3)
console.log(r2)

// return ukončí funkci

function konec() {
    console.log("A");
    return "Hotovo";
    console.log("B"); // toto neprojde
}

let konec2 = konec();
console.log(konec())

// cviceni

// 1) Vytvoř funkci jeSude()
// 2) Podmínka jestli je sude vypiš boolean True
// 3) Jestli je liché vypiš boolean false
// Návratová hodnota vrací výsledek

// jeSude(20) -> true
// jeSude(7) -> false

// Nápověda 
// % = vrací zbytek po dělení
// === porovnání čísel bez převodů JS past

function jeSude(cislo) {
    return cislo % 2 === 0;
}

console.log(jeSude(20));
console.log(jeSude(7));
