import torch

class NPC():
    def __init__(self, name):
        print("----- Starting up", name, "-----")
        self.name = name



if __name__ == "__main__":
    ai = NPC(name="Lyric")
    done = False
    while not done:
        message = input().lower()
        x = message.split()
        if "hi" in x:
            print("Hello, I'm " + ai.name + "!")
        elif "exit" in x:
            print("Okay, bye!")
            done = True
        else:
            print("HERE WE GO HERE WE GO, GET 'EM UP")
