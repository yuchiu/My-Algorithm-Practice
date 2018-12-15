/*
convert the given number into a roman numeral.

All roman numerals answers should be provided in upper-case.
*/



function convertToRoman(num) {
  let romanChar = ['M', 'D', 'C', 'L', 'X', 'V', 'I'];
  let romanNum = [1000, 500, 100, 50, 10, 5, 1];
  let numOfRomanChar = [];
  let ans = [];
  let remainder = num;
  for (let i = 0; i < romanNum.length; i++) {

    numOfRomanChar.push(Math.floor(remainder / romanNum[i]));

    remainder = remainder % romanNum[i];

  }

  for (let i = 0; i < 7; i++) {

    if(numOfRomanChar[i] === 1 && numOfRomanChar[i+1]===4){
      ans.push(romanChar[i+1]);
      ans.push(romanChar[i-1]);
    }
    
    else if (numOfRomanChar[i] === 4&&numOfRomanChar[i-1]!==1)  {
      ans.push(romanChar[i]);
      ans.push(romanChar[i-1]);
    } 
    
    else if(numOfRomanChar[i] !== 4){
            for (let j = 0; j < numOfRomanChar[i]; j++) {
        ans.push(romanChar[i]);
      }
    }
  }
  ans = ans.join('');
  return ans;
}

console.log(convertToRoman(83));
console.log(convertToRoman(14));
console.log(convertToRoman(3459));
console.log(convertToRoman(681));