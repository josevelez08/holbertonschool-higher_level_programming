#!/usr/bin/node
if (process.argv[2] != null) {
  console.log(process.argv[2]);
} else if (process.argv[2] == null) {
  console.log('No argument');
}
