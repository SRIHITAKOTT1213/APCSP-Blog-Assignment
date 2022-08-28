---
- toc: true
- comments: true
- title: Biology Quiz
- image: /images/aws.png



def question_and_answer(prompt):

    print("Question: " + prompt)
    msg = input()
    print("Answer: " + msg)


import getpass, sys

def question_with_response(prompt):
    print("Question: " + prompt)
    msg = input()
    return msg

questions = 10
correct = 0

print('Hello,' + getpass.getuser())
print("You will be asked " + str(questions) +" questions. ")
question_and_answer("Are you ready to take the Quiz?")


questions = ["What are nitrogenous bases in DNA?", "What does DNA stand for?", "Who was the person who came up with the theory of Evolution?","In what cell does photosynthesis take place?", "What is the name of the relationship in which both sides benefit?", "Glycogen is a polymer of what?", "How many chromosomes do humans have?", "What are the weak bonds between water molecules called?", "What is the division of body cells called?", "What is the division of gametes called?"]
answers = ["Adenine, Guanine, Cytosine, Thymine", "Deoxyribonucleic Acid", "Charles Darwin","Chloroplast", "Mutualism", "Glucose", "46", "Hydrogen bonds", "Mitosis", "Meiosis"]

for i in range(len(questions)):
    rsp = question_with_response(questions[i])
    if rsp == answers[i]:
       print(rsp + " is correct!")

       correct += 1

    else:
       print(rsp + " is incorrect")
       print("The correct answer is " + answers[i])

print(getpass.getuser() + " you scored " + str(correct) +"/10")