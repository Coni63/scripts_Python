import re
import string

with open("ticket") as f:
    for ticket in f:
        ticket = ticket.upper()
        ticket = re.sub(r'\W', '', ticket)
        if ticket.startswith('PC'):
            print(ticket)
            pass
        elif ticket.startswith('CA'):
            print(ticket)
            pass
        elif ticket.startswith('WC'):
            print(ticket)
            pass
        elif ticket.startswith('STONO'):
            print(ticket)
            pass
        elif ticket.startswith('SOTONO'):
            print(ticket)
            pass
        elif ticket.startswith('SCPARIS'):
            print(ticket)
            pass
        elif ticket.startswith('WEP'):
            print(ticket)
            pass
        elif ticket.startswith('PPP'):
            # print(ticket)
            pass
        elif ticket.isnumeric():
            # print(ticket)
            pass