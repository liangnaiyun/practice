"""
寫一個function來印出誰的成績是第二高，如果超過一個人分數都是第二高，請把人名一行一行印出來。

function的參數：
    students：一個二維清單，例如 [['Jerry', 88], ['Justin', 84], ['Tom', 90], ['Akriti', 92], ['Harsh', 90]] 

function的回傳：
    不須回傳

期望的執行結果：
    例如 有個清單是 students = [['Jerry', 88], ['Justin', 84], ['Tom', 90], ['Akriti', 92], ['Harsh', 90]]  
    second_highest(students)  的執行結果應該要印出：
    Tom
    Harsh

重要提示：
不一定要，但可以使用sorted這個function來排列清單，

例如 
x = [3, 1, 4, 5, 2]
x = sorted(x) # 排列x (由小到大)
print(x) # 印出 [1, 2, 3, 4, 5]

如果要顛倒排列也可以，只要多加reverse=True

x = [3, 1, 4, 5, 2]
x = sorted(x, reverse=True) # 排列x (由大到小)
print(x) # 印出 [5, 4, 3, 2, 1]
"""


def second_highest(students):
	students = sorted(students, key = lambda s: s[1], reverse=True)
	student = students[1]
	result = [s[0] for s in students if s[1] == student[1]]
	for r in result:
		print(r)


second_highest([['Jerry', 88], ['Justin', 84], ['Tom', 90], ['Akriti', 92], ['Harsh', 90]])