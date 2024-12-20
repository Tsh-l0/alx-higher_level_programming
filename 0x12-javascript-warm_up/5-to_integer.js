#!/usr/bin/node

// Prints the first argument converted to an integer

const args = process.argv[2];
const num = parseInt(args, 10);

if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${num}`);
}
