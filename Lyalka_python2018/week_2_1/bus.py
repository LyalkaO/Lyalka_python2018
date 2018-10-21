# def enough(cap, on, wait):
#     if cap-on >= wait:
#         return 0
#     else: cap-on-1 < wait
#     return wait-cap+on

def enough(cap, on, wait):
    return 0 if cap-on >= wait else wait-cap+on


