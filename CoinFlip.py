"""3.Write a program that flips a coin 100 times and then tells youthe number of heads and tails.


1.import random 
2.declare a variable n h and t and assign it with value 0 for all
   n=number of repetition
   h=no of tail
   h=no of head
3.run while loop till n(no of repetition ois equal less than 100)
4.generate random no using randint()method in while loop 
5. use if condition under while loop 
    if no is equal to 1 then h=h+1
    else t=t+1    
   increment the number of repetition after every time.
 6.print no of head,h and nof tail, t  

"""
import random  
n=0 #(no of times coin is flipped)
h=0 #(no of head)
t=0 #(no of tail)  
while n<100:# flip the coin for 100 times
      no=random.randint(1,2)
      if no==1:
          h=h+1#(incremeting head when coin turns to head)
     
      else :
          t=t+1#(incerementing tail when coin turn to tail)
     
          
      n=n+1 #(incrementing no of flips)  
print("no of head is",h,"no of tail is ",t)        

   

   