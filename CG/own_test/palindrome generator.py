import string
import random

"""
choice = string.ascii_letters + string.digits
#print(choice)

final = ''
left = ''
before = ''
after = ''
palindrome = ""
for i in range(500):
    left += choice[random.randrange(len(choice))]

for j in range(4500):
    before += choice[random.randrange(len(choice))]
    after += choice[random.randrange(len(choice))]

palindrome = left + left[::-1]
final = before + palindrome + after


print(palindrome)
print(final)
"""

import itertools
palindrome = ""
after = ''
before = ''
mix = ''
choice = string.ascii_uppercase

g = itertools.cycle('EF')
for i in range(999):
    palindrome += next(g)
print(palindrome)


split = random.randint(1, 9000)
for i in range(9000):
    mix += choice[random.randrange(len(choice))]

palindrome = mix[:split] + palindrome + mix[split:]
print(palindrome)

"""

t = 'x0xRjJRRu5DYAHBUUCd71XO7KLsgE7sztLwM8ngNIpTG8IetjIK2bfmznHxiof2D5wIClCo5cufRIQvUHuDl1UdbUlKwWNVhMsoIDcrlB9luKWfgmwiBQsykT4WO7ZukmrZGSabgEoGulRAYYh9ghgLcbjAHlG8M2Z6DlJrkQVd7rKNySleV9CCFPnzMtIpXoD5fTTiU0mHOL3BxV9fOdGEpVRHJJIC4ZzY8UgXF2VA3yt4BpRvQZ1fruAuocH96ix9Qf1jBE9nB68x2nim3wAXEgNYlmqy2unfW88PRPauLKBA2T2jeFTpUyGBcIF8beWfFV8jTi2HGQw4qNrZbyhJQLidjEmelHBgQyaurLjcd7D4deMwYC22vSwvErN67a0NcoICuZtAGKjMduxPBwR79djLNCHfLKbieAwAILEsw0PHRbVe3m6GuzoN9kOzZlpyGqng8TFAsdWgLn5zRR18VSkQtcQWElU8JezhvLt7sBs2DKMOpRWgPblvhlERhbbOJ7d8tWGvX1odfcgz56XMALaEefV8NTnYrE45J2MAydXWvkBMzcQCEQ4dtiZdBeCDjD2uaN5fid2CmpwjNG0zX3BlpKcF3RruLAjJpxexz411CW1mggyd63q4luDWvfcxesG32unYCBOP9Vc72SJQWEXuSbhm3j1boj12c1Edl6vrx37LAxBCB47KaLzyfh8buwrRg5Nj8yPMLocZ4jUW1AnQzqQaO01ukgZ0c7tlzYvfzHxmERWMUCbTX9tz5DL0lwyKuKb4XWkGV4wI2iph1WvWNQTKekYTxqZtILgjL8lYLbUwx22I1WyV0DqpmEg2Er93pWtOd9MkafMFABmneOjprJaU7R1e00bJB6CbxRY71OGzRUrrWFbFaelF9VkV9Sm0iJWwL6VUHb7VDcFDySpyJ4TKCe8XwgVvhkaOVhXzFkWsE7DQC21r4CaJqcibE4f5Hog4XLYR5KCgEVo0EuATqNAO94F3J6cJ8'
print(len(t))
"""