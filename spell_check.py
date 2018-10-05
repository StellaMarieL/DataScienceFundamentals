#Create a list of 'wrong' words and an empty list
wrong = ["bad", "sad", "television", "pen", "telephone", "letter"]
correct = ["good", "happy", "laptop", "paper", "mobile", "email"]

#Ask for a sentence, split at the spaces and enter in the list
sentence = input("In one sentence what did you use 15 years ago?")
sentence = sentence.split(" ")

index = 0

#Create a forloop to check the words and replace them if they are wrong
for word in sentence:
	if word in wrong:
		correct_index = wrong.index(word)
		print(correct_index)
		sentence[index] = correct[correct_index]
			index = index + 1

		sentence = " ".join(sentence)
		print(sentence)
