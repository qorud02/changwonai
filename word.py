from urllib.request import urlopen

with urlopen('http://blogattach.naver.net/ca5fd665752b2ef2dd3a506a5db3c1b01343b85ee2/20180618_274_blogfile/topspin1278_1529278974170_Fa2424_txt/story.txt') as story:
  story_words = []
  for line in story:
      line_words = line.decode('utf-8').split()
      for word in line_words:
          story_words.append(word)

for word in story_words:
  print(word)