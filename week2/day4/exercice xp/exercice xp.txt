//Exercice 1 : Informations
	//Partie I : fonction sans paramètre
	//1//2
	function infoAboutMe(){
		console.log("Je me nomme Steve SANKARA, j'ai 22 ans et mis à part la programmation j'aime bien faire le sport tel que le basket");
	}

	//3
	infoAboutMe();

	//Partie II : fonction à trois paramètres
	//1
	function infoAboutPerson(personName, personAge, personFavoriteColor) {
		console.log("Je m'appelle",personName,"j'ai",personAge," ans ma couleur préférée est",personFavoriteColor);
	}
	infoAboutPerson("David", 45, "blue")
	infoAboutPerson("Josh", 12, "yellow")

//Exercice 2 : Conseils
	//1//2//3
	function calculateTip() {
		let montant = Number(prompt("Quel est le montant de la facture"))
		let pourb;
		if (montant < 50) {
			console.log("ffff")
			pourb = montant*0.2;
		} else if (montant <= 200) {
			pourb = montant*0.15;
		} else {
			pourb = montant*0.1;
		}//4
		console.log("Pourboire : ",pourb,"$  Facture finale",montant+pourb,"$");
	}//5
	calculateTip();

//Exercice 3 : Trouver Les Nombres Divisibles Par 23
	//1//..//4
	function isDivisible(){
		console.log("Outcome : ")
		let summ = 0;
		for (var i = 0; i <= 500; i++) {
			if ( i%23 == 0) {
				console.log(i+" ");
				summ += i;
			}
		}
		console.log("Sum : ",summ);
	}
	isDivisible();

	//5 Bonus
	function isDivisible(divisor){
		console.log("Tous les nombres divisible par",divisor,": ")
		let summ = 0;
		for (var i = 0; i <= 500; i++) {
			if ( i%divisor == 0) {
				console.log(i+" ");
				summ += i;
			}
		}
		console.log("Sum : ",summ);
	}
	isDivisible(Number(prompt("Entrez un nombre : ")));

//Exercice 4 : Liste De Courses
	//1
	let stock = { 
	    "banana": 6, 
	    "apple": 0,
	    "pear": 12,
	    "orange": 32,
	    "blueberry":1
	}  

	let prices = {    
	    "banana": 4, 
	    "apple": 2, 
	    "pear": 1,
	    "orange": 1.5,
	    "blueberry":10
	} 
	//2
	let shoppingList = [
		"banana",
		"orange",
		"apple"
	];
	//3//4
	function myBill() {
		let sum = 0;
		for(x of shoppingList){
			if (stock[x] > 0) {
				sum += prices[x];
				stock[x] -= 1;//6 Bonus
			} else {
				console.log("Rupture de stock : ",x);
			}
		}
		console.log("Le prix total est : ",sum);
	}//5
	myBill();

//Exercice 5 : Qu'y A-T-Il Dans Mon Portefeuille ?
	//1
	function changeEnough(itemPrice, amountOfChange) {
		let sum = 0;//3
		sum += amountOfChange[0]*0.25;
		sum += amountOfChange[1]*0.10;
		sum += amountOfChange[2]*0.05;
		sum += amountOfChange[3]*0.01;
		if(sum >= itemPrice) {
			return true;//2
		} else {
			return false;
		}
	}
	changeEnough(14.11, [2,100,0,0]);
	changeEnough(0.75, [0,0,20,5]);

//Exercice 6 : Frais De Vacances
	//1
	function hotelCost() {	
		while(1) {
			let nombreNuit = prompt("Combien de nuit souhaitez vous séjourner à l'hotel");
			type = Number(nombreNuit);
			if (!type) {
				console.log("Erreur!!! Entrez un nombre de nuit");
			} else return 140*type;
		}
	}
	//2
	function planeRideCost() {
		while(1) {
			let destination = prompt("Quelle est votre destination ?");
			type = Number(destination);
			if (type) {
				console.log("Erreur!!! Entrez votre destination");
			} else {
				if (destination=="Londres") return 183;
				else if (destination=="Paris") return 220;
				else return 300;
			}
		}
	}
	//3
	function rentalCarcost() {
		while(1) {
			let location = prompt("Combien de jours souhaitez vous louer la voiture");
			type = Number(location);
			if (!type) console.log("Erreur!!! Entrez un chiffre"); 
			else {
				if (type > 10) return 40*type-40*type*0.1;
				else return 40*type;
			}
		}
	}

	//4
	function totalVacationCost() {
		console.log("La voiture coûte : " + rentalCarcost() + ", l'hôtel coûte " + hotelCost() + ", les billets d'avions coûtent " + planeRideCost())
	}
	//5
	totalVacationCost();

