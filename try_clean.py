import re
import time

# Import the necessary package to process data in JSON format
try:
    import json
except ImportError:
    import simplejson as json


# Clean text before saving in file
def clean_text(text):
    text = re.sub(r'\'+', '', text)
    text = re.sub(r'[^\x00-\x7F]+', ' ', text)
    text = re.sub(r'(https?://[^\s]+)', ' ', text, flags=re.MULTILINE)
    text = re.sub('[$,?!\n]', ' ', text)
    text = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", text).split())
    text = re.sub('[^A-Za-z0-9 ]+', ' ', text)
    return text

tweets_filename = 'raw_2016-Feb-28__00_31_50.txt'
tweets_file = open(tweets_filename, "r")

moment = time.strftime("%Y-%b-%d__%H_%M_%S", time.localtime())
ht_file_name = "../cleaned_ht/cleaned_ht_" + moment + ".txt"
text_file_name = "../cleaned_text/cleaned_text_" + moment + ".txt"
info_file_name = "../cleaned_info/cleaned_info_" + moment + ".txt"

ht_file = open(ht_file_name, 'w')
text_file = open(text_file_name, 'w')
info_file = open(info_file_name, 'w')

id_list = list()
tweets_with_ht = 0

for line in tweets_file:
    try:
        # Read in one line of the file, convert it into a json object 
        tweet = json.loads(line.strip())
        if 'text' in tweet:  # only messages contains 'text' field is a tweet
            idt = str(tweet['id'])
            id_list.append(idt)

            created = str(tweet['created_at'])
            text = str(tweet['text'])

            user_id = str(tweet['user']['id'])  # id of the user who posted the tweet
            user_name = str(tweet['user']['name'])  # name of the user, e.g. "Wei Xu"
            user_screen_name = str(tweet['user']['screen_name'])  # name of the user account, e.g. "cocoweixu"
            user_location = clean_text(str(tweet['user']['location']))

            text = clean_text(text)

            info_file.write(idt + ", " + created + ", " + user_id + "\n")
            text_file.write(text + " ,\n")

            hash_tags = []
            for hashtag in tweet['entities']['hashtags']:
                ht = hashtag['text']
                ht = clean_text(ht)
                hash_tags.append(ht)
                ht_file.write(" " + ht + ", ")

            if hash_tags != []:
                tweets_with_ht += 1
            else:
                ht_file.write(", ")
            ht_file.write("\n")
    except:
        # read in a line is not in JSON format (sometimes error occurred)
        print("Error")
        continue

'''
print(len(id_list))
print(len(set(id_list)))
'''
print("Tweets with #s = ", tweets_with_ht)

ht_file.close()
text_file.close()
info_file.close()
tweets_file.close()
