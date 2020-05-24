import pyttsx3

engine = pyttsx3.init()

engine.say("Welcome to my text-to-speech program. Type the text you would like to convert below")
engine.runAndWait()

while True:
	text = input('===>')
	engine.say(text)
	engine.runAndWait()