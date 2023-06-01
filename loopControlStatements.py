# Loop Control Statements = change a loops execution from its normal sequence

# break = used to terminate the loop entirely
# continue = skips to the next iteration of the loop
# pass = does nothing, acts as a placeholder

while True:
    name = input("Enter your name:") # This loop terminates when you enter a name
    if name != "":
        break

phone_number = "+1 800 423-9789"

for i in phone_number: # this will remove all the dashes and plus signs from the phone number
    if i == "-" or i == "+": # skips to the next index if the current one is - or +
        continue
    print(i, end=" ")

for i in range(1, 21):
    if i == 13: # skips the number 13
        pass
    else:
        print(i)