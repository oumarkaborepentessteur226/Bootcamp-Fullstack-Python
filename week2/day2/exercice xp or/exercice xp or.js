//Exercice 1 : Le Traducteur Du Monde
	//1
	let langue = prompt("Quelle langue parler vous ?");
	//2
	langue = langue.toLowerCase();
	//3//..//7
	switch(langue) {
		case "français":
		console.log("Bonjour");
		break;
		case "anglais":
		console.log("Hello");
		break;
		case "hébreu":
		console.log("Shalom");		
		break;
		default:
		console.log("01110011 01101111 01110010 01110010 01111001");
	}

//Exercice 2 : L'assignateur De Notes
	//1
	let note = prompt("Quelle est votre note ?");
	//1//..//5
	if (note > 90) {
		console.log("A");
	} else if (note > 80) {
		console.log("B");
	} else if (note >= 70) {
		console.log("C");
	} else {
		console.log("D");
	}

//Exercice 3 : Verbe
	//1
	let verbe = prompt("Entrez un verbe :" , "manger"); 
	if (verbe.length >= 3) {
		if (!(verbe.match(/ing$/i))) {
			console.log(verbe +"ing");
		} else {
			console.log(verbe + "ly")
		}
	} else {
		console.log(verbe);
	}



