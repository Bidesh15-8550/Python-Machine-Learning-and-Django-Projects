message = input(">")
words = message.split(' ')
emojis ={
    ":)": "đ",
    ":(": "âšī¸",
    ":p": "đ",
    "<3": "â¤ī¸"
}
output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)
