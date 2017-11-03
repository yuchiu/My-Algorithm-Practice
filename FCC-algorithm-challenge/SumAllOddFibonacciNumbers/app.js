/*
Given a positive integer num, return the sum of all odd Fibonacci numbers that are less than or equal to num.

The first two numbers in the Fibonacci sequence are 1 and 1. Every additional number in the sequence is the 
sum of the two previous numbers. The first six numbers of the Fibonacci sequence are 1, 1, 2, 3, 5 and 8.

For example, sumFibs(10) should return 10 because all odd Fibonacci numbers less than 10 are 1, 1, 3, and 5.
*/
function sumFibs(num) {
    let ans = 0;
    let sum = 0;
    let combine = [0, 1];
    while (sum+combine[0]<= num) {
        sum = combine[0] + combine[1];

        console.log('combine[0] + combine[1] = sum : '+combine[0] + ' + ' + combine[1] + ' = ' + sum)

        if (sum % 2 !== 0) {
            let printt = ans + sum;
        console.log('ans = ans + sum : '+ ans + ' + ' + sum +' = '+ printt);
            ans += sum;
        }

        combine[0] = combine[1];
        combine[1] = sum;

        console.log('new combine[0] assign to: ' + combine[0] + ' , '+' new combine[1] assign to: '+ combine[1])
    }
    return ans + 1;
}
console.log(
    sumFibs(1)
);
console.log(
    sumFibs(1000)
);
console.log(
    sumFibs(4000000)
);
console.log(
    sumFibs(4)
);
console.log(
    sumFibs(75024)
);
console.log(
    sumFibs(75025)
);