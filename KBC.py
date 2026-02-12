import time
current_time = int(time.strftime('%H'))
if 5 <= current_time < 12 :
    print("Good Morning player ")
elif 12 <= current_time < 17:
    print("Good Afternoon player")
else:
    print("Good Evening player")

ask = input("Are you ready for game(YES/NO):").strip().upper()
if ask == 'YES':
   print(" Okay! Let's play 😊")
   questions = [
    {
    "question" : "How many infinity stones are there in marvel?",
    "options" : ["A)5","B)6","C)4","D)7"],
    "answer" : "B"
  },
  {
      "question" : " What is the real name of Shaktimaan in serial ?",
      "options" : ["A)Gangadhar","B)Yamunadhar","C)Jamunaghar","D)non of these"],
      "answer": "A"
  },
  
  {
      "question" : "What is name of the BATMAN city ?",
      "options" :["A)Gotham","B)New York","C)Paris","D)London"],
      "answer" : "A"
  },
  {
      "question" : "What is the name of Nobita 's Mother ?",
      "options" : ["A)TAMAO NOBI","B)EMIKO NOBI","C)TAMAKO NOBI","D)YAMIKO NOBI"], 
      "answer" : "C"
  },
  
 ]
   prize_money = [5000,10000,50000,100000]
   total_prize = 0 
   for i,q in enumerate(questions):
    print("\nQuestion ",i+1,":",q["question"])
    for option in q["options"]:
        print(option)

    answer = input("Enter your answer(A,B,C,D): ").strip().upper()    
    if answer == q["answer"] :
     print("Correct Answer ! You Won: ₹",prize_money[i])
     total_prize += prize_money[i]
    else:
     print("wrong Answer!Game over")   
     break
    print(" Total money you won : ₹",total_prize)
else:
   print("okay! play next time 😊:")
   
