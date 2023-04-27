
s= "school"                          # all the "o" has index 3
s1 = ""
i = 0

for x in s:
    if s.index(x) == i:
        s1 = s1 + x
    else:
        char = s[i]                   # holds repeated character
        if char == s1[s[i]+1]:
            s1 = s1.replace(char,"!")
        else:
            s1= s1

    i += 1
print(s1)
'''
list1 = [1,2,3,4,5,6,2,3,4,9,1,6,6]
list2 = []
for i in range(len(list1)):
    for j in range(i+1,len(list1)):
        if list1[i]==list1[j]:
            list2.append(list1[j])
for i in list2:
    list1.remove(i)
print(list1)


notes = "Cucumber, Please remember to buuy the following things: \n \tFish, \n \tShell \n \tPolish, \n \tFish, \n \tSlippers,\n \t"
print(len(notes))
notes = notes[10:30]+notes[31:len(notes)]+notes[0:8]+"."
print(notes)
print(len(notes))


s = "goodjobboy"
i=0
l = ""
n = len(s)
while i<=n-2:
    i = i + 3
    l = l+s[i-1]

print(l)
'''
