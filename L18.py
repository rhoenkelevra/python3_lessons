# this one is like your scripts with argv
def print_two(*args):
	arg1, arg2 = args
	print(f"arg1: {arg1}, arg2: {arg2}")
	
print_two("Mateus", "Dudu")

def print_one(arg1):
	print(f"arg:1 {arg1}")
	
print_one("Sara")	
