#!/usr/bin/node

const path = (process.argv[2]);
const fs = require('fs');
fs.readFile(path, 'utf8', function (err, data) {
  if (err) {
    return console.log(err);
  }
  console.log(data);
});
