/*
Find the smallest common multiple of the provided parameters that can be evenly divided by both, as well as by all sequential numbers in the range between these parameters.

The range will be an array of two numbers that will not necessarily be in numerical order.

e.g. for 1 and 3 - find the smallest common multiple of both 1 and 3 that is evenly divisible by all numbers between 1 and 3.
*/

function smallestCommons(arr) {
    let lcm = [];
    let numSize;
    if (arr[0] > arr[1]) {
        numSize = arr[0] - arr[1] + 1;
        for (let i = 0; i < numSize; i++) {
            lcm.push(arr[0] - i);
        }
    } else {
        numSize = arr[1] - arr[0] + 1;
        for (let i = 0; i < numSize; i++) {
            lcm.push(arr[1] - i);
        }
    }

    for (let i = 0; i < numSize - 1; i++) {
        let num1 = lcm.pop();
        let num2 = lcm.pop();

        let ans;
        //using Euclidean Algorithm to find the lcm. lcm(a,b) = ab/gcd(a,b)
        if (num1 > num2)
            ans = (num1 * num2) / gcd(num1, num2);
        else
            ans = (num1 * num2) / gcd(num2, num1);
        lcm.push(ans);
    }
    return (lcm[0]);
}

function gcd(largeNum, smallNum) {
    let remainder;
    do {
        remainder = largeNum % smallNum;
        largeNum = smallNum;
        smallNum = remainder;
    } while (remainder !== 0);

    return largeNum;
}

console.time('smallestCommons');
console.log(smallestCommons([1, 5]));
console.timeEnd('smallestCommons');

console.time('smallestCommons');
console.log(smallestCommons([1, 13]));
console.timeEnd('smallestCommons');

console.time('smallestCommons');
console.log(smallestCommons([23, 18]));
console.timeEnd('smallestCommons');

console.time('smallestCommons');
console.log(smallestCommons([1, 40]));
console.timeEnd('smallestCommons');