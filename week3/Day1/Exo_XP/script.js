//Exercice 1 : Utilisateurs 
//2
/*
	let div = document.getElementById("container");
	console.log(div);
	let lis = document.getElementsByTagName("li");
	for(let i=0;i<lis.length;i++){
		if (lis[i].innerHTML == "Pete") {
			lis[i].innerHTML = "Richard";
		}
	}
	for(let i=0;i<lis.length;i++){
		if (lis[i].innerHTML == "Sarah") {
			lis[i].setAttribute("id","sup")
		}
		lis[i].innerHTML = "Sank";
	}
	let sup = document.getElementById("sup")
	let ul = document.getElementsByClassName("list");
	ul[1].removeChild(sup);
	//3
	ul[0].setAttribute("class",ul[0].className+" student_list")
	ul[1].setAttribute("class",ul[1].className+" student_list")
	ul[0].setAttribute("class",ul[0].className+" university attendance")
*/

//Exercice 2 : Utilisateurs Et Style
/*	
	//1//2
	let div = document.getElementsByTagName("div")
	console.log(div)
	div[0].style.background = "#33ccff";
	//3
	let li = document.getElementsByTagName("li");
	let ul = document.getElementsByTagName("ul");
	for(let i=0;i<li.length;i++){
		if (li[i].innerHTML == "John") {
			ul[0].removeChild(li[i]);
		}
	}
	//4
	for(let i=0;i<li.length;i++){
		if (li[i].innerHTML == "Pete") {
			li[i].style.border = "2px solid black";
		}
	}
	//5
	body = document.getElementsByTagName("body");
	body[0].setAttribute("style","font-size: 150%;");
*/

// Exercice 3 : Changer La Barre De Navigation
/*
	//1//2
	let div = document.getElementsByTagName("div");
	div[0].setAttribute("id","socialNetworkNavigation");
	console.log(div[0]);
	//3
	let ul = document.getElementsByTagName("ul");
	let li1 = document.createElement("li");
	let text = document.createTextNode("Déconnexion");
	li1.appendChild(text);
	ul[0].appendChild(li1);
	//4
	console.log(ul[0].firstElementChild.textContent)
	console.log(ul[0].lastElementChild.textContent)
*/
	//Exercice 4 : Ma Liste De Livres
let allBooks = [
	{
		title :"The life",
		author :"SANKARA",
		image :"http://",
		alreadyRead :false
	},
	{
		title :"Ton corps fait pour la vie",
		author :"Daniel Ange",
		image :"http://",
		alreadyRead : true
	}
];
	let div = document.getElementsByClassName("listBooks")
	let table = document.createElement("table");
	let tr1 = document.createElement("tr");
	let tr2 = document.createElement("tr");
	let tr3 = document.createElement("tr");
	let th1 = document.createElement("th");
	let th2 = document.createElement("th");
	let th3 = document.createElement("th");
	let td1 = document.createElement("td");
	let td2 = document.createElement("td");
	let td22 = document.createElement("td");
	let td3 = document.createElement("td");
	let td4 = document.createElement("td");
	let td44 = document.createElement("td");
	let img1 = document.createElement("img");
	let img2 = document.createElement("img"); 
	div[0].appendChild(table);
	table.appendChild(tr1);
	table.appendChild(tr2);
	table.appendChild(tr3);
	tr1.appendChild(th1);
	tr1.appendChild(th2);
	tr1.appendChild(th3);
	tr2.appendChild(td1);
	tr2.appendChild(td2);
	tr2.appendChild(td22);
	tr3.appendChild(td3);
	tr3.appendChild(td4);
	tr3.appendChild(td44);
	td22.appendChild(img1);
	td44.appendChild(img2);
	th1.innerHTML = "Title";
	th2.innerHTML = "Author";
	th3.innerHTML = "Image";
	td1.innerHTML = allBooks[0].title;
	td2.innerHTML = allBooks[0].author;
	td3.innerHTML = allBooks[1].title;
	td4.innerHTML = allBooks[1].author;
	
	img1.setAttribute("src","logo.png");
	img2.setAttribute("src","img.jpg");
	img1.setAttribute("style","width : 100px");
	img2.setAttribute("style","width : 100px");
	console.log(img2);

	if (allBooks[0].alreadyRead == true) {
		tr1.setAttribute("style","color : red")	
	}
	if (allBooks[1].alreadyRead == true) {
		tr2.setAttribute("style","color : red")	
	}
