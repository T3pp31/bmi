def bmi(height,weight):
    return weight/height**2
print("あなたのbmiを求めます")
h=float(input("身長を入力してください(m)"))
w=int(input("体重を入力してください(kg)"))
print("あなたのbmiは%.4fです"%bmi(h,w))