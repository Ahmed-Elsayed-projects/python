# solves quadratic equation by giving a,b,c. Also, a can't be 0
def quadratic_equation(self, a, b, c):
    import math
    step_1 = (b / a) / -2
    step_2 = (step_1 ** 2) - (c / a)
    step_3 = math.sqrt(step_2)
    first_x = step_1 + step_3
    second_x = step_1 - step_3
    return first_x, second_x


# it adds variable to files as many as you want
def variables_adder(filename, the_range, variable_name, content):
    file_name = open(filename, "a")
    for i in range(the_range):
        file_name.write(f"\n{variable_name}{i} = {content}")
    file_name.close()


# it search many files and find the required string
# to see results clearly put it in for loop
def search_inside_files(folder_name, string):
    import os
    line_number = 0
    list_of_results = []
    files = os.listdir(folder_name)
    for file in files:
        with open(f'{folder_name}\{file}', 'r') as read_obj:
            for line in read_obj:
                line_number += 1
                if string in line:
                    list_of_results.append(f"file: {file}, line: {line_number, line.rstrip()}")
    return list_of_results


def add_files(content):
    from os.path import join
    for i in range(1, 32):
        path = join('C:/Users/Hosam/Desktop/example', f"{i}-5-2021.md")
        file = open(path, 'w')
        file.write(content)


# this for encrypting a file you need file's path, and key string which is the algorithm to encrypt with
def encrypting(file_path, key_string):
    import cryptography.fernet
    with open(file_path, 'rb') as original_file:
        original = original_file.read()

    f = cryptography.fernet.Fernet(key_string)
    encrypted = f.encrypt(original)

    with open(file_path, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)


# this one is decrypt file that already encrypted, you need file's path and key string which is the same algorithm
# used to encrypt
def decrypting(file_path, key_string):
    import cryptography.fernet
    with open(file_path, 'rb') as encrypted_file:
        encrypted = encrypted_file.read()

    f = cryptography.fernet.Fernet(key_string)
    decrypted = f.decrypt(encrypted)

    with open(file_path, 'wb') as decrypted_file:
        decrypted_file.write(decrypted)

def scrape_content(class_name, word, soup, access_failed):
    meaning = soup.find(class_=class_name)
    try:
        meaning = meaning.get_text()
        done = True
        return meaning, access_failed, done
    except AttributeError:
        access_failed.append(word)
        done = False
        return meaning, access_failed, done


def downloadFile(AFileName, file_path):
    import urllib.request
    import requests
    # extract file name from AFileName
    # download image using GET
    rawImage = requests.get(AFileName, stream=True)
    # save the image recieved into the file
    with open(file_path, 'wb') as fd:
        for chunk in rawImage.iter_content(chunk_size=1024):
            fd.write(chunk)

def writing_csv():
    import csv
    with open(r'C:\Users\Hosam\Documents\the_file.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for word in words_list:
            x, y = online_dic(word)
            writer.writerow([word, x, y])

def sendmail(self, email, password, message):
    import smtplib
    # manages a connection to an SMTP server
    server = smtplib.SMTP(host="smtp.gmail.com", port=587)
    # connect to the SMTP server as TLS mode ( for security )
    server.starttls()
    # login to the email account
    server.login(email, password)
    # send the actual message
    server.sendmail(email, email, message)
    # terminates the session
    server.quit()