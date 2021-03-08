#! python3
# pw.py - An insecure password locker program.

import sys
import pyperclip

passwords = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '1234'}


if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]   # First command line arg is the account name

if account in passwords:
    pyperclip.copy(passwords[account])
    print('Password for ' + account + 'copied to clipboard.')
else:
    print('There is no account named ' + account)
