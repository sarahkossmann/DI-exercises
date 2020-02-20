function playGame () {

	var answer= confirm('Do you want to play a game?')
	if (answer== true)
	{
		var num= prompt ('put an number between 0 and 10');
		if (num < 0 || num > 10)
		{
			alert ('sorry not a good number, goodbye');
		}
		else if (isNaN(num))
		{
			alert ('Sorry not a number, goodbye');
		}
		
		else 
		{
			var computerNumber=Math.floor(Math.random()*10)
			alert (computerNumber);
			test(num,computerNumber)
		}
	}
	if (answer==false)
	{
		alert ('no problem');
	}


}

function test (num,computerNumber){
	var num= '';
	var computerNumber= '';
	var attempt = 3;
	do {
		alert (attempt-1); attempt--;
		}
		while (attempt=0);
//faire un loop while a condition(-1) que try =0
		if(num=computerNumber){
			alert ('you won!');
		}
		else if (num>computerNumber){
			alert ('your number is bigger, guess again');
		}
		else if (num<computerNumber){
			alert ('your number is lower, guess again');
		}
		else {
			alert ('you cant try again')

		}
	}

