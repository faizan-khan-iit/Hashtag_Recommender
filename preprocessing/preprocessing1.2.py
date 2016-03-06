import re
def remove_multiple(text):
    ls = re.findall(r'((\w)\2{2,})', text)
    chars = list(set(list(map(lambda x: x[1], ls))))
    for c in chars:
        reg_str = r'((' + c + r')\2{2,})'
        text = re.sub(reg_str, c, text)
    return text
    
def remove_stop_and_small_words(text):        
    for i in range(len(text)):
        if text[i] in stop_words or len(text[i]) < 3:
            text[i] = ""
    text = list(filter(("").__ne__, text))            
    text = " ".join(text) + "\n"
    return text

so = open("stop_words.txt")
data = so.readlines()
stop_words = [x.strip('\n') for x in data]    

for i in range(1, 19):
        
    f = open("../clean_1/Tweets_" + str(i) ,"r")    
    g = open("../clean_2/Tweets_" + str(i) + ".txt","w")
    
    for line in f:
        text = remove_multiple(str(line))[:-1].split()
        text = remove_stop_and_small_words(text)       
        g.write(text)

    f.close()
    g.close()

so.close()    