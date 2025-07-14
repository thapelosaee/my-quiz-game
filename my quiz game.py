print("welcome to my quiz game!! 😍😍😍")

playing = input("would you like to play my quiz game?  yes or no: ").lower()

if playing != "yes":  # != means is not
    print("weak... 💀")
    quit()

print("okay let's play 😈")   

score = 0

answer = input("1. what does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("you're correct!!👌 ")
    score += 1
else:
    print("nah buddy, it's *central processing unit* 🧠💻 ")

answer = input("2. what does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("you're correct!!👌 ")
    score += 1
else:
    print("nope! it's *graphics processing unit*, not your guess 💀 ")

answer = input("3. what does RAM stand for? ")
if answer.lower() == "random access memory":
    print("you're correct!!👌 ")
    score += 1
else:
    print("wrong move! it's *random access memory* 😬 ")

answer = input("4. what does LAN stand for? ")
if answer.lower() == "local area network":
    print("you're correct!!👌 ")
    score += 1
else:
    print("nah fam, its *local area network* 🌐 ")

answer = input("5. what is thapelo's favourite color? ")
if answer.lower() == "gray":
    print("you're correct!!👌 ")
    score += 1
else:
    print("bro it's GRAY... how do you not know this? 😭 ")

answer = input("6. what does CC stand for (in coding squad)? ")
if answer.lower() == "code collectives":
    print("you're correct!!👌 ")
    score += 1
else:
    print("nope! it's *code collectives* stay in the loop 😪 ")

answer = input("7. what do you call a computer inside a computer? ")
if answer.lower() == "virtual machine":
    print("you're correct!!👌 ")
    score += 1
else:
    print("ouch... its called a *virtual machine* 🤖 ")

answer = input("8. what does HTML stand for? ")
if answer.lower() == "hypertext markup language":
    print("correct!!🔥 ")
    score += 1
else:
    print("nope 😭 its *hypertext markup language*, not made up letters ")

answer = input("9. is python in the top 3 most in demand programming languages? (yes or no) ")
if answer.lower() == "yes":
    print("correct!!🐍 ")
    score += 1
else:
    print("yea bro you cooked fr, Python is 🔥🔥🔥 it's in the top 3 most in demand languages ")

answer = input("10. what is the output of: print(3 * '7') ? ")
if answer == "777":
    print("you're sharp!!⚔️ ")
    score += 1
else:
    print("nah that's not it chief 😪 it multiplies the string, not math ")

answer = input("11. what keyword defines a function in Python? ")
if answer.lower() == "def":
    print("correct!!🧠 ")
    score += 1
else:
    print("nope! its 'def' dont guess it 😤 ")

answer = input("12. which operator checks if two values are equal? ")
if answer == "==":
    print("correct!!⚖️ ")
    score += 1
else:
    print("wrong! its == not = 😩 they're not the same bro ")

answer = input("13. what's the result of 10 % 3? ")
if answer == "1":
    print("you got it!! 🔢 ")
    score += 1
else:
    print("nah bro that's remainder math 💀 its 1, stay sharp ")

answer = input("14. what's the first index of a list in Python? ")
if answer == "0":
    print("correct!! 😎 ")
    score += 1
else:
    print("nah fam Python starts at 0 😵 index from the ground up ")

answer = input("15. what data type is used for text? ")
if answer.lower() == "string":
    print("you're right!! 💬 ")
    score += 1
else:
    print("wrong! it's string 💢 you just got typed out ")

answer = input("16. which loop is used for repeating code while a condition is true? ")
if answer.lower() == "while":
    print("correct!! 🔁 ")
    score += 1
else:
    print("nope! 'while' is the loop you're looking for 😩 ")

answer = input("17. what's the correct way to start a comment? ")
if answer == "#":
    print("yes sir!! 💭 ")
    score += 1
else:
    print("nope. comments start with #, not vibes 😤 ")

answer = input("18. what built-in function returns the length of a string? ")
if answer.lower() == "len":
    print("you got it!! 📏 ")
    score += 1
else:
    print("nah it's 'len' bro, not 'length' or anything else 😵 ")

answer = input("19. what keyword is used to import a module? ")
if answer.lower() == "import":
    print("correct!! 📦 ")
    score += 1
else:
    print("you missed that one 😵 the keyword is *import*, stop guessing bro ")

# Final score
print(f"\n🔥 You got {score} out of 20 correct 🔥")

if score == 19:
    print("PERFECT!!! 💯 YOU'RE A PYTHON DEMON 🐍💀")
elif score >= 15:
    print("not bad at all 👊")
elif score >= 10:
    print("decent, but sharpen up and stop playing 😐")
else:
    print("weak... start training bro aint no ☠️")

       
print("thanks for playing my quiz game! 😍")