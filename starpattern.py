# Number of rows for the pattern
n = 5

#inverted pattern
# Outer loop for rows
for i in range(n, 0, -1):
    # Inner loop for printing stars
    print('*' * i)


#normal pattern
for i in range(0,n+1,+1):
    print('*'*i)
