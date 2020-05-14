import argparse
import getpass
import imaplib
import poplib
import smtplib
import os
import socket 

IMAP_SERVER = 'imap.googlemail.com'
IMAP_PORT = 993

POP_SERVER = 'pop.googlemail.com'
POP_PORT = 995

def imap_mail(username):
    mailbox = imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT) 
    password = getpass.getpass(prompt='Enter your email password: ') 
    mailbox.login(username, password)
    mailbox.select('Inbox')
    typ, data = mailbox.search(None, 'ALL')
    for num in data[0].split():
        typ, data = mailbox.fetch(num, '(RFC822)')
        print ('Message %s\n%s\n' % (num, data[0][1]))
        break
    mailbox.close()
    mailbox.logout()
    
def pop_mail(username):
    mailbox = poplib.POP3_SSL(POP_SERVER, POP_PORT) 
    mailbox.user(username)
    password = getpass.getpass(prompt='Enter your email password: ') 
    mailbox.pass_(password) 
    num_messages = len(mailbox.list()[1])
    print ('Total emails: {}'.format(num_messages))
    mailbox.quit()

def mail():
    protocol = input("Ketik pop_mail atau imap_mail : ")
    if (protocol == "imap_mail"):
        imap_mail('edwardyukihira@gmail.com')
    else:
        pop_mail('edwardyukihira@gmail.com')

if __name__ == '__main__':
    mail()
    