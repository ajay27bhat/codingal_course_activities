# Exam Eligibility Check using Nested If-Else

attendance = float(input("Enter attendance percentage: "))
fees_paid = input("Have you paid the exam fees? (yes/no): ")

if attendance >= 75:
    if fees_paid.lower() == "yes":
        print("You are eligible to write the exam.")
    else:
        print("You are not eligible because the exam fees are not paid.")
else:
    if attendance >= 65:
        print("Attendance is below 75%. Apply for condonation if allowed.")
    else:
        print("You are not eligible due to low attendance.")