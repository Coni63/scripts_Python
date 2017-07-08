import certifi
import urllib3
import io
import json

http = urllib3.PoolManager(
    cert_reqs='CERT_REQUIRED', # Force certificate check.
    ca_certs=certifi.where(),  # Path to the Certifi bundle.
)

# You're ready to make verified HTTPS requests.
try:
    r = http.request('GET', 'https://api.twitch.tv/kraken/teams/')
    #test = json.load(r)
    #str_response = r.readall().decode('utf-8')
    test = json.loads(r.data.decode('utf8'))
    print(test['teams'])
    for each in test['teams']:
        print(each)

    #print(r.status)
    #print(r.headers['server'])
    #for chunk in r.stream():
    #    print(chunk)
    r.close()
except urllib3.exceptions.SSLError as e:
    # Handle incorrect certificate error.
    print('Error')