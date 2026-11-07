#CALCULATOR
import click
# Operator chosen must be in ('+', '-', '*', '/')
# Input must be having spaces.
try:
	num1, oper, num2 = input("Enter the operation you want to perform: ").split(" ")
	num1 = int(num1)
	num2 = int(num2)
	
	def addition(num1, num2):
		click.echo(click.style(num1+num2, fg='green')) 

	def subtraction(num1, num2):
		click.echo(click.style(num1-num2, fg='green'))

	def multiplication(num1, num2):
		click.echo(click.style(num1*num2, fg='green'))

	def division(num1, num2):
		click.echo(click.style(num1/num2, fg='green'))

	def power(num1, num2):
		click.echo(click.style(num1**num2, fg='green'))

	def remainder(num1, num2):
		click.echo(click.style(num1%num2, fg='green'))

	def greater_than(num1, num2):
		if num1 > num2:
			click.echo(click.style("True", fg='green'))
		else:
			click.echo(click.style("False", fg='green'))

	def less_than(num1, num2):
		if num1 < num2:
			click.echo(click.style("True", fg='green'))
		else:
			click.echo(click.style("False", fg='green'))

	if oper == '+':
		addition(num1, num2)

	elif oper == '-':
		subtraction(num1, num2)

	elif oper == '*':
		multiplication(num1, num2)

	elif oper == '/':
		division(num1, num2)

	elif oper == '**':
		power(num1, num2)

	elif oper == '%':
		remainder(num1, num2)

	elif oper == '>':
		greater_than(num1, num2)

	elif oper == '<':
		less_than(num1, num2)

	else:
		click.echo(click.style("Invalid operation.", fg='red'))
except ValueError:
	click.echo(click.style("Please provide only single space between every element.",fg="red"))
