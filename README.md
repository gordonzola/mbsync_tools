# mbsync_tools
A set of scripts to help mbsync fetch user credentials from system keyring

## Requirements

- python3 (tested on python3.7, should be working on every maintained python
  version)
- any system keyring supported by the
  [keyring](https://github.com/jaraco/keyring) lib, configured and running

## Installation

```shell
$ pip install https://github.com/gordonzola/mbsync_tools
```

## Usage

To store a password:

```shell
$ gnome_keyring_add_imap_password.py
Username: gordon
Password: admin  # note: no characters are actually shown here
Password saved for gordon
```

To retrieve a password:

```shell
$ mbsync_helpers.py gordon
admin
```

You can use it in your mbsync config file like this, for an `IMAPAccount`:

```
IMAPAccount gordon
Host mail.gordon.tld
User gordon
SSLType IMAPS
AuthMecs LOGIN
PassCmd "mbsync_helpers.py gordon"
```

## Licence

This tiny amount of work is released under the GPLv3.
