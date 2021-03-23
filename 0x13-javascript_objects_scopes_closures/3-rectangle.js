#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w !== 0 && w > 0 && h !== 0 && h > 0 && w !== undefined && h !== undefined) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i;
    const y = 'X';
    const result = y.repeat(this.width);
    for (i = 0; i < this.height; i++) {
      console.log(result);
    }
  }
}
module.exports = Rectangle;
