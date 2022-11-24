exercice 1

let x=93;
let y=55;
if (x<y) 
console.log("x est inferieur a y");


else
console.log("x est supperieur a y");



exercice 2

let newDog="Chihuahua";
//taille de newdog
console.log(newDog.length);
//majuscule
console.log(newDog.toUpperCase());
//miniscule
console.log(newDog.toLowerCase());
//conditionage
if (newDog==="Chihuahua")
console.log("J'adore les chihuahuas, c'est ma race de chien préférée");
else
console.log("Je m'en fous, je préfère les chats");



exercice 3

 let x = prompt("entrer une valeur");

 let y = prompt("entrer une valeur");

if (x%y==0)
console.log("x est un nombre pair");
else
console.log(" x est un nombre impair");


exercice 4

let users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"];

if (users.lenght==0)
console.log(" personne n'est en ligne");

else if (users.lenght==1){

console.log("name_user est en ligne");
}

else if (users.lenght==2){

console.log("name_user1 et name_user2 est en ligne ");
}

else if (users.lenght>2){

let un =users[0];
let deux =users[1];
console.log(users.lenght);
console.log(un,deux, " est en ligne ");
}
