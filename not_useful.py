from bs4 import BeautifulSoup
import requests

def scrape_audio(word):
    url = "https://www.wordreference.com/fren/" + str(word)
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")    
    try:
        div = soup.find("audio", id="aud0")
        audio_url = div.find('source', src=True)
        return audio_url['src']
    except:
        audio_url = ''

def download(url, file_path):
    from wget import download
    download(url, file_path)

def filter_word(word):
    not_wanted = ['le', 'la', 'les', 'l\'', '(m)', '(f)', 'le/la', '(m/f)']
    out_word = ''
    for i in word.split():
        if i.lower() not in not_wanted:
            out_word += i
    return out_word


for run in range(11):
    with open(f'C:\\Users\\Hosam\\Desktop\\{run}.txt', 'r') as file:
        words_list = file.readlines()
        for i in range(len(words_list)):
            words_list[i] = words_list[i][:-1]


    with open(f'C:\\Users\\Hosam\\Documents\\new_file{run}.csv', 'w', newline='') as file:
        from csv import writer
        writer = writer(file)
        for i in range(int(len(words_list)/2)):
            from os.path import join
            path = join(r'C:\Users\Hosam\AppData\Roaming\Anki2\User 1\collection.media', f'{words_list[i]}.mp3')
            word  = words_list[i]
            print(word)
            try:
                audio_url = 'https://www.wordreference.com' + scrape_audio(filter_word(word).replace(' ', '%20'))
                download(audio_url, path)
                writer.writerow([words_list[int(len(words_list)/2+i)], word, f"{words_list[i]}.mp3", "Fr_vocab"])
            except:
                writer.writerow([words_list[int(len(words_list)/2+i)], word, f" ", "Fr_vocab"])
