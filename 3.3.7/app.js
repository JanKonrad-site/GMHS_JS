function rekniAhoj() {
    console.log("Čus");

}

rekniAhoj();
rekniAhoj();

let pozdrav = "Pozdrav!";

function ukazPozdrav() {
    console.log(pozdrav)
}

function testLocal() {
    let localValue = 123;
    console.log(localValue)
}

ukazPozdrav();
testLocal();




if (true) {
  var y = "var blok nerespektuje";
}
console.log(y);

// Parametr & Argument

function sayHello(name) { // name = parametr
    console.log("Ahoj " + name);
}

sayHello("Alice")

function addNumber(num1, num2) {
    console.log(num1 + num2);
}

addNumber(5,8);
