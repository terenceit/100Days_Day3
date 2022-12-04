# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#Combine and change names to all lower case
combined = name1 + name2
lower_combined = combined.lower()

#Count TRUE
t = lower_combined.count("t")
r = lower_combined.count("r")
u = lower_combined.count("u")
e = lower_combined.count("e")

#Count LOVE
l = lower_combined.count("l")
o = lower_combined.count("o")
v = lower_combined.count("v")
e = lower_combined.count("e")

#Add all together
true = str(t + r + u + e)
love = str(l + o + v + e)

#Combine numbers from True and Love totals
true_love = int(true + love)

if true_love < 10 or true_love > 90:
    print(f"Your score is {true_love}, you go together like coke and mentos.")
elif true_love > 40 and true_love < 50:
    print(f"Your score is {true_love}, you are alright together.")
else:
    print(f"Your score is {true_love}.")