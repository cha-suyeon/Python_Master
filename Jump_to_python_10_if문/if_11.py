# 다양한 조건 표시 elif
pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
    print("택시 타고 가삼")
else:
    if card:
        print("택시 타고 가삼")
    else:
        print("걸어가삼")