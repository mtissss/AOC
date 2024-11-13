from collections import Counter

data = """zekvierkzferc-treup-ljvi-kvjkzex-789[ekrvz]
zekvierkzfsssserc-treup-ljvi-kvjkzex-789[ekrvz]

"""
results = []
data = data.strip().split("-")
# for word in data.splitlines("/."):
# print(word)
index = len(data)
last_word = data[index - 1]
# print(last_word)
new_data = data[:-1]
sumword = "".join(new_data)


letter_counts = Counter(sumword)
sorted_letters = sorted(letter_counts.items(), key=lambda x: (-x[1], x[0]))
result = "".join([letter for letter, count in sorted_letters[:5]])

print(result)
