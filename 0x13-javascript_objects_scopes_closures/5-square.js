#!/usr/bin/node
const Rectangle = require('./4-rectangle'); //call the parent

class Square extends Rectangle {
  constructor (size) {
    super(size, size); //call the super class constructor
  }
}
module.exports = Square;
