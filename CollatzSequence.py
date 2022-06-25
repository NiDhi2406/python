import sys, time

print('''Rules:
      1). If n is even, the next number n is n /2.
      2). If n is odd, the next number is n*3+1.
      3). If n is 1, stop. Otherwise repeat.''')
print("Enter a starting number (greater than 0) or QUIT: ")
response = input('> ')
if not response.isdecimal() or response == '0':
    print("You must enter an integer greater than 0.")
    sys.exit()
n = int(response)
print(n, end ='', flush = True)
while n != 1:
    if n%2 == 0:
        n = n//2
    else:
        n = 3 * n + 1
    print(', ' + str(n), end = '', flush = True)
    time.sleep(0.1)
print()