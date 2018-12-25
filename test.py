thisList = ["apple", "banana", "cherry"]

thisList = [3,8,9,5,8,4,2]
thisList.append(7)
thisList.reverse()
thisList.remove(8)
thatList = []

_input = int(input("Index: "))

for k in range(0,_input):
    thatList.append(thisList.pop(0))


print("\n".join(str(i) for i in thisList))
print()
print("\n".join(str(i) for i in thatList))
