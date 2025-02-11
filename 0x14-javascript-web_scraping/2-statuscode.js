#!/usr/bin/node

const request = require('request');
const filePath = process.argv[2];

request.get(filePath, (err, response) => {
  if (err) {
    console.error(err);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
