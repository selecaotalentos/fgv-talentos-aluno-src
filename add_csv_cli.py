# code responsible for adding users from csv

import csv
import yagmail
import argparse

from signin_api import add_login

def run(args):
    # required
    filename = args.filename
    manager = args.manager
    api_key = args.api_key
    # flags
    preffix = args.p
    bodyf = args.body
    gmail = args.gmail
    gname = args.gname
    appwd = args.appwd
    subject = args.subj
    with open(filename) as csvfile:
        if len(bodyf) > 0:
            yag = yagmail.SMTP({gmail:gname}, appwd)

        for user in csv.reader(csvfile):
            user,name,email = user
            # creates users
            user = preffix+user
            name = name.title()
            password = add_login(user, email, name, manager, api_key)
            # sends message
            if len(bodyf) > 0:
                name = name.split()[0]
                body = open(bodyf).read()
                body = body.format(name, user, password, email)
                # sends email
                yag.send(to=email, subject=subject, contents=body,)
            else:
                print(name, user, password, email)

parser = argparse.ArgumentParser(description="creates users from .csv containing cols 'id, name, email'")
parser.add_argument("filename", help=".csv filename containing users to be added")
parser.add_argument("manager", help="AuthPro manager")
parser.add_argument("api_key", help="AuthPro api_key")
parser.add_argument("-p", help="preffix to usernames", required=False, default="")
parser.add_argument("--subj", help="email subject", required=False, default="Welcome")
parser.add_argument("--body", help="email from file format", required=False, default="")
parser.add_argument("--gmail", help="sender gmail address", required=False, default="")
parser.add_argument("--appwd", help="sender app password", required=False, default="")
parser.add_argument("--gname", help="sender user name", required=False, default="Suporte Talentos")

# cals main function
args = parser.parse_args()
run(args)