#!/usr/bin/node
// Reads a file provided by user and prints it to the screen
const fs = require('fs').promises;
const filePath = process.argv[2];

async function readFile (path) {
  try {
    const data = await fs.readFile(path, 'utf8');
    console.log(data.toString());
  } catch (error) {
    console.log(error);
  }
}
readFile(filePath);
