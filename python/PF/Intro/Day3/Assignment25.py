#PF-Tryout

#debug the below code
counter1=0
counter2=5
counter3=0
while(counter1 < 5): 
  star=""
  counter3 = counter2
  while(counter2>counter1):
     star=star+ "*"
     counter2-=1
  print(star)
  counter2 = counter3
  counter1+=1

  
  