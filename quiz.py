print("***** Welcome to quiz game ****")

questions = input("Do you want to play? YES / NO. ANS= ")
if questions.upper() != "YES":
    quit()

score = 0

print("Getting Ready ...")

answer = input("What is the full Meaning of ROM? ANS = ")
if answer.lower() == "read only memory":
    print("correct")
    score += 1
else:
    print("wrong")
    print("Right answer is read only memory")

answer = input("Who is the father of computer? ANS = ")
if answer == "Charles Babbage":
    print("correct")
    score += 1
else:
    print("wrong")
    print("Right answer is Charles Babbage")

answer = input("What is the brain of computer system? ANS = ")
if answer.lower() == "cpu":
    print("correct")
    score += 1
else:
    print("wrong")
    print("Right answer is CPU")

answer = input("What is known as a temporary memory in computer system? ANS = ")
if answer.lower() == "ram":
    print("correct")
    score += 1
else:
    print("wrong")
    print("Right answer is RAM")

answer = input("What is half byte called? ANS = ")
if answer.lower() == "nibble":
    print("correct")
    score += 1
else:
    print("wrong")
    print("Right answer is NIBBLE")

answer = input("What does ALU stand for in the context of computers? ANS = ")
if answer.lower() == "arithmetic logical unit":
    print("correct")
    score += 1
else:
    print("wrong")
    print("Right answer is Arithmetic Logical Unit")

answer = input("What does SSD stand for? ANS = ")
if answer.lower() == "solid state drive":
    print("correct")
    score += 1
else:
    print("wrong")
    print("Right answer is Solid State Drive")

print("You got " + str(score) + " questions correct")
print("You got " + str((score/7) * 100) + " %")
