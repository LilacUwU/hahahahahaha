meme_dict = {
    "smile": "посмішка",
    "happy": "счасливий",
    "sad": "сумний",
    "funny": "смішний",
    "angry": "злий",
    "tasty": "смачний",
    "wet": "мокрий",
    "dry": "сухий",
    "famous": "відомий",
    "hand": "рука",
}

word = input("Впиши слово яке не знаеш ")
if word in meme_dict.keys():
    print(f"Слово {word} означає {meme_dict[word]}")
else:
    print("Я не знаю такого слова")
