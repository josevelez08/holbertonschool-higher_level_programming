#!/usr/bin/node

const request = require('request');
const path = (process.argv[2]);

request(path, function (err, response, body) {
  if (err) {
    return console.log(err);
  }
  console.log(JSON.parse(body));
});
