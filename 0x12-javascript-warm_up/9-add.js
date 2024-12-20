#!/usr/bin/node
// Prints the addition of 2 integers

function add (firstInt, secondInt) {
  return firstInt + secondInt;
}

const firstInt = parseInt(process.argv[2], 10);
const secondInt = parseInt(process.argv[3], 10);

console.log(isNaN(firstInt) || isNaN(secondInt) ? 'NaN' : add(firstInt, secondInt));
