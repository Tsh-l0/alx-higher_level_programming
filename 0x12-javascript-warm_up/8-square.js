#!/usr/bin/node
// Prints a square

const sqrSize = parseInt(process.argv[2], 10);

if (isNaN(sqrSize) || sqrSize <= 0) {
  console.log('Missing size');
} else {
  for (let ab = 0; ab < sqrSize; ab++) {
    console.log('X'.repeat(sqrSize));
  }
}
