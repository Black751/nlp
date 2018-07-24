from nltk.chat.util import Chat, reflections

pairs = [
	[
		r"My name is (.*)",
		["Hello %1"]
	],

	[
		r'hi',
		['hello', 'tomate', 'canard'],
	]	
]


def bot():
	print("Hi how can I help you today ?")
	chat = Chat(pairs, reflections)
	chat.converse()

if __name__ == "__main__":
	bot()