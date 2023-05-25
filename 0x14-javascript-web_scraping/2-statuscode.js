#!/usr/bin/node
// display the status code of a GET request
const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) console.log(`code: ${response.statusCode}`);
  console.log(`code: ${response.statusCode}`);
});
