#!/usr/bin/node

const https = require('https');
const path = (process.argv[2]);

const req = https.request(path, (res) => {
  console.log('code:', res.statusCode);
});

req.on('error', (e) => {
  console.error(e);
});
req.end();
