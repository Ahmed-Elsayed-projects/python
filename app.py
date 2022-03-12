import random
choices = ['Head', 'Tail']
print(40*" " + "Head Or Tail")
total_ah =0
total_om =0
def omar_first():
    Omar = 0
    Ahmed = 0
    for i in range(5):
        omar_ans = input("Omar:   ")
        ahmed_ans = input("Ahmed:   ")
        x = random.choice(choices)
        print(f"It was {x}\n")
        if ahmed_ans.upper() == x[0]:
            Ahmed += 1
        if omar_ans.upper() == x[0]:
            Omar += 1
        print(f"""Ahmed = {Ahmed}     Omar = {Omar}\n""")
        return Ahmed, Omar


def Ahmed_first():
    Omar = 0
    Ahmed = 0
    for i in range(5):
        ahmed_ans = input("Ahmed:   ")
        omar_ans = input("Omar:   ")
        x = random.choice(choices)
        print(f"It was {x}\n")
        if ahmed_ans.upper() == x[0]:
            Ahmed += 1
        if omar_ans.upper() == x[0]:
            Omar += 1
        print(f"""Ahmed = {Ahmed}     Omar = {Omar}\n""")
        return Ahmed, Omar
while True:
    Omar = 0
    Ahmed = 0
    f = random.choice([1, 2])
    if f == 1:
        Ahmed, Omar = Ahmed_first()
    if f == 2:
        Ahmed, Omar = omar_first()
    total_ah += Ahmed
    total_om += Omar
    print(f"\n\nAhmed's total = {total_ah}     Omar's total = {total_om}\n\n")
