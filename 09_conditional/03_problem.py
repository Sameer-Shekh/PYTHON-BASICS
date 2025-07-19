# GRADE CALCULATOR
# ASSIGN A LETTER GRADE BASED ON STUDENT'S SCORE : A(90-100) , B(80-89) , C(70-79) , D(60-69) , F(BELOW 60)

score = 188

if score >=101:
    print("Please Verify Your Number Again")
    exit()
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >=60:
    grade = 'D'
else:
    grade = 'F'

print("Your Grade Based On Your Number",grade)