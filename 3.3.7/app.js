function ahoj() {
    console.log("Ahoj");
    console.log("Ahoj")
}

ahoj();

let greeting = "Nazdárek";

function showGreeting() {
    console.log(greeting);
}

showGreeting();

function funkceUvnitr() {
    let cislo = 123;
    console.log(cislo);
}

funkceUvnitr();

// Parametr a Argument

function test(name) {
    console.log("Ahoj " + name);
}

test("Tomáš");
test("Ema");
test(123)

function scitani(num1, num2) {
    console.log(num1 + num2)
    console.log(num1 - num2)
    console.log(num1 * num2)
    console.log(num1 / num2)
    
}


scitani(6,7)

// Napiš funkci printRange, která vypíše do
// konzole všechna čísla od parametru start až po end

// Postup:
// 1) Deklarace funkce
// 2) definování parametrů
// 3) for smyčka

function printRange(start, end) {

    for (let i = start; i <= end; i++) {
        console.log(i);
    }
}

// 4) Vyvolání funkce a argumentů

printRange(3,7)
