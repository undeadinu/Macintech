# encoding: utf-8
# @MICKEY TODO: Comment and stuff
import sys, getopt
from random import randint

class Namer:
	@staticmethod
	def vaporname(song):
		name_length = randint(1,19)
		with open ("src/jap-chars") as myfile:
			charlist = myfile.read()
			charlist_length = len(charlist)

		name = ''
		songused = False
		for i in range(0,name_length):
			if ((randint(0,9) == 9) and not (songused)):
				name +=  Namer.songtitlepiece(song)
				songused = True
			else:
				rand_char = randint(0,((charlist_length-1)/3)-1)*3
				name += charlist[rand_char] + charlist[rand_char + 1] + charlist[rand_char + 2]

		return name

	@staticmethod
	def songtitlepiece(song):
		words = song.split()
		longest_word = " ";
		longest_length = 0;
		for j in range(len(words)):
			if ( len(words[j]) > longest_length ):
				longest_word = words[j]
				longest_length = len(words[j])
			elif (len(words[j]) == longest_length ):
				if ( randint(0,1) == 1):
					longest_word = words[j]
		return longest_word

