//Exercice 1 : Différence D'âge
	//Étant donné les années de naissance de deux personnes, 
	//trouvez la date à laquelle la plus jeune a exactement 
	//la moitié de l'âge de la plus âgée. 
	//Notes : Les dates sont données au format AAAA 
	date1 = Number(prompt("Entrez l'année de naissance de la première personne", "1999"));
	date2 = Number(prompt("Entrez l'année de naissance de la deuxième personne", "2009"));
	/*age1 = 2022 - date1;
	age2 = 2022 - date2;
	//soit x etant l'age de la personne la plus jeune et soit y etant l'âge de la personne la plus vielle
	if (age1 != age2 ) {
		if (age1 < age2) {
			x = age1;
			y = age2; 
		} else if (age1 > age2){
			x = age2;
			y = age1;
		}
		//Si x < y/2 alors cette date n'est pas encore arrivé 
		if ( x < y/2) {
			//nous pouvons poser la formule suivante :
			// x + k = (y+k)/2 , avec k étant le nombre d'année à ajouter pour arriver à la date voulue
			// k = y-2x
			let k = y - 2*x;
			console.log("Cette date est :",2022+k);
		} else if (x > y/2) {//Si x > y/2 alors cette date n'est pas encore arrivé 
			//nous pouvons poser la formule suivante :
			// x - k = (y-k)/2 , avec k étant le nombre d'année à ajouter pour arriver à la date voulue
			// k = 2x-y
			let k = 2*x - y;
			console.log("Cette date est :",2022-k);
		} else {
			console.log("Cette date est : 2022");
		}
	} else {
		console.log("Vous avez entrez deux dates identiques");
	}*/
	//autre résolution
	if (date1>date2) {
		let x = 2*date1 - date2;
		console.log(x);
	} else if (date1<date2) {
		let x = 2*date2 - date1;
		console.log(x);
	} else {
		console.log("Les deux dates sont identiques");
	}
	
//Exercice 2 : Codes Postaux
	let code = prompt("Quel est votre code postal?","xxxxx");
	//1ère partie
	let codeNumb =Number(code);
	if (code.length == 5 &&  codeNumb) {
		console.log("Succès");
	} else {
		console.log("Error");
	}
	//2ieme partie
	if (/[0-9][0-9][0-9][0-9][0-9]$/y.test(code)) {
		console.log("Succès");
	} else {
		console.log("Error");
	}

//Exercice 3 : Mot Secret
	//1
	let mot = prompt("Entrez un mot","yooo");
	//2
	mot = mot.replace(/[a,e,i,o,u]+/g,"");
	console.log(mot);
	//3
	mot = mot.replace(/[a]+/g,"1");
	mot = mot.replace(/[e]+/g,"2");
	mot = mot.replace(/[i]+/g,"3");
	mot = mot.replace(/[o]+/g,"4");
	mot = mot.replace(/[u]+/g,"5");
	console.log(mot);