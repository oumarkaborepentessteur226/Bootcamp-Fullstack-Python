//Exercice 1 : Vérification De L'IMC
	//1//2
	let personne = [
		{
			nom : "Sank",
			prenom : "sss",
			masse : 100,
			taille : 175,
			imc : function () {
				return this.masse/(this.taille*this.taille);
			}
		},
		{
			nom : "Ouedra",
			prenom : "OSM",
			masse : 88,
			taille : 194,
			imc : function () {
				return this.masse/(this.taille*this.taille);
			}
		}
	];
	//3//4
	function compImc(){
		if (personne[0].imc() > personne[1].imc())
			console.log(personne[0].nom, personne[0].prenom , "a le plus grand IMC");
		else
			console.log(personne[1].nom , personne[1].prenom  , "a le plus grand IMC");
	}

	compImc();

//Exercice 2 : Moyenne Scolaire
	//1//..//4
	function findAvg(gradesList) {
		moyenne = 0;
		for(x of gradesList)
			moyenne += x;
		moyenne = moyenne / gradesList.length
		if (moyenne > 65)
			console.log("Votre moyenne est :",moyenne + ", vous avez réussi.");
		else 
			console.log("Vous avez échouez, try again");		
	}
	findAvg([42,90,86,99,85]);
	
	//Bonus
	function moy(gradesList) {
		sum = 0;
		for(x of gradesList)
			sum += x;
		return sum/gradesList.length;
	}

	function isSuccess(gradesList) {
		moy(gradesList);
		if (moyenne > 65)
			console.log("Votre moyenne est :",moyenne + ", vous avez réussi.");
		else 
			console.log("Vous avez échouez, try again");
	}

	isSuccess([42,90,86,99,85]);