#!/usr/bin/node
if (isNaN(process.argv[2])) {
  console.log(1);
}
console.log(factorial(process.argv[2]));

function factorial (n) {
  if (n <= 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
