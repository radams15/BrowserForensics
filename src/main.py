from FirefoxExtractor import FirefoxExtractor
from ChromeExtractor import ChromeExtractor

'''f = FirefoxExtractor()
for h in f.history():
    print(h)'''

c = ChromeExtractor()

for h in c.history():
    print(h)
