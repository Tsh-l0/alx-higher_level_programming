#!/usr/bin/node
// Computes and prints a factorial

function factorial (ac) {
  if (isNaN(ac) || ac === 0) {
    return 1;
  }
  return ac * factorial(ac - 1);
}

const fact = parseInt(process.argv[2], 10);
console.log(factorial(fact));
