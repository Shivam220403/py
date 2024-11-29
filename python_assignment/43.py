message = []
print("Enter student details")
for i in range(0, 2):
	details = []
	name = str(input("Enter the name of student: ")).lower()
	f_name = str(input("Enter the fathers name: "))
	branch = str(input("Enter the branch: "))
	absence = str(input("Enter the Number of days of absence: "))

	details.append(name)
	details.append(f_name)
	details.append(branch)
	details.append(absence)

	message.append(details)

student = str(input("Enter the name of student you want to send: ")).lower()
for i in range(0, 2):
	if message[i][0] == student:
		print(f"Dear {message[i][1]} , your ward {message[i][0]} of course {message[i][2]} is absent for {message[i][3]} days from the college.")

