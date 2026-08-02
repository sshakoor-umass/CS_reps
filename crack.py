from string import ascii_letters, digits, punctuation
num = 0

for i in ascii_letters + digits + punctuation:
    for j in ascii_letters + digits + punctuation:
        for k in ascii_letters + digits + punctuation:
            for l in ascii_letters + digits + punctuation:
                print(i,j,k,l)
                num = num + 1
print(num)