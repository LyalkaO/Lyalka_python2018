def areYouPlayingBanjo(name):
    name_l =list(name)
    if name_l[0] is'R':
        return '{} plays banjo'.format(''.join(name_l))
    elif name_l[0] is 'r':
        return '{} plays banjo'.format(''.join(name_l))
    else:
        return '{} does not play banjo'.format(''.join(name_l))