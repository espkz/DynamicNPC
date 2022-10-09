from emora_stdm import DialogueFlow

# utilizing the test chatbot from way down yonder and adjusting it bit by bit
# Notes: literally just copy-pasted lmao we'll get there
chatbot = DialogueFlow('start')
transitions = {
    'state': 'start',
    '`Hello, my name is Lyric.`': {
        '#INT(Hi! How are you?, How are you doing?)': {
            '"How are you?"': {
                'state': 'ask-mood',

                '[{good, great, okay, fine, fantastic}]': {

                    '"That\'s great! '

                    'How was your day?"': {
                        'state': 'day',

                        '[{good, great, okay, fine, fantastic}]': {

                            '"That\'s good to hear! '
                            'What happened?"': {
                                'error': 'music-subconvo'
                            }
                        },
                        '[{bad, horrible, awful, terrible}]': {

                            '"Oh no! '
                            'What happened?"': {
                                'error': 'music-subconvo'
                            }
                        },
                    },
                },

                '[{bad, horrible, awful, terrible}]': {

                    '"Oh no! I\'m sorry to hear that. '
                    'How was your day?"': {
                        'state': 'day',

                        '[{good, great, okay, fine, fantastic}]': {

                            '"That\'s good to hear! '
                            'What happened?"': {
                                'error': 'music-subconvo'
                            }
                        },
                        '[{bad, horrible, awful, terrible}]': {

                            '"Oh no! '
                            'What happened?"': {
                                'error': 'music-subconvo'
                            }
                        },
                    },
                },

                'error': {

                    '"I don\'t understand! "': 'start'
                }
            }
        },
        '#INT(Tell me your favorite type of music.)': {

            'state': 'music-subconvo',

            '"Well, what kind of music do you like?"': {
                '[{jazz, classical, pop, rock, metal, electronic, country, hip hop, techno, country}]': {
                    '"Me too! '
                    'Who\'s your favourite artist?"': {
                        'error': {
                            '"Well you should listen to them! Bye for now!"': 'end'
                        }
                    },
                },
                'error': {
                    '"I\'ve never heard of that before! '
                    'Who\'s your favourite artist from that kind of music?"': {
                        'error': {
                            '"Well you should listen to them! Bye for now!"': 'end'
                        }
                    },
                }
            }
        }
    }
}

chatbot.load_transitions(transitions)

if __name__ == '__main__':
    chatbot.run()