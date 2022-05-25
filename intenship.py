# -*- coding: utf-8 -*-
"""
Created on Fri May 20 20:14:22 2022

@author: SKY
"""

guess=""
feedback=""
guess_list=[]
try:
    with open('wordlist.txt') as f:
        for line in f:
            guess_list.append(line.strip())
except FileNotFoundError:
    print("file not found")
    
print("Good started words are: slice,tried,crane")
for guesses in range(6):
    guess=input("\nEnter a word:").lower()
    print("g-green,y-yellow,w-wrong/grey")
    feedback=input("Feedback:").lower()
    if feedback=="ggggg":
        print("well done! Guess",guesses+1)
        break
temp_tuple=tuple(guess_list)


for word in temp_tuple:
    for i in range(5):
        if feedback[i]=='w' and guess[i] in word:
            guess_list.remove(word)
            break
        elif feedback[i]=="g" and guess[i]!=word:
            guess_list.remove(word)
            break
        elif feedback[i]=="y" and guess[i] not in word:
            guess_list.remove(word)
            break
        elif feedback[i]=="y" and guess[i] == word[i]:
            guess_list.remove(word)
            break
        
        
counter = 0
for word in guess_list:
    print(word,end=", ")
    counter-=1
    if counter == 8:
        print("")
        counter=0
        
        
        
        