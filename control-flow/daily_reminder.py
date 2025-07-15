def task_priority(task,priority,time_bound):
	match priority:
		case "high":
			if time_bound=="yes":
				return print(f"Reminder : {task} is a high priority task"
				"requires immediate attention today! ")
			else:
				return print(f"Reminder : {task} is a high priority task"
				"seek to do it as soon as possible ")
		case "medium":
			if time_bound=="yes":
				return print(f"Reminder : {task} is a medium priority task"
				"requires attention today! ")
			else:
				return print(f"Reminder : {task} is a medium priority task"
				"seek to do it as soon as possible ")
		case "low":
			if time_bound=="yes":
				return print(f"Reminder : {task} is a low priority task"
				"requires attention tommorow! ")
			else:
				return print(f"Reminder : {task} is a low priority task"
				"seek to do it in your freetime ")


task=input("Enter your task:")
priority=input("Priority (high/medium/low)").lower()
time_bound=input("Is is time-bound? (yes/no)").lower()


