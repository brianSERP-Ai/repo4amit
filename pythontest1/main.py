# import csv

# with open('articles_original.csv', 'r') as csv_file:
#     csv_reader = csv.DictReader(csv_file)

#     with open('new_names.csv', 'w', newline="") as new_file:
#         fieldnames = ['first_name', 'last_name', 'email']

#         csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter=',')

#         csv_writer.writeheader()

#         for line in csv_reader:
            
#             csv_writer.writerow(line)


#YOU NEED TO ADD CODE HERE TO PROCESS THE ROW IN THE CSV FILE RIGHT NOW THIS WONT WORK!


context = "<h2> The mounting of your engagement ring influences the ring’s design — so consider your ring setting carefully. </h2> <p> If a diamond is indeed forever, you need a setting that’s going to last. It’s important to consider the engagement ring setting, or mounting, as part of the overall design — and also understand how it can contribute to the diamond’s everlasting beauty. </p> <p> For people who use their hands a lot, the bezel keeps diamonds snug and prevents them from snagging on things. </p> <p> People can mean different things when they refer to a diamond’s setting. Sometimes you’ll hear jewelers refer to the <em> overall ring </em> as the setting when describing the ring that you choose to have a diamond set into. </p> <p> Technically, a ring is made up of two parts: the <em> shank </em> , or body of the ring, and the <em> head </em><h2> The mounting of your engagement ring influences the ring’s design — so consider your ring setting carefully. </h2> <p> If a diamond is indeed forever, you need a setting that’s going to last. It’s important to consider the engagement ring setting, or mounting, as part of the overall design — and also understand how it can contribute to the diamond’s everlasting beauty. </p> <p> For people who use their hands a lot, the bezel keeps diamonds snug and prevents them from snagging on things. </p> <p> People can mean different things when they refer to a diamond’s setting. Sometimes you’ll hear jewelers refer to the <em> overall ring </em> as the setting when describing the ring that you choose to have a diamond set into. </p> <p> Technically, a ring is made up of two parts: the <em> shank </em> , or body of the ring, and the <em> head </em><h2> The mounting of your engagement ring influences the ring’s design — so consider your ring setting carefully. </h2> <p> If a diamond is indeed forever, you need a setting that’s going to last. It’s important to consider the engagement ring setting, or mounting, as part of the overall design — and also understand how it can contribute to the diamond’s everlasting beauty. </p> <p> For people who use their hands a lot, the bezel keeps diamonds snug and prevents them from snagging on things. </p> <p> People can mean different things when they refer to a diamond’s setting. Sometimes you’ll hear jewelers refer to the <em> overall ring </em> as the setting when describing the ring that you choose to have a diamond set into. </p> <p> Technically, a ring is made up of two parts: the <em> shank </em> , or body of the ring, and the <em> head </em><h2> The mounting of your engagement ring influences the ring’s design — so consider your ring setting carefully. </h2> <p> If a diamond is indeed forever, you need a setting that’s going to last. It’s important to consider the engagement ring setting, or mounting, as part of the overall design — and also understand how it can contribute to the diamond’s everlasting beauty. </p> <p> For people who use their hands a lot, the bezel keeps diamonds snug and prevents them from snagging on things. </p> <p> People can mean different things when they refer to a diamond’s setting. Sometimes you’ll hear jewelers refer to the <em> overall ring </em> as the setting when describing the ring that you choose to have a diamond set into. </p> <p> Technically, a ring is made up of two parts: the <em> shank </em> , or body of the ring, and the <em> head </em><h2> The mounting of your engagement ring influences the ring’s design — so consider your ring setting carefully. </h2> <p> If a diamond is indeed forever, you need a setting that’s going to last. It’s important to consider the engagement ring setting, or mounting, as part of the overall design — and also understand how it can contribute to the diamond’s everlasting beauty. </p> <p> For people who use their hands a lot, the bezel keeps diamonds snug and prevents them from snagging on things. </p> <p> People can mean different things when they refer to a diamond’s setting. Sometimes you’ll hear jewelers refer to the <em> overall ring </em> as the setting when describing the ring that you choose to have a diamond set into. </p> <p> Technically, a ring is made up of two parts: the <em> shank </em> , or body of the ring, and the <em> head </em><h2> The mounting of your engagement ring influences the ring’s design — so consider your ring setting carefully. </h2> <p> If a diamond is indeed forever, you need a setting that’s going to last. It’s important to consider the engagement ring setting, or mounting, as part of the overall design — and also understand how it can contribute to the diamond’s everlasting beauty. </p> <p> For people who use their hands a lot, the bezel keeps diamonds snug and prevents them from snagging on things. </p> <p> People can mean different things when they refer to a diamond’s setting. Sometimes you’ll hear jewelers refer to the <em> overall ring </em> as the setting when describing the ring that you choose to have a diamond set into. </p> <p> Technically, a ring is made up of two parts: the <em> shank </em> , or body of the ring, and the <em> head </em><h2> The mounting of your engagement ring influences the ring’s design — so consider your ring setting carefully. </h2> <p> If a diamond is indeed forever, you need a setting that’s going to last. It’s important to consider the engagement ring setting, or mounting, as part of the overall design — and also understand how it can contribute to the diamond’s everlasting beauty. </p> <p> For people who use their hands a lot, the bezel keeps diamonds snug and prevents them from snagging on things. </p> <p> People can mean different things when they refer to a diamond’s setting. Sometimes you’ll hear jewelers refer to the <em> overall ring </em> as the setting when describing the ring that you choose to have a diamond set into. </p> <p> Technically, a ring is made up of two parts: the <em> shank </em> , or body of the ring, and the <em> head </em><h2> The mounting of your engagement ring influences the ring’s design — so consider your ring setting carefully. </h2> <p> If a diamond is indeed forever, you need a setting that’s going to last. It’s important to consider the engagement ring setting, or mounting, as part of the overall design — and also understand how it can contribute to the diamond’s everlasting beauty. </p> <p> For people who use their hands a lot, the bezel keeps diamonds snug and prevents them from snagging on things. </p> <p> People can mean different things when they refer to a diamond’s setting. Sometimes you’ll hear jewelers refer to the <em> overall ring </em> as the setting when describing the ring that you choose to have a diamond set into. </p> <p> Technically, a ring is made up of two parts: the <em> shank </em> , or body of the ring, and the <em> head </em>"




