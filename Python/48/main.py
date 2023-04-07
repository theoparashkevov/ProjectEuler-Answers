# solution variable
sol = 0

# for loop to loop till 1000
for i in range(1, 1001):
    sol += i**i

# printing the last 10 digits
print(str(sol)[-10:])
