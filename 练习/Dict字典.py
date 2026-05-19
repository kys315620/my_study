# 1，添加购物车，输入商品名称，商品价格，数量，保存信息到购物车里
# 2，修改购物车，修改购物车商品名称，然后提示输入商品价格数量。输入完成后修改该商品信息
# 3，删除购物车，用户删除购物车的名称，根据名称删除购物车中的商品
# 4，查询购物车，将购物车的信息展示出来，格式为“商品名称：xxx，商品价格：xxx ，商品数量：xxx。”
# 5，退出购物车

shopping_cart = {}
menu = """"
########购物车系统########
#      1.添加购物车      #
#      2.修改购物车      #
#      3.删除购物车      #
#      4.查询购物车      #
#      5.退出购物车      #
########################
"""

print("欢迎来到购物车系统!")

while True:
    # 制作菜单
    print(menu)
    # 执行操作

    choice = int(input("请选择要执行的操作(1-5):"))
    if choice == 1:    # 添加购物车
        name = input("请输入商品名称:")
        price = float(input("请输入商品价格："))
        count = int(input("请输入商品数量："))
        if name in shopping_cart:
            print("该商品已存在，请重新选择")
        else:
            shopping_cart[name] = {"price": price, "count": count}
            print("商品已添加完成!")
    elif choice == 2:  # 修改购物车
        name = input("请输入要修改的商品名称：")
        if name not in shopping_cart:
            print("该商品不存在哦")
        else:
            new_price = float(input("请输入新的商品价格："))
            new_count = int(input("请输入新的商品数量："))
            shopping_cart[name] = {"price": new_price, "count": new_count}
            print("商品已修改完毕!")
    elif choice == 3:  # 删除购物车
        name = input("请输入要删除的商品名称：")
        if name in shopping_cart:
            del shopping_cart[name]
            print("已成功删除!")
        else:
            print("该商品不存在")
    elif choice == 4:  # 查询购物车
        if not shopping_cart.keys():
            print("购物车为空")
        else:
            for name, info in shopping_cart.items():
                print(f"商品名称:{name}，商品价格:{info['price']} ，商品数量:{info['count']}")
    elif choice == 5:  # 退出购物车
        print("退出购物车，欢迎下次光临")
        break
    else:
        print("输入错误，请输入1-5的数字")
