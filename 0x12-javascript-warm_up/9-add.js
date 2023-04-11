#!/usr/bin/node
const process = require('process');
const args = process.argv;
const first = parseInt(args[2]);
const second = parseInt(args[3]);
function add (a, b) {
  console.log(a + b);
}
add(first, second);
