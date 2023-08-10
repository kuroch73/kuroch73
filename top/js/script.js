// console.log("Hello !")
// let one = 1
// let str = "1"
// let bool = true || false
// let massiv = [1,2,3,4,5]
// let obj = {
//     "name" : "name",
//     "age" : 22
// }
// class Auto {
//     constructor(nmae,age) {
//         this.name = nmae;
//         this.age = age;
//     }
// }
 
// class AutoV2 extends Auto {
//     constructor(name,age){
//         this.name = name;
//         this.age = age
//     } 
// }
// function sum(a,b) {
//     return a + b
// }
// let sum2 = (a,b) => {
//     return a + b
// }
// console.log(sum(2,3))
// const pi = 3.14
// //console.log(one)
// //let x = prompt(" Введите ваше имя") // строка
// //let y = +prompt(" Введите число") // число
// //console.log(x,y)

// let i = 0 
// while (i <10) {
//     i ++;
//     console.log(i)
// }
// for (let i = 0; i <10; i ++) {
//     console.log(i)
// }

// let z = 2;
// let k = 2;
// if (z < k) {
//     console.log("z < k")
// }
// else if (k < z ) {
//     console.log("k < z")
// }
// else if (k = z) {
//     console.log("k = z")
// }
// else {
//     console.log("ошибка")
// }
// let x = +prompt(" 1 -число  ")
// let y = +prompt(" 2-число")
// let z = +prompt("3-число")

// console.log("ср арифм" , (x + y + z)/3)
 
// let x = +prompt("введите возраст ")
// if (x > 0 , x < 11) {
//     console.log("Ребенок")
// }
// else if (x > 11, x < 18) {
//     console.log(" подросток")
// }
// else {
//     console.log("взрослый")
// }

// let x = +prompt(" 1 -число  ")
// let y = +prompt(" 2-число")
// let z = +prompt("3-число")
// console.log(Math.max(x,y,z))

let plus = document.querySelector("#plus");
let minus = document.querySelector("#minus");
let out = document.getElementById("out")
console.log(plus)
console.log(minus)
console.log(out)

// let head = document.querySelector('head')
// console.log(head)

let h1 = document.querySelector("h1")
h1.innerHTML = "УРОК4"

let title = document.querySelector("title")
title.innerHTML = "урок" + 5

let i = 0;
function plusOut(){
    i++;
    out.innerHTML = i;

}
function minusOut(){
    i--;
    out.innerHTML = i;

}
plusOut()
plusOut()
minusOut()

// out.innerHTML = 123;
plus.addEventListener("click", plusOut)
minus.addEventListener("click", minusOut)

let number1 = document.querySelector("#number1");
let number2 = document.querySelector("#number2");

let calcPlus = document.querySelector("#calcPlus");
let calcMinus = document.querySelector("#calcMinus");
let calcMul = document.querySelector("#calcMul");
let calcDiv = document.querySelector("#calcDiv");

let otvet = document.querySelector("#otvet");

function fPlus() {
    
    otvet.innerHTML = Number(number1.value) + Number(number2.value)
}

function mMul() {
    // number1 = number(number1)
    // number2 = number(number2)
    otvet.innerHTML = number1.value * number2.value
}
function dDiv() {
    // number1 = number(number1)
    // number2 = number(number2)
    otvet.innerHTML = number1.value / number2.value
}
function sMin() {
    // number1 = number(number1)
    // number2 = number(number2)
    otvet.innerHTML = number1.value - number2.value
}

calcPlus.addEventListener("click", fPlus)
calcMul.addEventListener("click", mMul)
calcDiv.addEventListener("click", dDiv)
calcMinus.addEventListener("click", sMin)

let body = document.body;
// body.style.backgroundColor = "red"
