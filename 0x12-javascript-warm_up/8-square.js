#!/usr/bin/node
const process = require('process');
const args = process.argv;
const size = parseInt(args[2]);
if (size) {
  let i = 0;
  let j = 0;
  let square = '';
  while (i < size) {
    while (j < size) {
      square = square + 'X';
      j = j + 1;
    }
    j = 0;
    i = i + 1;
    if (i < size) {
      square = square + '\n';
    }
  }
  console.log(square);
} else {
  console.log('Missing size');
}
