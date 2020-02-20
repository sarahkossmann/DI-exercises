/*Exercise 1
Ask a number to the user, and save it to a variable.
Check if the variable is an even number
If yes, display: “x is an even number’. Where x is the actual number of the user
If no, display “x is not an even number’. Where x is the actual number of the user
Exercise 2
Create 2 variables, x and y =. Each of them has a different numeric value
Write an if/else statement that display the bigger number
Exercise 3 : The World Translator
Ask the user which language he speaks
Create a few conditions :
If he speaks French : display “Bonjour”
If he speaks English : display “Hello”
If he speaks Hebrew : display “Shalom”
If he doesn’t speak none of these 3 languages: display “😊”
Exercise 4 : The Grade Assigner: Use Switch Case
Ask the user for his grade
If the score is bigger than 90, console.log ‘A’
If the score is between 80 and 90, console.log ‘B’
If the score is between 70 and 80, console.log ‘C’
If the score is lower than 70, console.log ‘D’*/

var num= prompt('what is your number?')

if (num%2 == 0 ){
	alert('x is an even number');
}
else {
	alert('x is not an even number');
}


var x = 5 
var y = 12

if (x>y) {

	alert (x + ' number is the biggest')
}
 else{

 	alert (x + ' number is the smallest')
 }

 var language = prompt('Which language do you speak?')

 if (language === 'French'){
 	alert ('Bonjour');
 }
 else if (language === 'English'){
 	alert ('Hello');
 }
 else if (language=== 'Hebrew') {
 	alert ('Shalom');
 }
 else {
 	alert ('😊');
 }

var grade = prompt ('what is your grade?')

if (grade>= 90){
	alert ('A');
}
else if (grade >= 80 && grade <= 90){
	alert ('B');
}
else if (grade >= 70 && grade <= 80){
	alert ('C');
}
else {
	alert ('D');
}

