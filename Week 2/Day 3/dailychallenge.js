	const num =[5,0,9,1,7,4,2,6,3,8];
  let temp;

for (let i = 0; i < num.length; i++) 
{
  for (let j = i; j < num.length; j++) 
  {

    if (num[j]>num[i])
    {
        temp= num[i];
        num[i]=num[j];  // 3
        num[j]=num[j-1];
        num[j]=temp
    } 
        
  }
}
    

    
		    
  

console.log(num)



