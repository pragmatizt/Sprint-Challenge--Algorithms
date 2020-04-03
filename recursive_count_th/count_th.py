'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # DELETE: create counter
    # DELETE: counter = 0

    # If the word is less than 2, then throw it away
    if len(word) < 2:
        return 0
    # Elif "th" is in beginning of slice:
    elif word[:2] == 'th':
        # add one, continue searching through word
        # we take out the first letter of word, then repeat the search for 'th'
        # DELETE: counter += 1
        # MAKES SENSE.  For every 'th' we find, we mark 1, then sum at end
        return 1 + count_th(word[1:])
    # Otherwise, if th is not in slice
    # you return -- take first letter out, and keep slicing through
    # Without a "1" to return to be summed up.
    else:
        return count_th(word[1:])

