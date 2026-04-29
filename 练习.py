# score = int(input("请输入考试成绩： "))
# if  85<=score<100:
#     print("优秀")
# elif(60<=score<85):
#     print("及格")
# elif(0<=score<60):
#     print("不及格")
# else:
#     print("输入的成绩异常,请重新输入")


amounts = float(input("请输入购物车商品总金额："))
if amounts >= 500:
    print(f"您消费已满500元,享受八折优惠,实际消费金额为{amounts*0.8:.2f}")
elif 300 <= amounts < 500:
    print(f"您消费已满300元,享受九折优惠,实际消费金额为{amounts*0.9:.2f}")
elif 100 <= amounts < 300:
    print(f"您消费已满100元,享受九五折优惠,实际消费金额为{amounts*0.95:.2f}")
else:
    print(f'您实际消费金额为{amounts:.2f}')
