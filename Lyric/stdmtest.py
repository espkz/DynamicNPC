from emora_stdm import DialogueFlow

# utilizing the test chatbot from way down yonder and adjusting it bit by bit
# Notes: literally just copy-pasted lmao we'll get there
greetings = {
    'state': 'start',
    '`Hello, my name is Lyric.`': {
        '[{hi, hello, greetings, salutations}]': {
            '`It is a pleasure to meet you. How are you today?`': {
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

lyric = DialogueFlow('start')
lyric.load_transitions(greetings)

if __name__ == '__main__':
    lyric.run()