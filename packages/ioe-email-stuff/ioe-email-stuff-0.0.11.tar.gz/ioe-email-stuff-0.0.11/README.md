# ioe-email-stuff

A package that allows to send emails via a number of different methods from within a python application.

## Installation

Run the following to install:

```python
pip install ioe-email-stuff
```

## Usage

```python
from ioe_email_stuff import send_email

# Send an email - outlook only (for now)
# CC, BCC and attachment args not required
send_email("SUBJECT", "BODY", "USERNAME", "PASSWORD", "RECIPIENTS", "CCs", "BCCs", ["./ATTACHMENT1.png", "./ATTACHMENT2.png"])
```