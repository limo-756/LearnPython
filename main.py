# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import pandas as pd
import json
import logging
import requests
import datetime
import math
import time
import sys

header = {
    "X-API-Key": "0a3597b2-9597-48fe-a341-f389207b20fe"
}

def iterateTheCsv(data, indexToStart):
    for index, row in data.iterrows():
        if (index < indexToStart):
            continue
        time.sleep(1)
        notificationBody = mapToMailOrderCreatedResponse(row)
        notificationBody = json.dumps(notificationBody)
        response = requests.post("https://proemail.hostgator.io/_webhook/titan", headers=header, json=notificationBody, timeout=10)
        if response.status_code != 200:
            logging.error("Failed to send notification id - %s, response %s", index, response.text)
            return



def mapToMailOrderCreatedResponse(attrs):
    notificationBody = {
        "id": attrs["event_id"],
        "event": "MAIL_ORDER_CREATED",
        "data": {
            "titanOrderId": int(attrs["domain_id"]),
            "domainName": attrs["domain_name"],
            "customerId": attrs["partner_customer_id"],
            "status": attrs["status"],
            "metadata": {}
        }

    }
    if attrs["metadata.cpanelUserName"] is not None and not(isNaN(attrs["metadata.cpanelUserName"])):
        notificationBody["data"]["metadata"]["cpanelUserName"] = attrs["metadata.cpanelUserName"]
    if attrs["metadata.cpanelHostName"] is not None and not(isNaN(attrs["metadata.cpanelHostName"])):
        notificationBody["data"]["metadata"]["cpanelHostName"] = attrs["metadata.cpanelHostName"]

    nullableFields = [EventKeyToResponseKeyMapper("customer_name", "customerName"),
                      EventKeyToResponseKeyMapper("customer_email", "customerEmailAddress"),
                      EventKeyToResponseKeyMapper("customer_country", "customerCountry"),
                      EventKeyToResponseKeyMapper("plan_type", "planType"),
                      EventKeyToResponseKeyMapper("storage_limit", "storageLimit", True),
                      EventKeyToResponseKeyMapper("no_of_accounts", "noOfAccounts", True),
                      EventKeyToResponseKeyMapper("billing_cycle", "billingCycle")]
    handleNullableFields(attrs, nullableFields, notificationBody)
    if attrs["expiry_date"] is not None and not(math.isnan(attrs["expiry_date"])):
        notificationBody["data"]["expiryDate"] = epocToDateTime(int(attrs["expiry_date"]))
    return notificationBody

class EventKeyToResponseKeyMapper:
    def __init__(self, eventKey, responseKey, isInt = False, isJson = False):
        self.keyName = eventKey
        self.responseKeyName = responseKey
        self.isInt = isInt
        self.isJson = isJson

def handleNullableFields(dic, nullableFields, response):
    for nullableField in nullableFields:
        if nullableField.keyName in dic and not(isNaN(dic[nullableField.keyName])):
            if (nullableField.isInt):
                response["data"][nullableField.responseKeyName] = int(dic[nullableField.keyName])
            elif (nullableField.isJson):
                response["data"][nullableField.responseKeyName] = json.loads(dic[nullableField.keyName])
            else:
                response["data"][nullableField.responseKeyName] = dic[nullableField.keyName]

def epocToDateConverter(dic, field, response):
    if field.keyName in dic:
        response["data"][field.responseKeyName] = epocToDateTime(int(dic[field.keyName]))

def epocToDateTime(epoc):
    epoc = epoc / 1000.
    return datetime.datetime.fromtimestamp(epoc).strftime("%Y-%m-%d").__str__()

def isNaN(string):
    return string != string


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    indexToStart = 0
    if (len(sys.argv) == 2):
        indexToStart = int(sys.argv[1])
    data = pd.read_csv('missedNotifications.csv')
    iterateTheCsv(data, indexToStart)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
