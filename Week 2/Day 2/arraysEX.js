
//Remove the banana from the array

var array =["Banana", "Apples", "Oranges", "Blueberries"];
array.shift();
console.log(array);

//sort the array in order

array.sort();
console.log (array);

//put "Kiwi" at the end of the array
 array.push("Kiwi");
 console.log (array);

 //remove apple
delete array [0];
  console.log (array);

  //or array.splice(2,1);

//reverse

array.reverse();
console.log(array);
 
 //reach the orange
 var array2=["Banana",["Apples", ["Oranges"], "Blueberries"]]
 console.log(array2[1][1][0])