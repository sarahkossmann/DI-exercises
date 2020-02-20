const root = document.getElementById('root');
const h1 = document.createElement('h1');
var ul = document.createElement('ul');
const input = document.createElement ('input');
const btn = document.createElement('button');
var btn2 = document.createElement('button');

h1.innerText = 'Shopping list';
btn.innerText= 'Add to the list';
btn2.innerText= 'Clear all';


root.appendChild(h1)
root.appendChild(input)
root.appendChild(btn)
root.appendChild(btn2)
root.appendChild(ul)


function addItem(){
	if (input.value !== ' ') {
	let li = document.createElement('li');
	li.innerText = input.value;
	ul.appendChild(li)
	}
}
btn.addEventListener('click', addItem)

function deleteItem(){
 let allItems = document.querySelectorAll("li");
 for (var i = 0; i <allItems.length; i ++){
 	allItems[i].remove();
 }	


	}


btn2.addEventListener('click', deleteItem)



