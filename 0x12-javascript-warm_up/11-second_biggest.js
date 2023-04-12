#!/usr/bin/node
const process = require('process');
const args = process.argv;
const len = args.length;
if (len === 3) {
  console.log(0);
} else if (len > 2) {
  let size = len;
  let i = 0;
  let j = 0;
  while (i < 2) {
    while (j < size - 1) {
      if (parseInt(args[j]) > parseInt(args[j + 1])) {
        const temp = args[j + 1];
        args[j + 1] = args[j];
        args[j] = temp;
      }
      j = j + 1;
    }
    size = size - 1;
    i = i + 1;
    j = 0;
  }
  console.log(args[len - 2]);
} else {
  console.log(0);
}
