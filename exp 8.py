# question no 1
d ={'a': 3, 'b':1,'c':2}
# Ascending
asc = dict(sorted(d.items(), key=lambda x:x[1]))
print(" ascending:", asc)
# Descsnding
desc =dict(sorted(d.items(), key=lambda x: x[1], reverse=True))
print("Descending:", desc)


# question no 2
d={'a':1,'b':2}
key='a'
if key in d:
    print("key exists")
else:
    print("key does not exist")
    
    
# question no 3
d1={'a':1}
d2={'b':2}
d3={**d1, **d2}
print(d3)


# question no 4
t=(1,2,3)
t=t+(4,)
print(t)


# question no 5
t=(1, "Hello",3.5, True)
print(t)


# question no 6
lst=[1,2,3,4]
totle=sum(lst)
print("sum")


# question no 7
lst=[10,5,20,8]
print("Largest:", max(lst))


# question no 8
s={1,2,3,}
s.add(4)
s.update([5,6])
print(s)


# question no 9
arr=[1,2,3,4,5]
arr.reverse()
print(arr)


# question no 10
arr =[10,20,30,40,50]
# dispiay all items
print(arr)
#Access using index
print("first element:", arr[0])
print("Last element:", arr[4])
