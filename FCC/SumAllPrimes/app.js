/*Sum all the prime numbers up to and including the provided number.

A prime number is defined as a number greater than one and having only two divisors, one and itself. For example, 2 is a prime number because it's only divisible by one and two.

The provided number may not be a prime.
*/

function sumPrimes(num) {
    let sum = 0;
    let numArr = [];
    for (let i = 2; i <= num; i++) {
        numArr.push(i);
    }
    for (let i = 0; i < numArr.length; i++) {
        for (let j = i + 1; j < numArr.length; j++) {

            if (numArr[j] % numArr[i] === 0) {
                console.log('splicing element ' + numArr[j] + ' which is the multiple of ' + numArr[i]);
                numArr.splice(j, 1);
                console.log('current numArr ' + numArr);
            }
        }
    }
    for (let i = 0; i < numArr.length; i++) {
        sum += numArr[i];
    }
    return sum;
}

console.log('the sum of all primes within the number '+20+ ' is '+sumPrimes(20));