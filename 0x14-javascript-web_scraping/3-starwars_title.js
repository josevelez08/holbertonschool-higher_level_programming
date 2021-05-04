#!/usr/bin/node

const request = require('request');
const path = 'https://swapi-api.hbtn.io/api/films/' + (process.argv[2]);

request(path, function (err, response) {
  if (err) {
    return console.log(err);
  }
  const hola = (JSON.parse(response.body).title);
  console.log(hola);
});
