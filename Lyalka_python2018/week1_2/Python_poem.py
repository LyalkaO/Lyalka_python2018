import this
poem = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea."""

# task 1. print poem as a string:
print(poem)

# task 2: count nunber of better, never, is.
sep_w = list(poem.split())
print(sep_w)
better = sep_w.count('better')
never = sep_w.count('never')
w_is = sep_w.count('is')
print('The count of better is:', better, 'never:', never, 'is:', w_is)

# task 3. Print ht poem in upper case
upper_case_poem = poem.upper()
print(upper_case_poem)

# task 4. substitute i with &
subst_i = poem.replace('i', '&')
print(subst_i)








