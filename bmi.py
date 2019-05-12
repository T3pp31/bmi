def bmi(height,weight):
    return weight/height**2
print("‚ ‚È‚½‚Ìbmi‚ğ‹‚ß‚Ü‚·")
h=float(input("g’·‚ğ“ü—Í‚µ‚Ä‚­‚¾‚³‚¢(m)"))
w=int(input("‘Ìd‚ğ“ü—Í‚µ‚Ä‚­‚¾‚³‚¢(kg)"))
print("‚ ‚È‚½‚Ìbmi‚Í%.4f‚Å‚·"%bmi(h,w))