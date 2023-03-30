#!/usr/bin/node

function add(a, b){
  /**
     * Addition of two integers
     * Use arguments
     *  a: arguments of first int
     *  b: second argument in int
     */
  a = parseInt(process.argv[2]);
  b= parseInt(process.argv[3]);
  const result = a + b;
  console.log(result);
}

add(10, 30);
