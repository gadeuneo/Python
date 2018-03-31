# baern.py
# Input corpus in command line
# Output random sentances

from sys import *
from random import *

def corpusWordList(corpus):
	"""Reads a file and creates a list containing all of the words in the 
	in order, with capitalization and punctuation retained"""
	
	inputFile = open(corpus)
	corpusText = inputFile.read()
	corpusList = corpusText.split()
	inputFile.close()
	
	return corpusList

def connectionDict(corpusList):
	"""Input list of words in a corpus in order
	Output a dictionary containing each word as a key and
	all of the words that follow it as the key's values"""
	
	connectionD = {}
	
	# Loop through all but the last word in corpusList
	# and add them to the dictionary connectionD
	for indx in range(len(corpusList) - 1):
		if corpusList[indx] not in connectionD:
			
			# Adds the word as a key to connectionD
			# and sets the key's value equal to a list
			# containing the next word in the corpus
			connectionD[corpusList[indx]] = [corpusList[indx + 1]]
		
		# If the word is already in the dictionary,
		# adds the next word as a new value of the key
		else:
			connectionD[corpusList[indx]] += [corpusList[indx + 1]]
	
	return connectionD

def startWords(corpusList):
	"""Input list of words in corpus in order
	Outputs list of start words in corpus"""
	
	startW = [corpusList[0]]
	
	# Loop through each word to determine if it starts a sentence
	for index in range(1, len(corpusList)):
		
		# Adds start words not already in the list
		priorW = corpusList[index - 1]
		if ("." in priorW or "!" in priorW or "?" in 
		priorW) and (corpusList[index] not in startW):
			startW.append(corpusList[index])
	
	return startW

def sentenceConstruction(connectionD, startW):
	"""Input connection dictionaty and start words
	Output sentence"""
	
	# Getting first word and adding it to sentence list
	sentence = [choice(startW)]
	
	# Looping to add remaining words to sentence
	noStopChar = True
	while (noStopChar or len(sentence) < 4) and len(sentence) < 50:
		
		# Add another random word to the sentence
		wordKey = sentence[-1]
		nextWord = choice(connectionD[wordKey])
		sentence.append(nextWord)
		
		# Check whether the sentence list contains a
		# stop character after the first 3 words
		if (("." in nextWord) or ("!" in nextWord) or ("?" in nextWord)) and len(sentence) > 3:
			noStopChar = False
	
	# Return the sentence as a string
	return " ".join(sentence)

def sentenceLoop(connectionD, startW):
	"""Creates random sentences for user
	'c' to continue or 'q' to quit"""
	
	# Creates a new sentence using a while loop as
	# long as the user enters 'c'
	# and quits when the user enters 'q'
	userInput = "c"
	while userInput != "q":
		sentence = sentenceConstruction(connectionD, startW)
		print("Generated sentence:", sentence)
		userInput = input("Enter 'c' to continue or 'q' to quit: ")
		while userInput != "c" and userInput != "q":
			userInput = input("Enter 'c' to continue or 'q' to quit: ")

def main():
	""" Create a random sentence from a corpus in the command line"""

	# Create a list of words in corpus, a connection
	# dictionary, and a list of start words
	wordList = corpusWordList(argv[1])
	connectionDictionary = connectionDict(wordList)
	startWordList = startWords(wordList)
	
	# Create and print the random sentence
	sentenceLoop(connectionDictionary, startWordList)

main()
