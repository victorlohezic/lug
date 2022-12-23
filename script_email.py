import os
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from datetime import datetime

def send_email_smtp(receiver, path):
  """
  Send email using SMTP from sender to receiver with an attachemnent from path
  """
  customer = os.environ.get('LUG_CUSTOMER')
  educational_manager = os.environ.get('LUG_EDUCATIONAL_MANAGER')
  receivers = {"Customer" : customer, "Educational manager" : educational_manager}
  currentDateAndTime = datetime.now()
  currentHour = int(currentDateAndTime.strftime("%H"))

  sender_email=os.environ.get('LUG_SENDER')
  receiver_email = [sender_email, receivers[receiver]]
  password = os.environ.get('LUG_PASSWORD')

  message = MIMEMultipart("alternative")
  message["Subject"] = "[PFA ZesteDeSavoir] Compte Rendu"
  message["From"] = sender_email
  message["To"] = ", ".join(receiver_email)
  end_email = "bonne fin de journée" if currentHour >= 18 else "bonne journée" 

  # Create the plain-text and HTML version of your message
  text = f"""\
  Bonjour,
  vous trouverez en pièce jointe le compte rendu de la dernière réunion. 
  {end_email}, 
  Victor Lohézic
  """
  html = f"""\
  <html>
    <body>
      <p>Bonjour,<br>
        vous trouverez en pièce jointe le compte rendu de la dernière réunion. <br>
        {end_email}, <br>
        Victor Lohézic
      </p>
    </body>
  </html>
  """

  # Turn these into plain/html MIMEText objects
  part1 = MIMEText(text, "plain")
  part2 = MIMEText(html, "html")

  # Add HTML/plain-text parts to MIMEMultipart message
  # The email client will try to render the last part first
  message.attach(part1)
  message.attach(part2)

  filename = "compte_rendu.pdf"

  # Open PDF file in binary mode
  with open(path, "rb") as attachment:
      # Add file as application/octet-stream
      # Email client can usually download this automatically as attachment
      part = MIMEBase("application", "octet-stream")
      part.set_payload(attachment.read())

  # Encode file in ASCII characters to send by email    
  encoders.encode_base64(part)

  # Add header as key/value pair to attachment part
  part.add_header(
      "Content-Disposition",
      f"attachment; filename= {filename}",
  )

  # Add attachment to message and convert message to string
  message.attach(part)

  # Create secure connection with server and send email
  context = ssl.create_default_context()
  with smtplib.SMTP_SSL("partage.bordeaux-inp.fr", 465, context=context) as server:
      server.login(sender_email, password)
      server.sendmail(
          sender_email, receiver_email, message.as_string()
      )
