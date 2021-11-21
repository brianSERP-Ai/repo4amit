import csv

with open('names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open('new_names.csv', 'w', newline="") as new_file:
        fieldnames = ['first_name', 'last_name', 'email']

        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter=',')

        csv_writer.writeheader()

        for line in csv_reader:
            
            csv_writer.writerow(line)


#YOU NEED TO ADD CODE HERE TO PROCESS THE ROW IN THE CSV FILE RIGHT NOW THIS WONT WORK!


context = "(ROW IN CSV TO BE PROCESSED GOES HERE AMIT)"


# This is my way of splitting the ddat. I want all caps made into lower first then added again to the start of every list item"


new_str3 = context

new_str4 = new_str3.replace(".", ".").replace("  ", " ").replace(",",", ").replace("   "," ").replace("*","")

new_str5 = new_str4.lower()

new_str6 = new_str5.split(". ")

for i, word in enumerate(new_str6):
    new_str6[i] = word.capitalize().replace(".","")+"."



# THE PEGASUS MODEL

import requests

API_URL = "https://api-inference.huggingface.co/models/tuner007/pegasus_paraphrase"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

output = query(new_str6)

values = ' '.join([str(elem) for elem in output])


#Concatenating shit at the end(you might need to change this)
values = ' '.join([str(elem) for elem in output])

new_value = values.replace("{'generated_text':", "").replace("{'",'').replace("'},",'').replace("}",'').replace("'",'').replace("  "," ").replace('"'," ")

print("FIRST_SHOT:" +new_value)
finaltest = new_value.split(".")




# Now you need to somehow add the original HTML back before saving in the the new CSV folder