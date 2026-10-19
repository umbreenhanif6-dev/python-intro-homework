day = input("What day is it? ").capitalize()
time = input("Is it morning, afternoon, or evening? ").capitalize()

if day =="Sunday":  
     if time == "Morning":
          print("Plan for a brunch and a trip to the mall! ")
     elif time == "Afternoon":
          print("Prepare dinner. ")
     elif time == "Evening":
          print("Go out for a movie. ")
     else:
          print("Invalid time, try again.")	

elif day == "Saturday":
     if time == "Morning":
          print("Go for a morning walk. ")
     elif time == "Afternoon":
          print("Have lunch. ")
     elif time == "Evening":
          print("Go bowling with friends. ")
<<<<<<< HEAD
     else:
           print("Invalid time, try again.")	
=======
          print("Invalid time, try again.")	
>>>>>>> 78481ff (add warmup3 for assignment 3)

elif day ==  "Friday": 
     if time == "Morning": 
          print("Do morning yoga. " )
     elif time == "Afternoon": 
          print("Call a family member. ")
     elif time == "Evening": 
          print("Go out for dinner. ") 
     else:
          print("Invalid time, try again.")	

else:
     print("Relax and read a book! ")