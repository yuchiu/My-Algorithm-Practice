/*
Convert a string to spinal case. Spinal case is all-lowercase-words-joined-by-dashes.
*/

function spinalCase(str) {
  let arr = str.split('');
  console.log(str);
    arr[0] = arr[0].toLowerCase();

  for(let i = 1; i<arr.length; i++){
    if(arr[i].toLowerCase() == arr[i].toUpperCase() ){
      console.log('i is "'+i+'", removing "'+arr[i]+'"');
      arr[i+1] = arr[i+1].toLowerCase();
      arr[i] = '-';
    }else if(arr[i] !== arr[i].toLowerCase()){
      arr[i] = arr[i].toLowerCase();
      arr.splice(i,0,'-');
    }
  }
  arr = arr.join('');
  return arr;
}

console.log(
spinalCase('This Is Spinal Tap')
);
console.log(
spinalCase("The_Andy_Griffith_Show")
);
console.log(
spinalCase("thisIsSpinalTap")
);
