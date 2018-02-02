import os
import httplib2
from apiclient import discovery
import GMAILCredentials
from pprint import pprint
import requests

# GMAIL Account : onfaitlescours@gmail.com
# MDP           : bioinformatique

# INSTALL :  sudo apt install python3-pip
# INSTALL : pip3 install --upgrade google-api-python-client


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
    display_labels(service)

    # TODO : display all messages in INBOX
    display_inbox_messsages(service)

    # TODO : Display mails coming from maucourt.t@gmail.com
    display_messages_from(service, "maucourt.t@gmail.com")


def display_labels(service):
    """
    Display labels for onfaitlescours@gmail.com

    Arguments:
        service {service} -- object allowing the communication with GMAIL API
    """

    pass


def display_inbox_messsages(service):
    """
    Display all messages with the INBOX label

    Arguments:
        service {service} -- object allowing the communication with GMAIL API
    """

    pass


def display_messages_from(service, sender):
    """
    Display mails coming from sender

    Arguments:
        service {service} -- object allowing the communication with GMAIL API
        sender {string} -- sender mail
    """

    pass

if __name__ == '__main__':
    main()
