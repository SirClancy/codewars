#! /usr/bin/python

def tribonacci(signature, n):
  res = signature[:n]
  for i in range(n - 3): res.append(sum(res[-3:]))
  return res

print tribonacci([1, 1, 1], 10)