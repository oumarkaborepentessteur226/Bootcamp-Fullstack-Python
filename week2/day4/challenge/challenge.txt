// //1
// 	let mots = prompt("Entrez plusieurs mots séparés par des virgules");
// //2//3//4
// 	mots = mots.split(",");
// 	let longEtoile = 0;
// 	let etoile = "*";
// 	for (let x of mots)
// 		if (longEtoile < x.length) 
// 			longEtoile = x.length;
// 	for (var i = longEtoile + 4; i > 1; i--) 
// 		etoile = etoile + "*";
// 	console.log(etoile);
// 	for (let x of mots) {
// 		let mot = "* " + x;
// 		for (i=mot.length; i < longEtoile+3; i++)
// 			mot = mot + " ";
// 		console.log(mot + "*");
// 	}
// 	console.log(etoile);


function plusGrand(mots) {
	let longEtoile = 0;
	for (let x of mots)
		if (longEtoile < x.length) 
			longEtoile = x.length;
	return longEtoile;
}

function etoile(longEtoile) {
	let etoile = "*";
	for (var i = longEtoile + 4; i > 1; i--) 
		etoile = etoile + "*";
	return etoile;
}

function affiche(mots) {
	mots = mots.split(",");
	longEtoile=plusGrand(mots);
	etoile=etoile(longEtoile);
	console.log(etoile);
	for (let x of mots) {
		let mot = "* " + x;
		for (i=mot.length; i < longEtoile+3; i++)
			mot = mot + " ";
		console.log(mot + "*");
	}
	console.log(etoile);
}

affiche(prompt("Entrez plusieurs mots séparés par des virgules"));