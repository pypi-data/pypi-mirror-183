import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def a8mailer(luser, lpass ,to_list, subject, body, cc_list=None, bcc_list=None):
    """
    Send an email using Outlook and SMTP.
    
    Parameters:
    - luser (str): sender email
    - lpass (str): sender password
    - to_list (list of str): List of email addresses to send the email to.
    - subject (str): Subject of the email.
    - body (str): Body of the email.
    - cc_list (list of str): Optional list of email addresses to CC the email to.
    - bcc_list (list of str): Optional list of email addresses to BCC the email to.
    
    Returns:
    - None
    """
    # Create the message
    msg = MIMEMultipart()
    msg['To'] = ", ".join(to_list)
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    
    if cc_list:
        msg['CC'] = ", ".join(cc_list)
        
    if bcc_list:
        msg['BCC'] = ", ".join(bcc_list)
    
    # Connect to Outlook SMTP server and send the email
    server = smtplib.SMTP('smtp-mail.outlook.com')
    server.starttls()
    server.login(luser, lpass)
    server.sendmail(luser, to_list + cc_list + bcc_list, msg.as_string())
    server.quit()