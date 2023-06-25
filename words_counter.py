# working script

import re  # module for regular expressions
from collections import Counter

from moviepy.editor import VideoFileClip

times_texts = []


# Need to figure out how it wokrs and why is error
def convert_time(timestring):
    """ Converts a string into seconds """
    nums = map(float, re.findall(r'\d+', timestring))
    return 3600 * nums[0] + 60 * nums[1] + nums[2] + nums[3] / 1000


with open("apple.srt") as f:
    lines = f.readlines()

current_times, current_text = None, ""
for line in lines:
    times = re.findall("[0-9]*:[0-9]*:[0-9]*,[0-9]*", line)
    if times != []:
        current_times = map(convert_time, times)
    elif line == '\n':
        times_texts.append((current_times, current_text))
        current_times, current_text = None, ""
    elif current_times is not None:
        current_text = current_text + line.replace("\n", " ")

whole_text = " ".join([text for (time, text) in times_texts])
all_words = re.findall("\w+", whole_text)
counter = Counter([w.lower() for w in all_words if len(w) > 5])
print(counter.most_common(10))  # word count limit

video = VideoFileClip(r'C:\Users\GIGACHAD\Desktop\videogrep2\source_videos\apple.mp4')

cuts = [times for (times, text) in times_texts
        if (re.findall("iphone", text) != [])]
