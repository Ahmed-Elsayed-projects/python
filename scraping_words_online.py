def scrape_vocab(word, access_failed):
    import urllib.request
    from bs4 import BeautifulSoup

    url = "https://www.vocabulary.com/dictionary/" + word
    htmlfile = urllib.request.urlopen(url)
    soup = BeautifulSoup(htmlfile, 'lxml')

    def scrape_content(class_name,access_failed):
        meaning = soup.find(class_=class_name)
        try:
            meaning = meaning.get_text()
            done = True
            return meaning, access_failed, done
        except AttributeError:
            access_failed.append(word)
            done = False
            return meaning, access_failed, done
    the_meaning, access_failed, is_done = scrape_content('short', access_failed)
    if is_done:
        return the_meaning


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
    return


failed = []
list = ['vocation', 'monograph', 'cosy', 'treaty', 'predecessor', 'sophisticated', 'prose', 'malevolent',
              'wickedness', 'motive', 'scanty', 'eminently', 'dreary', 'mimic', 'forerunner', 'meticulous', 'pierced',
              'tall', 'play', 'obviously']
with open(r'C:\Users\Hosam\Documents\new_file.csv', 'w', newline='') as file:
    import csv
    writer = csv.writer(file)
    for word in list:
        from os.path import join
        word_meaning = scrape_vocab(word, failed)
        sound_url = f"https://ssl.gstatic.com/dictionary/static/pronunciation/2021-03-01/audio/{word[0] + word[1]}/{word}_en_gb_1"
        path = join(r'C:\Users\Hosam\AppData\Roaming\Anki2\User 1\collection.media', f'{word}.mp3')
        downloadFile(sound_url, path)
        writer.writerow([word, word_meaning, f"[sound {word}.mp3]", "en_vocab"])

print(failed)