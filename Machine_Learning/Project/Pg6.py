emoji = {"happy" : "😀", "sad" : "🥲", "angry" : "😒", "love" : "🥰"}
message = input ("Enter the feeling: ")

words = message.split(" ")
new_message = ""

for word in words:
    if word in emoji:
        new_message += emoji[word] + " "
    else:
        new_message += word + " "

print("Converted message: " + new_message)
