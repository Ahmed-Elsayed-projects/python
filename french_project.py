

with open(r"fr_vocab.txt", 'r') as file2:
    lines = file2.readlines()
    count = 0
    french_list = []
    english_list = []
    errorr = []
    for line in lines:
        count += 1
        if count % 2 == 1:
            french_list.append(line)
        elif count % 2 == 0:
            english_list.append(line)
        else:
            errorr.append(line)

print("french list: ", french_list)
print("english list: ", english_list)
print(errorr)
print('ù', 'é', 'è', 'à', 'ç')



import csv

with open(r'C:\Users\Hosam\Documents\french_vocab.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for i in range(len(lines)-1):
        frword = french_list[i]
        enword = english_list[i]
        writer.writerow([frword.replace('/n', ''), enword.replace('/n', ''), "fr_vocab"])



