#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
    this.size = size;
  }

  charPrint (c) {
    let y;
    if (c !== undefined) {
      y = 'C';
    } else {
      y = 'X';
    }
    let i;
    const result = y.repeat(this.size);
    for (i = 0; i < this.size; i++) {
      console.log(result);
    }
  }
}
module.exports = Square;
