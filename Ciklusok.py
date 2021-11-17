#for ciklusok-> magszámlálós (pontosan tudjuk, hányszor kell végrehajtani)
for x in range(5):
    print('Szia')
for y in range(2,11,2):
    print(y)
for z in range(100,10,-10):
    print(z)
#lista
allatok = ['Tigris', 'Malacka', 'Micimackó', 'Füles','Kanga']
for a in allatok:
    print(a, len(a))

#while ciklus -> nem ismert, hányszor kell végrehajtani, addig fut, amíg IGAZ a feltétel
i = 0
while i < 5:
    print('CSá Csumi')
    i=i+1
#1-től 10-ig a számok
j = 1
while j <=10:
    print(j)
    j+=1 #j = j+1

#50-től -50-ig 20-asával csökkenve
k = 50
while k >= -50:
    print(k)
    k -= 20  # k = k-20