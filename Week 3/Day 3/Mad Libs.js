let root = document.getElementById('root');
let h1 = document.createElement('h1');
let ul = document.createElement('ul');
let li = document.createElement('li');
let li2 = document.createElement('li');
let li3 = document.createElement('li');
let input = document.createElement('input');
let input2 = document.createElement('input');
let input3 = document.createElement('input');
let btn = document.createElement('button');




h1.innerText = 'Mad Libs'
li.innerText = 'Noun'
li2.innerText = 'Adjective'
li3.innerText = "Someone's name"
btn.innerText = 'Lib it!'



root.appendChild(h1);
h1.appendChild(ul);
ul.appendChild(li);
li.appendChild(input);
li.appendChild(li2);
li2.appendChild(input2);
li2.appendChild(li3);
li3.appendChild(input3);
root.appendChild(btn);


function genetaaaa(){
	let span = document.createElement('span');
	let sentence = document.createElement('p');
	sentence.innerText = 'If you take the ' + input.value + ' that is ' + input2.value +' you will please ' + input3.value
	span.appendChild(sentence);
	root.appendChild(span);

}

btn.addEventListener('click', genetaaaa);
