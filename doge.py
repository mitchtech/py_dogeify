import nltk
import re
import random

doge_adjectives = ["so", "such", "very", "much", "many", "how"]
doge_emotions = ["wow", "amaze", "excite"]

def dogeify(text):
  doge_msg = []
  sentences = re.split(r' *[\.\?!][\'"\)\]]* *', text)

  for sentence in sentences:
    if sentence == '':
      break
    
    doge_sentence = []
    tagged_set = nltk.pos_tag(sentence.split())

    allnouns = [word for word,pos in tagged_set if pos == 'NN' or pos == 'NNP'or pos == 'NNS' or pos == 'JJ']
    
    for word in allnouns:
      phrase = doge_adjectives[random.randint(0,5)] + " " + word.strip(',\'') + "."
      doge_sentence.append(phrase)
      
    emotion = doge_emotions[random.randint(0,2)] + "."
    doge_sentence.append(emotion)
    #print " ".join(doge_sentence)
    
    doge_msg.append(" ".join(doge_sentence))
  return " ".join(doge_msg)

  
if __name__ == '__main__':
  text = "We hold these truths to be self-evident, that all men are created equal, that they are endowed by their Creator with certain unalienable Rights, that among these are Life, Liberty and the pursuit of Happiness."
  print dogeify(text)
  