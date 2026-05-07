#99乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f"{j} × {i} = {i*j}", end="\t")
#     print()

for h in range(1,9):
    for s in range(1,9):
       if (h+s)%2==0:
           print("■",end="  ")
       else:
           print("▢",end="  ")
    print()
