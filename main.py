from urllib.request import urlopen
from bs4 import BeautifulSoup
import operator
import sys
 
result = []
for i in range(30):
    html = urlopen("https://programathor.com.br/jobs/page/"+str(i))
    bs = BeautifulSoup(html, 'html.parser')
    linhas = bs.find_all('span', {'class':'tag-list background-gray'})
    sys.stdout.write("pagina: %d\r" % (i))
    sys.stdout.flush()
    for i in linhas:
        result.append(i.text)
        
counts = dict()
for i in result:
  counts[i] = counts.get(i, 0) + 1

sorted = dict(sorted(counts.items(), key=operator.itemgetter(1),reverse=True))
values = sorted.values()
total = sum(values)

for (key) in sorted:
    print(key+":"+str(sorted[key])+'/'+str(total))