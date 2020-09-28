def read_input():
    prices = [int(x) for x in input().split()]
    string = input()
    
    return prices, string

def soution(prices, string):
    """
    1. 가격이 저렴한 꽃을 먼저 교체하도록 고려
    """
    red, blug, green = prices
    


if __name__ == "__main__":
    prices, string = read_input()
    solution(prices, string)