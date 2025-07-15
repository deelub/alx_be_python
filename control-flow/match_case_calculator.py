def match_calculator(num1,num2,operation):
	match operation:
		case "+":
			return print (f"The result is {num1+num2}")
		case "-":
			return print (f"The result is {num1-num2}")
		case "*":
			return print (f"The result is {num1*num2}")
		case "/":
			if num2==0:
				return "Cannot divide by zero."
				num2_2=int(input("Please enter another number"))
				match_calculator(num1,num2_2,operation)
			else:
				return print (f"The result is {num1/num2}")


num1=int(input("Enter the first number:"))
num2=int(input("Enter a second number"))
operation=input("Please select the type of operation(+, -, *, /):")
match_calculator(num1,num2,operation)

