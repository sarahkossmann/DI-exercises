
var allBooks = [
{ 
	title: 'Harry Potter',
	author: 'J.K. Rowling',
	image: 'https://is3-ssl.mzstatic.com/image/thumb/Video128/v4/ac/4a/c3/ac4ac3d4-11b7-d8fe-47d8-656f9076f192/pr_source.lsr/268x0w.png',
	alreadyRead: true },
 
{ 
	title: 'The Hunger Games',
	author: 'Suzanne Collins' ,
	image: 'https://images-na.ssl-images-amazon.com/images/I/415c0d-pmLL._SX303_BO1,204,203,200_.jpg',
	alreadyRead: false },

{	title: 'Da Vinci Code',
	author: 'Dan Brown' ,
	image: 'https://images-na.ssl-images-amazon.com/images/I/91Q5dCjc2KL.jpg',
	alreadyRead: true }
	]


	let body = document.querySelector ('body');//selectionner le premier element qui repond au param (body)
	let container = document.createElement('div');
		container.classList.add('container'); //rajoute une classe a l'elem
	body.appendChild(container); //coller le container au body

	allBooks.forEach(book=>{
		console.log(book); //il va looper au travers des items de la var allbooks
		let box = document.createElement('div');
			box.classList.add('book-box')
		let image = document.createElement('img');
		let title = document.createElement('h1');
		let paragraph = document.createElement('h3')
		let author = document.createElement('h2');


		image.setAttribute('src', book.image);
		image.style.width='300px'
		image.style.height='400px'
			box.appendChild(image)
		title.innerText = book.title;
			box.appendChild(title);
		paragraph.innerText = ' written by ';
			box.appendChild(paragraph);
		author.innerText = book.author;
			box.appendChild(author);
		// if (book.alreadyRead == true) {
		// 	box.classList.add('read')
		// }
		// else{
		// 	box.classList.add('notread')
		// }
		//  or ternary operator 
		book.alreadyRead == true ? box.classList.add('read') : box.classList.add('notread')
		


		container.appendChild(box)	


	})


	//let ul = document.createElement('UL')
	//ul.innerText = allBooks
	// var i = 0
	// for (var i = 0; i < allBooks.length; i++) {
	// var finalBooks = allBooks[i].title + ' written by ' + allBooks[i].author
	// let temp = document.createElement('p')
	// temp.innerText = finalBooks
	// document.write(finalBooks)

	// }
	// allBooks.forEach( item =>{
	// 	let title = document.createElement('h2');
	// 	let author = document.createElement('h3');

	// 	title.innerText=item.title;
	// 	author.innerText=item.author;

	// })
	//document.createElement('body')
	//parentNode.appendChild('body')

	// for (var i = 0; i < allBooks.length; i++) {
	// 	let titleList = document.createElement('div');
	// 	titleList.innerText = allBooks[i];
	// 	titleList.appendChild(titleList);
	// 	for (var j = 0; j <allBooks.length; j++) {
	// 	let authorList = document.createElement('div');
	// 	authorList.innerText = allBooks[i];
	// 	authorList.appendChild(authorList);	
	// 	}

	// }
// var table = document.createElement('div')
// table.setAttribute('class','table')
// table.id = 'content'

// var perrow = 2,
// 	table = document.createElement('table'),
// 	row = table.insertRow()