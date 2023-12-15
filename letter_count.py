import json
import urllib.request
import time
from threading import Thread,Lock


finished_count = 0

def letter_count(url,frequency,mutex):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    req = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(req)
    txt = str(response.read())
    mutex.acquire()
    for l in txt:
        letter = l.lower()
        if letter in frequency:
            frequency[letter] += 1
    
    global finished_count
    finished_count += 1
    mutex.release()



def main():
    frequency = {}

    mutex = Lock()

    for c in "abcdefghijkmnopqrstuvwxyz":
        frequency[c] = 0
    start = time.time()
    
    
    for i in range(1000,1020):
        Thread(target=letter_count,args=(f"https://www.rfc-editor.org/rfc/rfc{i}.txt",frequency,mutex)).start()
        #letter_count(f"https://www.rfc-editor.org/rfc/rfc{i}.txt",frequency)

    
    
    while True:
        mutex.acquire()
        if finished_count == 20:
            break
        mutex.release()
        time.sleep(0.5)
    end = time.time()

    print(json.dumps(frequency,indent=4))
    print("Done , time taken :",end - start)

    


main()