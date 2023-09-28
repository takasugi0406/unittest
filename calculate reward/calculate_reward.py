def calculate_reward(role, point):
    coins = 0

    if role == "người chơi thường":
        if point >= 100:
            coins = 1000

    elif role == "vip1":
        if point >= 100 and point < 1000:
            coins = 1000
        elif point >= 1000:
            coins = 50000

    elif role == "vip2":
        if point >= 0 and point < 10:
            coins = 1000
        elif point >= 10 and point < 100:
            coins = 5000
        elif point >= 100 and point < 1000:
            coins = 10000
        elif point >= 1000:
            coins = 50000

    return coins


# Thử nghiệm chương trình
# role = input("Nhập vai trò của bạn (người chơi thường, vip1, vip2): ")
# point = int(input("Nhập số điểm của bạn: "))

# reward = calculate_reward(role, point)

# if reward > 0:
#     print("Số coins phần thưởng của bạn là:", reward)
# else:
#     print("Bạn không đủ điều kiện nhận thưởng.")