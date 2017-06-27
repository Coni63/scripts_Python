import json
from urllib import request, parse
import re
import datetime as dt

def request_info(url):
    cle = url_to_key(url)  # 'GGnpIFK3G0Q'
    info = extract_data(cle)
    info['duration'] = YT_duration_to_string(info['duration'])
    info['uploaded'] = YT_published_to_date(info['uploaded'])
    return info

def url_to_key(video_url):
    print("parsing video from {}".format(video_url))
    video_id = ""
    url_data = parse.urlparse(video_url)
    #print(url_data)
    if len(url_data.path) == 12: #case path='/SA2iWivDJiE'
        video_id = url_data.path[1:]
    elif url_data.path[:3] == "/v/":
        video_id = url_data.path[3:]
    elif url_data.path[:7] == "/embed/":
        video_id = url_data.path[7:]
    elif url_data.path == "/watch" or url_data.path == "":
        arr = url_data.query.split('&')
        for each in arr:
            if each[:2] == "v=":
                video_id = each[2:]

    print("Key found : {}".format(video_id))
    return video_id


def YT_published_to_date(published):
    print("parsing published date from {}".format(published))
    result = dt.datetime.strptime(published, '%Y-%m-%dT%H:%M:%S.%fZ')
    return result


def YT_duration_to_string(YT_duration):
    prog = re.compile(r'PT(\d+H)?(\d+M)?(\d+S)?')
    result = prog.match(YT_duration)
    arr = []
    for i in range(1, 4):
        part = result.group(i)
        if not part is None:
            arr.append(part.lower())
    return ' '.join(arr)


def extract_data(video_id):
    print('extracting data for video', video_id)
    API_key = 'AIzaSyCh824aNQjLTRA5BAIaJD628KdNWmPhEqI'
    searchUrl = "https://www.googleapis.com/youtube/v3/videos?id=" + video_id + "&key=" + API_key + "&part=contentDetails,statistics,snippet"
    with request.urlopen(searchUrl) as url:
        response = url.read().decode('utf8')
    data = json.loads(response)
    result = {
                'id' : video_id,
                'author': data['items'][0]['snippet']['channelTitle'],
                'duration': data['items'][0]['contentDetails']['duration'],
                'uploaded': data['items'][0]['snippet']['publishedAt'],
                'views': data['items'][0]['statistics']['viewCount'],
                'title': data['items'][0]['snippet']['title']
              }
    return result

if __name__ == '__main__':
    pass
    # url = 'https://www.youtube.com/watch?v=GGnpIFK3G0Q'
    # cle = url_to_key(url) #'GGnpIFK3G0Q'
    # info = extract_data(cle)
    # info['duration'] = YT_duration_to_string(info['duration'])
    # info['uploaded'] = YT_published_to_date(info['uploaded'])
    # print(info)
    #
    # request_info('https://www.youtube.com/watch?v=3VdLXrPujpc')
    #
    # test_case = ['PT1H', 'PT23M', 'PT45S', 'PT1H23M', 'PT1H45S', 'PT23M45S', 'PT1H23M45S']
    # for each in test_case:
    #    YT_duration_to_string(each)
    #
    # test_case = ['http://youtu.be/SA2iWivDJiE', 'http://www.youtube.com/watch?v=_oPAwA_Udwc&feature=feedu', 'http://www.youtube.com/embed/SA2iWivDJiE', 'http://www.youtube.com/v/SA2iWivDJiE?version=3&amp;hl=en_US', 'https://www.youtube.com/watch?v=mxMkD-uCeB8&list=PLETuopLfmKSPXx-DAdq8fXA00WRb6rh1A']
    # for each in test_case:
    #    url_to_key(each)
    #
    # print(YT_published_to_date('2016-12-15T16:00:05.000Z'))