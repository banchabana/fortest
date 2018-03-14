#!/usr/bin/env python
#! -*- coding:utf-8  -*-
import random #daorusuijishu
Age=random.randrange(10)
for i in range(3):
    if i < 2:
        guess_number=int(input("Please input the age of my dog you guess:\n"))
        if guess_number > Age:
            print("The age you guess is a little big, think smaller!\n")
        elif guess_number < Age:
            print("The age you guess is a little small, think bigger!\n")
        else:
            print("Bingo, you got the number, congratulations!\n")
            break
    else:
        guess_number=int(input("Please input the age of my dog you guess:\n"))
        if guess_number == Age:
            print("Bingo, you got the number, congratulations!\n")
        else:
            print("Oh, you just got bad luck, come to try again, you can do it! The actual age of my dog is %d...\n" %Age)

            

    
