with open('input.txt', 'r') as f:
    lista1=list(eval(f.read()))
    print(lista1)
lista2=sorted(lista1)
print(lista2)
lista3=sorted(lista1, reverse=True)
print(lista3)
y=len(lista1)
print('Lungimea listei este:', y)
print('Elementul maxim este:', max(lista1))
print('elementul minim din lista este:', min(lista1))
print(lista1+[111])
lista1[2]=222
print(lista1)
with open('output.txt', 'w') as f:
    f.write(f' Lista: {lista1} \n')
    f.write(f' Lista sortata in ordine crescatoare: {lista2} \n')
    f.write(f' Lista sortata in ordine descrescatoare: {lista3} \n')
    f.write(f' Lungimea listei este: {y} \n')
    f.write(f' Elementul maxim este: {max(lista1)} \n')
    f.write(f' Elementul minim este: {min(lista1)} \n')
    f.write(f' Lista cu extinderea 111: {lista1+[111]} \n')
    f.write(f' Lista cu extindere pe pozitia a 2-a: {lista1[2]=222} \n')