# This is my way of splitting the ddat. I want all caps made into lower first then added again to the start of every list item"

import re
new_str3 = context

new_str4 = new_str3
# .replace("  ", " ").replace(",",", ").replace("   "," ").replace("*","")

new_str5 = new_str4
print(new_str5)


test = new_str5
print("FUUUUUCCKKK" +test)
test2 = re.split(r'(?<=>)(.+?)(?=<)', test)


# res = re.findall(r'<[^>]*>.*?</[^>]*>(?:<[^>]*/>)?|[^<>]+', new_str5)
# new_str6 = res

# print(new_str6)

for i, word in enumerate(test2):
    test2[i] = word.replace('<',"4").replace('>',"6")


print(test2)

# start of chunking
max_chunk = 50

current_chunk = 0 
chunks = []
for sentence in test2:
    if len(chunks) == current_chunk + 1: 
        if len(chunks[current_chunk]) + len(sentence.split(' ')) <= max_chunk:
            chunks[current_chunk].extend(sentence.split(' '))
        else:
            current_chunk += 1
            chunks.append(sentence.split(' '))
    else:
        print(current_chunk)
        chunks.append(sentence.split(' '))

for chunk_id in range(len(chunks)):
    chunks[chunk_id] = ' '.join(chunks[chunk_id])

print(chunks[1])

# values = ' '.join([str(elem) for elem in new_str6])
# print(values)


# res = re.findall(r'<[^>]*>.*?</[^>]*>(?:<[^>]*/>)?|[^<>]+', values)
# print(res)

# for i, word in enumerate(res):
#     res[i] = word.replace("<","").replace(">","")

# print(res)
# THE PEGASUS MODEL
print(len(chunks))
import requests

API_URL = "https://api-inference.huggingface.co/models/tuner007/pegasus_paraphrase"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

output = query(chunks[0])
# print(output)
# values = ' '.join([str(elem) for elem in output])


# #Concatenating shit at the end(you might need to change this)
# values = ' '.join([str(elem) for elem in output])

# new_value = values.replace("{'generated_text':", "").replace("{'",'').replace("'},",'').replace("}",'').replace("'",'').replace("  "," ").replace('"'," ")

# print("FIRST_SHOT:" +new_value)
# finaltest = new_value.split(".")




# # # Now you need to somehow add the original HTML back before saving in the the new CSV folder