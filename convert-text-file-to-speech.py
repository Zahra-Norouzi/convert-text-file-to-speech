from gtts import gTTS

with open("input.txt", "r") as file:
    text = file.read()

text_to_speech = gTTS(text=text, lang="en")
text_to_speech.save("output.mp3")