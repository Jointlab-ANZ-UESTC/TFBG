import sys
import requests
import csv
def getHttpStatusCode(url):
    try:
        request = requests.get(url)
        httpStatusCode = request.status_code
        return httpStatusCode
    except requests.exceptions.HTTPError as e:
        return e

if __name__ == "__main__":
    with open('urls.csv', 'r') as f:
        csv_reader = csv.reader(f)
        for line in csv_reader:
            try:
                status = getHttpStatusCode(csv_reader)
                if status == 200:
                    with open('200.csv', 'a') as w:
                        csv_write = csv.wirter(w)
                        csv_write.writerow(line)
                        print
                        line
                else:
                    print
                    'no 200 code'
            except Exception as e:
                print
                e

