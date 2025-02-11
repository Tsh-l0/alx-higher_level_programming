#!/usr/bin/node

const fs = require('fs');
const filePath = process.argv[2];
const write = process.argv[3];

fs.writeFile(filePath, write, 'utf-8', (error) => {
  if (error) {
    console.error(error);
  } else {
    console.log('File written successfully');
  }
});
