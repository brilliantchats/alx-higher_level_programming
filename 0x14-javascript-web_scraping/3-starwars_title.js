#!/usr/bin/node
// Use request to fetch data from an API
const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + id;

request(url, (error, response, body) => {
  if (error) console.log(error);
  const filmData = JSON.parse(body);
  console.log(filmData.title);
});
