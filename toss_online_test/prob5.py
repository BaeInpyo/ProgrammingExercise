def solution(ktoss, itoss):
    # convert str to int
    ktoss = [int(x) for x in ktoss.split()]
    itoss = [int(x) for x in itoss.split()]

    net_money = 0
    assert(len(ktoss) == len(itoss))
    answer = []

    for (kmoney, imoney) in zip(ktoss, itoss):
        net_money += kmoney - imoney
        if net_money > 0:
            answer.append(net_money)
            net_money = 0
        else:
            answer.append(0)

    print(" ".join([str(x) for x in answer]))
