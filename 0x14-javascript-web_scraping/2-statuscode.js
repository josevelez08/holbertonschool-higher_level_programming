#!/usr/bin/node

const https = require('https');
const path = (process.argv[2]);

https.get(path, (res) => {
  console.log('code:', res.statusCode);
}).on('error', (e) => {
  console.error(e);
});
