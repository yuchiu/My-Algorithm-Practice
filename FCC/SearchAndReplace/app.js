/*
Perform a search and replace on the sentence using the arguments provided and return the new sentence.

First argument is the sentence to perform the search and replace on.

Second argument is the word that you will be replacing (before).

Third argument is what you will be replacing the second argument with (after).
*/

function myReplace(str, before, after) {

  let strArr = str.split('');
  let beforeArr = before.split('');
  let afterArr = after.split('');

  let position = str.search(before);

  if(strArr[position] === strArr[position].toUpperCase()){
    afterArr[0] = afterArr[0].toUpperCase();
  }

  for(let i = 0; i<beforeArr.length; i++){
    strArr.splice(position,1);
  }
  
  for(let i = 0; i<after.length; i++){
    strArr.splice(position+i,0,afterArr[i]);
  }

  return strArr.join('');
}

console.log(myReplace("A quick brown fox jumped over the lazy dog", "jumped", "leaped"));

console.log(myReplace("He is Sleeping on the couch", "Sleeping", "sitting"));

console.log(myReplace("His name is Tom", "Tom", "john"));

console.log(myReplace("Let us get back to more Coding", "Coding", "algorithms"));