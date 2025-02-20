with open('codingal.txt','w')as file:
  file.write("Hy my name is sankerthan")
file.close()

with open('codingal.txt','r')as file:
  data = file.readlines()
  for line in data:
     word=line.split()
     print(word)
file.close()

file=open('codingal.txt','a')
file.write("benzema")
file.close()

file=open('football.txt','x')