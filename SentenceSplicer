#Ask the user to enter a sentence
sentence = input("Please enter a complete sentence here.")

#Calculate the length
length = len(sentence)

#find the start and the end parts of the sentence
start = round(length * 0.25)
end = round(length * 0.75)

print(sentence[start:end])

#Split the sentence at its spaces, then calculate the new length of the sentence
sentence_split = sentence.split(" ")
length_split = len(sentence_split)

start_split = round(length_split * 0.25)
end_split = round(length_split * 0.75)

sentence_split = sentence_split[start_split:end_split]

#Use a variable to put the sentence back together and then print the middle of the users sentence
tape = " "
sentence_split = tape.join(sentence_split)

print(sentence_split)
