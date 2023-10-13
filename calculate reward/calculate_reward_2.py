def calculate_reward_2(role, point):


    if role == "người chơi thường":
        if point >= 1000:
            return 1000


    elif role == "vip1":
        if point >= 100 and point < 1000:
            return 1000
        elif point >= 1000:
            return 5000


    elif role == "vip2":
        if point >= 0 and point < 10:
            return 1000
        elif point >= 10 and point < 100:
            return 5000
        elif point >= 100 and point < 1000:
            return 10000
        elif point >= 1000:
            return 50000


    return 0
