# -*- coding: utf-8 -*-
from collections import deque

def solution(string):
    orders = string.split(" ")
    latest = deque()    # latest 5 orders

    for order in orders:
        try:
            latest.remove(order)
        except ValueError:
            pass

        # keep only 5 latest order
        if len(latest) == 5:
            latest.pop()

        latest.appendleft(order)
        print(" ".join(latest))

solution("우리 우리 우리 하나 우리 국민 삼성 농협 농협 농협 국민 저축")