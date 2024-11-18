score = int(input("enter your score\n"))
if score >= 90 and score <= 100:
    print("your score is -> grade A")
elif score >= 80 and score<= 89:
    print("your score is -> grade B")
elif score >= 70 and score <= 79:
    print("your score is -> gread C")
elif score >= 60 and  score <= 69:
    print("your score is -> gread D")
elif score >=100:
    print("your cant get any score")
else :
    print ("your fail")