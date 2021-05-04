#!/usr/bin/node

const request = require('request');
const path = 'https://swapi-api.hbtn.io/api/films/';
let count = 0;

request(path, function (err, response) {
  if (err) {
    return console.log(err);
  }
  const hola = (JSON.parse(response.body));

  for (const pelis in hola.results) {
    for (const perso in (hola.results[pelis].characters)) {
      const url = (hola.results[pelis].characters[perso]).split('/');
      if (url[5] === '18') {
        count++;
      }
    }
  }
  console.log(count);
});
