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

  rotate () {
    this.x = this.height;
    this.height = this.width;
    this.width = this.x;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}
module.exports = Rectangle;
