# 1  
# a)

tuple = ("早安", "午安", "晚安", "我是蘇奕哲")

print("第二個元素:",tuple[1])

print("最後一個元素:",tuple[-1])

#==============================================================================

# 1
# b)


old_tuple = (1, 2, 3, 4)


new_list = list(original_tuple)


new_list.append(5)  
new_list.extend([6, 7, 8])  


updated_tuple = tuple(new_list)


print(f"原始的tuple: {old_tuple}")
print(f"更新後的tuple: {updated_tuple}")


#==============================================================================

#2

import random

def guess_number():

    target_number = random.randint(1, 100)
    guess = None
    
    print("歡迎來到猜數字遊戲！請猜1到100之間的數字。")
    

    while guess != target_number:

        try:
            guess = int(input("請猜一個數字："))
        except ValueError:
            print("請輸入一個正整數。")
            continue


        if guess < target_number:
            print("太低了。再試一次！")
        elif guess > target_number:
            print("太高了。再試一次！")
    

    print(f"恭喜答案是 {target_number}。")


guess_number()


    
