#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (err, response) {
  if (err) {
    return console.log(err);
  }
  console.log('code:', response && response.statusCode);
});
