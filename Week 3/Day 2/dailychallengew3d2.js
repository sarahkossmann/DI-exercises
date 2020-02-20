const body = document.getElementsByTagName('body')[0];
const root = document.createElement('div');
	body.appendChild(root);

const input = document.createElement('input')
	input.setAttribute('type','text')
	input.setAttribute('placeholder','type new color');
	input.setAttribute('id', 'myColor')
	root.appendChild(input)
	


const btn = document.createElement('button')
	root.appendChild(btn)
	btn.innerText = 'click to change color'
	btn.addEventListener('mouseover',function (event){
		btn.style.background = 'green';
	})
	btn.addEventListener('mouseleave', function(event){
		btn.style.background = 'grey';
	})

	btn.addEventListener('click', function(event){
		btn.style.background = 'red'

	})
	btn.addEventListener('click', function(event){
		console.log(input.value)
		let myColor = document.getElementById('myColor').value;
		body.style.backgroundColor = myColor;

		})
	btn.setAttribute('draggable', 'true');
	btn.addEventListener('drag', function(event){
	let x = event.clientX;
	let y = event.clientY;
	btn.style.left = x + 'px';
	btn.style.top = y +'px';
	console.log(x)
	console.log(y)
	})
	btn.addEventListener('drop', function(event){
	
	})




















