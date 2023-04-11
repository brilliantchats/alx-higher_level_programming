#!/usr/bin/node
const process = require('process');
const args = process.argv;
const fact = parseInt(args[2]);
function factorial (num) {
  if (num === 0 || num === 1 || isNaN(num)) {
    return 1;
  }
  return num * factorial(num - 1);
}
console.log(factorial(fact));
