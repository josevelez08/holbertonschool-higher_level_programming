#!/usr/bin/node

const request = require('request');
const path = (process.argv[2]);
const fs = require('fs');
const fileName = process.argv[3];

request(path, function (err, response, body) {
  if (err) {
    return console.log(err);
  }
  fs.writeFile(fileName, body, 'utf8', function (err) {
    if (err) return console.log(err);
  });
});
