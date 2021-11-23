fruits =['apple', 'Banana','Pineapple',3]
animals = [
'Lion',
'Tiger',
'Rabbit',
3,
]
clubs =[
'ManU',
'ManC',
 3,
]

for i in range(1,16+1):
    if i%15==0:
         print("Fizz buzz")
    if i%3 == 0:
         print("fizz")
    elif i%5 == 0:
         print("buzz")
    else:
         print(i)

