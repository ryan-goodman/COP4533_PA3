import time

inputFile = open("input.txt")

K = int(inputFile.readline())

charValues = {}

for i in range(K):
    currentLine = inputFile.readline().split(" ")
    currentX = currentLine[0]
    currentV = int(currentLine[1])

    charValues[currentX] = currentV

A = inputFile.readline()
B = inputFile.readline()

inputFile.close()

start_time = time.time()

n = len(A)
m = len(B)

dp = [[0] * (m + 1) for _ in range(n + 1)]

# The first row and first column will be all stay as 0 since
# the maximum possible value with a string of any length and ""
# is 0

for i in range(1, n+1):
    for j in range(1, m+1):
        # We're working by looking at the end of the string
        # So, imagine the last character of both strings matches
        # Then we should just take it and find the largest possible value
        # we can achieve with the remaining characters from each string
        if A[i-1] == B[j-1]:
            dp[i][j] = dp[i-1][j-1] + charValues[A[i-1]]
        
        # If the end characters don't match, one of them has to remain unmatched forever
        # We should choose to drop the one that results in the largest possible value
        # We look at what the largest possible value would be using all characters of B
        # and dropping the last character of A
        # We then do the same but with all characters of A and dropping the last character of B
        # Whichever one gives a greater value is the one we'll take
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

maxVal = dp[n][m]

# Now we backtrack to recreate at least 1 of the optimal sequences

i, j = n, m

sequence = []

# If i or j gets to 0, that means that we have run out of characters
# from string A or B, respectively
while i > 0 and j > 0:
    if A[i-1] == B[j-1]:
        sequence.append(A[i-1])
        i -= 1
        j -= 1
    elif dp[i-1][j] > dp[i][j-1]:
        i -= 1
    else:
        j -= 1

sequence.reverse()

finalSequence = "".join(sequence)

end_time = time.time()

with open("output.txt", "w") as outputFile:
    outputFile.write(f"{maxVal}\n{finalSequence}")

print(f"Run time: {end_time - start_time:.6f} seconds")