import json
import csv

open_json_file = open('sample_json_file.json','r')
json_parse_data = json.loads(open_json_file.read())

csv_file = open('converted_csv_file.csv','w')

csvwriter = csv.writer(csv_file)

counter = 0

for i in json_parse_data:
    if counter == 0:
        csvwriter.writerow(i.keys())
        counter+=1
    csvwriter.writerow(i.values())
csv_file.close()
