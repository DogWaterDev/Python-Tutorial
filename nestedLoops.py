# a nested loop = The "inner loop" will finish all of its iterations before finishing one iteration
# of the outer loops

# like the hands on a clock
# the inner loop (second hand) will finish 60 iterations before the outer loop (minute hand) will iterate once


rows = int(input("How many rows?: "))
columns = int(input("How many columns?: "))
symbol = input("Enter a symbol here: ")

for i in range(rows): # outer loop
    for j in range(columns): # inner loop
        print(symbol, end="")
    print()