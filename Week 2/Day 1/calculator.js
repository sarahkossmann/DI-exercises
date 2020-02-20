let first='';
let second='';
let sign='';

function my_f(a) {
	if(a=='+'){
	 console.log(first+second);
	}
	else if(a=='-'){
		console.log(first-second);
	}
	else if (a=='*'){
		console.log(first*second);
	}
	if(first===''){
	 	first=a;
	}
	else{
	 	second=a;
	}
}


// let x;
// function sara(a){
// 	x = a;
// 	console.log(x);
// }
// sara(0)