def bmi(height,weight):
    return weight/height**2
print("���Ȃ���bmi�����߂܂�")
h=float(input("�g������͂��Ă�������(m)"))
w=int(input("�̏d����͂��Ă�������(kg)"))
print("���Ȃ���bmi��%.4f�ł�"%bmi(h,w))