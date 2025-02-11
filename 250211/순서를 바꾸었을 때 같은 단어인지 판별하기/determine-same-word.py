word1 = input()
word2 = input()

# Write your code here!
word1 = sorted(list(word1))
word2 = sorted(list(word2))
print("Yes" if word1 == word2 else "No")