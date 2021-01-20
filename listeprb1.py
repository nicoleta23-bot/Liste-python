x=[1,3,4,10,-12,6]
print('Lista initiala=', x)
y=sorted(x)
print('Lista sortata crescator=', y)
x.sort(reverse=True)
print(x)
print(len(x))
x=[1,3,4,10,-12,6]
print('Lista initiala=', x)
print(max(x))
print(min(x))
print(x+[111])
x[2]=222
print(x)