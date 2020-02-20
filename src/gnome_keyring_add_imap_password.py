#!/usr/bin/env python3

import keyring
import getpass


if __name__ == '__main__':
    username = input("Username: ")
    password = getpass.getpass(prompt="Password: ")

    keyring.set_password("mbsync", username, password)
