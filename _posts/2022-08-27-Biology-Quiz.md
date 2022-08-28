

def question_and_answer(prompt):

    print("Question: " + prompt)
    msg = input()
    print("Answer: " + msg)


import getpass, sys, 

def question_with_response(prompt):
    print("Question: " + prompt)
    msg = input()
    return msg

questions = 10
correct = 0

print('Hello,' + getpass.getuser())
print("You will be asked " + str(questions) +" questions. ")
question_and_answer("Are you ready to take the Quiz?")

rsp = question_with_response("Who was the person who came up with the theory of Evolution")
if rsp == "Charles Darwin":
    print(rsp + " Is correct!")
    correct += 1
else:
    print(rsp + " is incorrect") 
    print("The correct answer is Charles Darwin")

rsp = question_with_response("What does DNA stand for?")
if rsp == "Deoxyribonucleic Acid":
    print(rsp + " is correct!")
    
    correct += 1
else:
    print(rsp + " is incorrect!") 
    print("The correct answer is Deoxyribonucleic Acid")

rsp = question_with_response("What are nitrogenous bases in DNA")
if rsp == "Adenine, Guanine, Cytosine, Thymine":
    print(rsp + " is correct!")
    correct += 1
else:
    print(rsp + " is incorrect!")
    print("The correct answer is Adenine, Guanine, Cytosine, Thymine")

