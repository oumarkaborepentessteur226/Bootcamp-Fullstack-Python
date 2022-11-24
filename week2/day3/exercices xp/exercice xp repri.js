



//Exercice 1 : Liste Des Personne
	let people = ["Greg", "Mary", "Devon", "James"];
	//1
	people.shift();
	//2
	people = people.join(" ");
	people = people.replace("James","Jason");
	people = people.split(" ");
	//3
	people.push("Steve");
	//4
	console.log("L'index de Mary est" , people.indexOf("Mary"));
	//5
	let people1 = people.slice(people.indexOf("Mary"),1);
	//6
	console.log(people.indexOf());
	//il renvoie -1 prcq Foo n'existe pas
	//7
	let last = people[people.length-1];

//Partie II - Boucles
	//1
	for (let x in people) {
		console.log(people[x]);
	}
	//2
	for (let x in people) {
		console.log(people[x]);
		if (people[x] == "Jason")
			break;
	}

//Exercice 2 : Vos Couleurs Préférées
	//1
	let colors = ["white","black","green","blue","grey"];
	//2
	for (let x in colors) {
		let y=Number(x)+1;
		console.log("My # "+ y + " choise is " + colors[x]);
	}
	//3
	let suffixes = ["st","nd","rd","th","th"];
	for (let x in colors) {
		let y=Number(x)+1;
		console.log("My "+ y + suffixes[x] + " choise is " + colors[x]);
	}

//Exercice 3 : Répéter La Question
	//1
	let numero = prompt("Entrez un numéro", "4");
	type = Number(numero);
	if (!type) {
		console.log("C'est une chaine de caractère qui a été saisie");
	} else {
		console.log("C'est un nombre qui a été saisie");
	}
	//2
	while(1) {
		let numero = prompt("Entrez un numéro", "4");
		type = Number(numero);
		if (!type) {
			console.log("C'est une chaine de caractère qui a été saisie, Entrez un nombre");
		} else {
			if (numero < 10) {
				console.log("Entrez un numéro supérieur à 10 ");
			} else {
				break;
			}
		}
	}

//Exercice 4 : Gestion Du Bâtiment
	//1
	let building = {
	    numberOfFloors : 4,
	    numberOfAptByFloor : {
	        firstFloor : 3,
	        secondFloor : 4,
	        thirdFloor : 9,
	        fourthFloor : 2,
	    },
	    nameOfTenants : ["Sarah", "Dan", "David"],
	    numberOfRoomsAndRent:  {
	        sarah: [3, 990],
	        dan :  [4, 1000],
	        david : [1, 500],
	    },
	}
	//2
	console.log("The number Of Floors is : " + building.numberOfFloors);
	//3
	console.log("The number of apartement rooms of firstFloor and thirdFloor : " + building.numberOfAptByFloor.firstFloor + " and " + building.numberOfAptByFloor.thirdFloor);
	//4
	console.log("The name of second tenant is : " + building.nameOfTenants[1]);
	//5
	if (building.numberOfRoomsAndRent.sarah[1] + building.numberOfRoomsAndRent.david[1] > building.numberOfRoomsAndRent.dan[1]) {
		building.numberOfRoomsAndRent.dan[1] = 1200;
	} else {
		console.log("Pas d'augmentation");
	}
	console.log(building);

//Exercice 5 : Famille
	//1
	let famille = {
		dady : "John",
		mum : "Mary",
		son : "Richard",
	}
	//2
	for ( let x in famille) {
		console.log(x);
	}
	//3
	for (let x in famille) {
		console.log(famille[x]);
	}

//Exercice 6
	let details = {
	  my: 'name',
	  is: 'Rudolf',
	  the: 'raindeer'
	}
	for(let x in details){
		console.log(x,details[x]);
	}

//Exercice 7 : Groupe Secret
	let names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];
	//1cd
	let nom = []
	for( let x in names){
		nom[x] = names[x][0];
	}
	nom = nom.sort();
	nom = nom.join("");
	//2
	console.log(nom);