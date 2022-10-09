# utilizing framework from https://github.com/espkz/Dev_AIChatbot_NLP/blob/main/Chatbot.py

import torch

#class of the npc
class NPC():
    def __init__(self, name):
        print("----- Starting up", name, "-----")
        self.name = name



if __name__ == "__main__":
    ai = NPC(name="Lyric")
    done = False
    print("Hello, my name is " + ai.name + "!")
    while not done:
        message = input().lower()
        x = message.split()
        if "hi" in x:
            print("Hello, how are you doing?")
            message = input().lower()
            x = message.split()
            if "good" or "great" or "fine" or "okay" in x:
                print("That's great! 'Tis a lovely day today.")
            else:
                print("I'm terribly sorry to hear that. Hopefully your day goes by better than how you feel now.")
        elif "exit" in x:
            print("Okay, bye!")
            done = True
        else:
            print("SAVE MY HOME IN THE OCEAN") #props if you get the reference
