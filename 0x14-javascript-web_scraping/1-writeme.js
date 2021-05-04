#!/usr/bin/node

const fs = require('fs');
const path = (process.argv[2]);
const string_to_write = (process.argv[3]);
fs.writeFile(path, string_to_write, 'utf8',function (err) {
  if (err) return console.log(err);
});
