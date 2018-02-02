import os
import httplib2
from apiclient import discovery
import GMAILCredentials
from pprint import pprint
import requests

## GMAIL Account : onfaitlescours@gmail.com
## MDP           : bioinformatique

## INSTALL :  sudo apt install python3-pip
## INSTALL : pip3 install --upgrade google-api-python-client


def main():
    """
    Main function to run for message processing.
    It initializes the GMAIL connection for onfaitlescours@gmail.com
    """

    # Getting credentials and service to interact with the GMAIL API
    credentials = GMAILCredentials.get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build(
        'gmail', 'v1', http=http, developerKey=GMAILCredentials.API_KEY)

    # TODO : Display all labels for onfaitlescours@gmail.com
    # display_labels(service)

    # TODO : display all messages in INBOX
    # display_inbox_messsages(service)

    # TODO : Display mails coming from maucourt.t@gmail.com
    display_messages_from(service, "maucourt.t@gmail.com")

def display_labels(service):
    """Display labels for onfaitlescours@gmail.com

    Arguments:
        service {service} -- object allowing the communication with GMAIL API
    """

    labels = service.users().labels().list(userId="me").execute()

    for label in labels["labels"]:
        print(label["id"])


def display_inbox_messsages(service):
    """Display all messages with the INBOX label

    Arguments:
        service {service} -- object allowing the communication with GMAIL API
    """

    labels = ["INBOX"]

    messages_informations = service.users().messages().list(userId="me", labelIds=labels).execute()

    pprint(messages_informations)

    # messages_list = list()
    for message in messages_informations["messages"]:
        message_id = message["id"]
        message_content = service.users().messages().get(userId="me", id=message_id).execute()

        pprint(message_content)
        print("\n\n+++\n\n")

def display_messages_from(service, sender):
    """Display mails coming from sender
    
    Arguments:
        service {service} -- object allowing the communication with GMAIL API
        sender {string} -- sender mail
    """

    labels = ["INBOX"]

    messages_informations = service.users().messages().list(userId="me", labelIds=labels).execute()

    # messages_list = list()
    for message in messages_informations["messages"]:
        message_id = message["id"]
        message_content = service.users().messages().get(userId="me", id=message_id).execute()

        for header in message_content["payload"]["headers"]:
            if header["name"] == "From" and sender in header["value"]:
                pprint(message_content)

if __name__ == '__main__':
    main()
