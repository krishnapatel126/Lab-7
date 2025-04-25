text = input("Enter a string: ")

freq = {}

for char in text:
    freq[char] = freq.get(char, 0) + 1

print("Character frequencies:")
for k, v in freq.items():
    print(f"{k}: {v}")
