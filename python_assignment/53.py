diction = {
	"1":35,
	"2":76,
	"3":43,
	"4":90,
	"5":5
}
print(diction)
temp = []
for i in diction:
	temp.append(diction[i])
temp.sort()
for i, j in enumerate(diction):
	diction[j] = temp[i]

print(diction)
