'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    # print(word)
    # print(len(word)-1)
    # found it easier to have another function within it because the parent function allows 1 parameter
    def repeat(word, start):
        # have a start and a count of 'th' to keep track
        count = 0
        # if the start is greater than the length of the word, return false
        # must have the -1 to keep it in range
        if start >= len(word) - 1:
            return 0

        # [start] = 't' and [start + 1] = 'h' == 'th'
        if word[start] + word[start + 1] == 'th':
            # if there is a pair, increase the count
            count += 1

        # repeat
        return repeat(word, start + 1) + count
    # must have the repeat
    return repeat(word, 0)
