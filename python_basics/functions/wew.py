def square(number):
    return number * number



print(square(10))


def emoji_converter(message):
    words = message.split(" ")
    emojis = {
        ":)": "wow",
        ":(": "longkot"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


message = input(">")
print(emoji_converter(message))