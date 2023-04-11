#!/usr/bin/node
const process = require('process');
const args = process.argv;
const first = parseInt(args[2]);
if (first) {
  console.log('My number: ' + first);
} else {
  console.log('Not a number');
}
