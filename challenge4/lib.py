def try_me(secretword=''):
    '''try different strings to guess the secret 3 letter word, hint, it's something on my desk'''
    if secretword == 'mug':
        return 'Success! Access granted'
    else:
        return 'Fail! No entry'
