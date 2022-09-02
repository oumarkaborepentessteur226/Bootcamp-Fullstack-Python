exercie 1

//nourrirture preferer
let fFood= "harikot";
//repas preferer
let fMeal= "déjeuner";


console.log("I eat " + fFood + " at every " + fMeal);


exercice 2


let myWatchedSeries = ["black mirror", "money heist", "the big bang theory"];

myWatchedSeriesLength=myWatchedSeries.length;

myWatchedSeriesSentence="black mirror, money heist, and the big bang theory";

console.log("I watched ",myWatchedSeriesLength, " serie : ",myWatchedSeriesSentence);

//remplacer
myWatchedSeries.splice(2,1,"friends");
console.log(myWatchedSeries);

//add fin
myWatchedSeries.push("naruto");
console.log(myWatchedSeries);

//add debut tableau

myWatchedSeries.unshift("dragon ball z");
console.log(myWatchedSeries);

//delete black mirror
myWatchedSeries.shift("black mirror");
console.log(myWatchedSeries);

//3eme lettre:.substring(1,1)
let trois=myWatchedSeriesSentence[1];

console.log(trois);


exercice 3

//variable en celcus
let cel=37;
let fal=(37/5)*3+32;
console.log(fal)



exercice 4

    let c;
    let a = 34;
    let b = 21;

    console.log(a+b) //first expression
    // Prediction:55 parceque  34+21 donne 55
    // Actual:55


 	a = 2;

    console.log(a+b) //second expression
    // Prediction:23 car la premiere variable a a ete ecraser par une nouvel variable a 
    // Actual:23

3.) c na pa de valeur

4.) console.log(3 + 4 + '5'); donne 75 car a et b s addition parce qu il sont des 
entier et ce concatene a 5 qui es une chaine de caractere



exercice 5

typeof(15)
// Prediction:entier
// Actual:number


typeof(5.5)
// Prediction:nombre a virgule
// Actual:number


typeof(NaN)
// Prediction:null
// Actual:number


typeof("hello")
// Prediction:chaine de caractere
// Actual:string

typeof(true)
// Prediction:booleen
// Actual:boolen

typeof(1 != 2)
// Prediction: vrai
// Actual:true

"hamburger" + "s"
// Prediction:hamburgers
// Actual:hamburgers


"hamburgers" - "s"
// Prediction:impossible
// Actual:nan

"1" + "3"
// Prediction:13
// Actual:13

"1" - "3"
// Prediction:-2
// Actual:-2
"johnny" + 5
// Prediction:johnny5
// Actual:johnny5

"johnny" - 5
// Prediction:impossible
// Actual:nan

99 * "hello"
// Prediction:impossible
// Actual:nan

1 != 1
// Prediction:faux
// Actual:false

1 == "1"
// Prediction:vrai
// Actual:true

1 === "1"
// Prediction:faux
// Actual:false


exercie 6



5 + "34"
// Prediction:534 concatenation number et sting
// Actual:534

5 - "4"
// Prediction:1
// Actual:1



10 % 5
// Prediction:0
// Actual:0

5 % 10
// Prediction:5
// Actual:5

"Java" + "Script"
// Prediction:javaScript
// Actual:javaScript

" " + " "
// Prediction:'  '
// Actual:'  '


" " + 0
// Prediction:' 0'
// Actual:' 0'


true + true
// Prediction:1+1=2
// Actual:2

true + false
// Prediction:1+0=1
// Actual:1


false + true
// Prediction:0+1=1
// Actual:1


false - true
// Prediction:0-1=-1
// Actual:-1

!true
// Prediction:faux
// Actual:false


3 - 4
// Prediction:-1
// Actual:-1


"Bob" - "bill"
// Prediction:nuull
// Actual:nan