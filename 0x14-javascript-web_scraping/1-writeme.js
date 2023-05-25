#!/usr/bin/node
// Write to a file using the fs module
const fs = require('fs');
const filePath = process.argv[2];
const fileContent = process.argv[3];

fs.writeFile(filePath, fileContent, 'utf-8', (error) => {
  if (error) console.log(error);
});
