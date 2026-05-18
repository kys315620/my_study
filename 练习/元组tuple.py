students = (
    ("S001", "王林", 85, 92, 78),
    ("S002", "李慕婉", 92, 88, 95),
    ("S003", "十三", 78, 85, 82),
    ("S004", "周铁", 88, 79, 91),
    ("S005", "王卓", 95, 96, 89),
    ("S006", "红蝶", 76, 82, 77),
    ("S007", "徐利国", 89, 91, 94),
    ("S008", "许木", 75, 69, 82),
    ("S009", "遁天", 66, 59, 72),
)

print("学号\t\t姓名\t\t语文\t\t数学\t\t英语\t\t总分\t\t平均分")
for s in students:
    total = (s[2] + s[3] + s[4])
    avg = total / 3
    print(f"{s[0]} \t {s[1]} \t {s[2]} \t {s[3]} \t {s[4]} \t {total} \t {avg:.1f}")


english = [s[4] for s in students]
math = [s[3] for s in students]
chinese = [s[2] for s in students]

print(f"英语最高分:{max(english)},英语最低分:{min(english)},平均分:{sum(english)/len(english):.1f}")
print(f"数学最高分:{max(math)},数学最低分:{min(math)},平均分:{sum(math) / len(math):.1f}")
print(f"语文最高分:{max(chinese)},语文最低分:{min(chinese)},平均分:{sum(chinese)/len(chinese):.1f}")

for s in students:
    total = (s[2] + s[3] + s[4])
    avg = total / 3
    if avg >= 90:
       print(f"学号:{s[0]}\t 姓名:{s[1]} \t 平均分:{avg:.1f}\t 评级:优秀")

