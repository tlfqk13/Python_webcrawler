import nltk
import sys
import string
from nltk.tokenize import RegexpTokenizer
from nltk.tokenize import TweetTokenizer
text="this is a test. Let's try this sentence boundary detector"
text_output=nltk.tokenize.sent_tokenize(text)
print('text_ouput :{0}'.format(text_output))
f_name=input('검색 결과를 저장할 csv 파일경로와 이름을 지정하세요 : ')

r=open('test.txt',mode='rt')
raw=r.read()
tokens=nltk.sent_tokenize(raw)
text1=nltk.Text(tokens)
lines=[]
tknzr=TweetTokenizer()
ss=tknzr.tokenize(str(r))


orig_stdout=sys.stdout
#f=open(f_name,'w',encoding='UTF-8')
#sys.stdout=f
#print(testString)
print("#"*50)

sys.stdout=orig_stdout
#f.close()
