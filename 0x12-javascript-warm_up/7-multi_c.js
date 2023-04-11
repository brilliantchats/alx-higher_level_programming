#!/usr/bin/node
const process = require('process');
const args = process.argv;
const firstArg = parseInt(args[2]);
if (firstArg) {
  let i = 0;
  while (i < firstArg) {
    console.log('C is fun');
    i = i + 1;
  }
} else {
  console.log('Missing number of occurrences');
}
