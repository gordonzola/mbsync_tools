#!/usr/bin/env python3

import sys
import keyring

if __name__ == '__main__':
    try:
        acct = sys.argv[1]
        passwd = keyring.get_password('mbsync', acct)
        if passwd is None:
            print('Account not found', file=sys.stderr)
            sys.exit(1)
        print(passwd)
    except IndexError:
        print('Argument required: account', file=sys.stderr)
        sys.exit(1)
