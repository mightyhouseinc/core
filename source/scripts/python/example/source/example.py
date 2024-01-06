#!/usr/bin/env python3

def dont_load_this_function(left, right):
	# This function will be loaded anyway because ducktype is supported now
	result = left * right
	print(left, ' * ', right, ' = ', result)
	return result

def multiply(left: int, right: int) -> int:
	result = left * right
	print(left, ' * ', right, ' = ', result)
	return result

def divide(left: float, right: float) -> float:
	if right != 0.0:
		result = left / right
		print(left, ' / ', right, ' = ', result)
	else:
		print('Invalid right operand: ', right)
	return result

def sum(left: int, right: int) -> int:
	result = left + right
	print(left, ' + ', right, ' = ', result)
	return result

def hello():
	print('Hello World from Python!!')
	return

def strcat(left: str, right: str) -> str:
	result = left + right
	print(left, ' + ', right, ' = ', result)
	return result

def bytebuff(input: bytes) -> bytes:
	print(input)
	print('Input length: ', len(input))
	buffer = b'abcd'
	print(buffer)
	print('Output length: ', len(buffer))
	return buffer

def return_array():
	return [1, 2, 3]

def return_same_array(arr):
	return arr
