from emora_stdm import DialogueFlow
from Lyric.stdm_test.utils import *

# Update (2022/10/10): Lyric became a menu but it's okay
# oh god I forgot lowercasing stuff h

greetings = {
    'state': 'start',
    "`Hello, my name is Lyric, and welcome to the Hellion's Respite. How may I help you?`": {
        'state' : 'menu', # because I can't think of anything else as of yet lmao oops
        '[{hi, hello, greetings, salutations}]': {
            '`It is a pleasure to meet you. How are you today?`': {
                FEELING_GOOD : {
                    "`That is quite good to hear.`" : 'menu'
                },
                FEELING_BAD : {
                    "`Oh... I am terribly sorry to hear that. Hopefully your day goes by better soon.`" : 'menu'
                },
                'error' : {
                    "`I see. Well, hopefully you will be able to unwind with the drinks and amenities offered here.`" : 'menu'
                }
            }
        },
        '[what, {respite}]' : {
            "`Well, the bartender here would probably be a better person to explain, but the Hellion's Respite here is a tavern, probably one of the better known in the area. Personally, I would say the drinks are a fair price, and you can find a good amount of work around talking to the patrons.`" : 'menu'
        },
        '[{quest, quests, work}]' : {
            "`Well, now, looking for work? I suppose I can give you a task from my list...`"
            "`\nAh, here we are. Currently, there is a farmer seeking help in his farm west from here. His chickens are going missing, it seems. What do you say?`" : {
                AGREE : {
                    "`Well, here are the coordinates, then. Safe travels.`" : 'end'
                },
                DISAGREE : {
                    "`Not to your liking? Very well, then. Unfortunately, I don't have any more quests to offer, so you may have to come back at a different time.`" : 'menu'
                },
                'error' : {
                    "`Oh my, what an enigmatic response. Well, I suppose I will safekeep this for now. Do let me know if you would like to take a look at it again.`" : 'menu'
                }
            }
        },
        '[{bye, see you}]' : {
            "`I hope you have a pleasant day.`" : 'end'
        },
        'error' : {
            "`I am afraid I do not understand. Is there anything that you would like to ask of me?`" : 'menu'
        }
    }
}

lyric = DialogueFlow('start', end_state='end')
lyric.load_transitions(greetings)

if __name__ == '__main__':
    lyric.run(debugging=False)