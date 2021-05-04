#!/usr/bin/node

const fs = require('fs');
const path = (process.argv[2]);
const stringWrite = (process.argv[3]);
fs.writeFile(path, stringWrite, 'utf8', function (err) {
  if (err) return console.log(err);
});
