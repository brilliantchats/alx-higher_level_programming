#!/usr/bin/node
// Reads a file provided by user and prints it to the screen
const fs = require('fs');
const filePath = process.argv[2];

fs.readFile(filePath, 'utf8', (data, error) => {
  if (error) console.log(error);
  else {
    console.log(data);
  }
});
