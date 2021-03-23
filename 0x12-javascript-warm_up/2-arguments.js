#!/usr/bin/node
if (process.argv[3] != null){
    console.log('Arguments found')
    return
}
if (process.argv[2] != null){
    console.log('Argument found')
    return
}
if (process.argv[2] == null){
    console.log('No argument')
    return
}
