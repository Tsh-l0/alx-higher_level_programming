#!/usr/bin/node

// Writes a class Rectangle that defines a rectangle

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let aa = 0; aa < this.height; aa++) {
      console.log('X'.repeat(this.width));
    }
  }
}

module.exports = Rectangle;
