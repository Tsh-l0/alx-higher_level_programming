#!/usr/bin/node
// Prints x times "C is fun"

const str = process.argv[2];
const strNum = parseInt(str, 10);

if (isNaN(strNum)) {
  console.log('Missing number of occurences');
} else {
  for (let ab = 0; ab < strNum; ab++) {
    console.log('C is fun');
  }
}
