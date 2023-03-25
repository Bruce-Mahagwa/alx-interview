#!/usr/bin/python3

"""
returns a list containing lists of pascal sequences
"""

def formula(n, k):
  if (n == 0 or n == 1):
      return 1;
  fact_n = 1;
  fact_k = 1;
  for i in range(2,n + 1):
    fact_n *= i;
  for i in range(2, k + 1):
    fact_k *= i
  fact_diff = n - k;
  fact_diff_fact = 1;
  for i in range(2, fact_diff + 1):
    fact_diff_fact *= i
  return (fact_n / (fact_k * fact_diff_fact))

def pascal_triangle(n):
  arr = [[1], [1, 1]];
  for i in range(2,n):
    placeholderarr = [];
    for j in range(0, i+1):
      placeholderarr.append(int(formula(i, j)))
    arr.append(placeholderarr)
  return arr;
