import click


# Model:- f(x)=wx

def ml_model_1param_diff(actaul_output):
	l1 = []
	for w in range(5):
		sum = 0
		for x,y in actaul_output:
			yhat = y - w*x
			sum = sum+yhat
			click.secho(f"{x},{y},{sum}", fg="yellow")
		click.secho(f"sum for w-> {w} is {sum}", fg="green")
		l1.append((w, sum))
	print(l1)





# def ml_cf_1param():


if __name__ == "__main__":
	actual_output = [(1,1), (2,1.5), (3,3), (4,4.5)]
	ml_model_1param_diff(actual_output)

