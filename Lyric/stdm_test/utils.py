from emora_stdm import Macro


FEELING_GOOD = '{[not, bad], '\
        '[! -not {' \
        'good, great, fantastic, fine, okay, ok, perfect, amazing, splendid' \
        '}]}'

FEELING_BAD = '[{' \
                'bad, badly, terrible, terribly, mess, ' \
                'hard, horrible, horribly, awful, tough, ' \
                '[!not, {good, great, well, happy, ok, okay}], '\
                '[!not, been, {good, great, well, happy, ok, okay}], '\
                'stressed, managing poorly, managing badly, poorly, '\
                'overwhelmed, tired, meh, blah, sucks, '\
                'struggle, struggling, sad, rough, failure, fail, hate, hopeless, depressed}]'

AGREE = '{[not, bad], '\
        '[! -not {' \
        'sure, i know, i do, i am, ok, okay, okie, ' \
        '[{yes, yeah, yea, yah, yep, yup, think so, i know, absolutely, exactly, precisely, ' \
        'certainly, surely, definitely, probably, true, of course, right}]' \
        '}]}'

DISAGREE = '{' + ', '.join([
    '[{no, nay, nah, na, not really, nope, no way, wrong}]',
    '[{absolutely, surely, definitely, certainly, i think} not]',
    '[-know, i, do, not]',
    '[i, am, not]',
    '[not true]'
]) + '}'

DONT_KNOW = '[{' \
            'idk, meh, eh, blah,' \
            'dont know,do not know,unsure,[not,{sure,certain}],hard to say,no idea,uncertain, ' \
            '[!no {opinion,opinions,idea,ideas,thought,thoughts,knowledge}],' \
            '[{dont,do not}, have, {opinion,opinions,idea,ideas,thought,thoughts,knowledge}],' \
            '[!{cant,cannot,dont} {think,remember,recall}]' \
            '}]'