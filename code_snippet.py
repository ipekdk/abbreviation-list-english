import pandas as pd
import re
abbr=pd.read_excel('abbraviations_eng.xlsx')
old = abbr['abbr']
new = abbr['long']
k=0 #counts how many changes are made
def abbr_clean(text):
    global k
    for i in range(0,len(abbr)):
      for word in text.split():
          if old[i] == word:
              text = re.sub(str(old[i]), str(new[i]), text)
              k+=1
    return text
# usage:
df['clean']=df['clean'].apply(abbr_clean) #df is the dataframe where your text is. Mine is twitter data as sentences.
  
