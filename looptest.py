# PACK 5
PACKAGE5 = 'sdlad, asdad, sad'

if PACKAGE5:
    ### PACKAGE CONST############################################
    PACKAGE5 = PACKAGE5.replace(', ', ',').split(',')
    p = []
    for PACKAGE5 in PACKAGE5:
        PACKAGE5 = '<p>{}</p>'.format(PACKAGE5)
        p.append(PACKAGE5)
    PACKAGE5 = '\n'.join(p)
    print (PACKAGE5)




