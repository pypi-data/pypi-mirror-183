# python-mailer

a8mailer is a package for sending emails using Outlook and SMTP.

### Installation
To install a8mailer, run the following command:

```bash
pip install a8mailer
```

### Usage
To use Mailer, import the a8mailer function and call it with the required arguments:
```python
from a8mailer import a8mailer

# Send an email to one recipient
a8mailer('sender@email.com','password',['recipient@email.com'], 'Subject', 'Body')

# Send an email to multiple recipients
a8mailer('sender@email.com','password', ['recipient1@email.com', 'recipient2@email.com'], 'Subject', 'Body')

# Send an email with CC and BCC recipients
a8mailer('sender@email.com','password',['recipient1@email.com', 'recipient2@email.com'], 'Subject', 'Body',
           cc_list=['cc1@email.com', 'cc2@email.com'], bcc_list=['bcc1@email.com', 'bcc2@email.com'])

```

The a8mailer function has the following parameters:

- luser (str): sender email
- lpass (str): sender password
- to_list (required): List of email addresses to send the email to.
- subject (required): Subject of the email.
- body (required): Body of the email.
- cc_list (optional): List of email addresses to CC the email to.
- bcc_list (optional): List of email addresses to BCC the email to.

### License
Mailer is licensed under the MIT License. See the LICENSE file for more details.