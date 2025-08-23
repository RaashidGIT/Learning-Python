def emoji_replacer(message):
    emoji_dict = {
        "happy": "😊",
        "love": "❤️",
        "sad": "😢",
        "angry": "😡",
        "laugh": "😂",
        "ok": "👌",
        "fire": "🔥",
        "cool": "😎",
        "cry": "😭",
        "star": "⭐"
    }

    words = message.split()
    result = []

    for word in words:
        # Replace word with emoji if found, otherwise keep the original word
        result.append(emoji_dict.get(word.lower(), word))
    
    return " ".join(result)


# Get input from the user and print the converted message
user_message = input("Enter your message: ")
print("Converted message:", emoji_replacer(user_message))
