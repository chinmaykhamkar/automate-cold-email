# import pandas as pd
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

# # Load data from Excel
# excel_file = "./test.xlsx"
# df = pd.read_excel(excel_file)

# # Email configuration
# smtp_server = "smtp.gmail.com"
# smtp_port = 465
smtp_username = os.getenv("SMTP_USERNAME")
smtp_password = os.getenv("SMTP_PASSWORD")
sender_email = "chinmaykhamkar8@gmail.com"

# Email template
email_subject = "Subject of your email"
email_body_template = """Dear chinmay,

Thank you for your interest in our company. 
Please find the attached PDF for more information.

Best regards,
Your Name"""

# LinkedIn link
# linkedin_url = "https://www.linkedin.com/in/chinmaykhamkar/"

message = MIMEMultipart('alternative', None, [MIMEText(email_body_template,'plain')])
message['Subject'] = email_subject
message['From'] = smtp_username
message['To'] = sender_email

try:
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.sendmail(smtp_username, sender_email, message.as_string())
    server.quit()
    print("email sent")
except Exception as e:
    print(e)

    
# # Email template
# email_subject = "Subject of your email"
# email_body_template = """Dear {name},

# Thank you for your interest in our company, {company}. 
# Please find the attached PDF for more information.

# Best regards,
# Your Name"""

# # LinkedIn link
# linkedin_url = "https://www.linkedin.com/in/chinmaykhamkar/"

# # Iterate through each row in the Excel sheet
# for index, row in df.iterrows():
#     # Create email message
#     msg = MIMEMultipart()
#     msg['From'] = smtp_username
#     msg['To'] = row['email']
#     msg['Subject'] = email_subject

#     # Replace placeholders in the email body template
#     email_body = email_body_template.format(name=row['name'], company=row['company'])
#     msg.attach(MIMEText(email_body, 'plain'))

#     # Attach PDF
#     pdf_path = "./Chinmay_Khamkar_resume.pdf"
#     with open(pdf_path, "rb") as pdf_file:
#         pdf_attachment = MIMEApplication(pdf_file.read(), _subtype="pdf")
#         pdf_attachment.add_header('Content-Disposition', f'attachment; filename={pdf_path}')
#         msg.attach(pdf_attachment)

#     # Insert LinkedIn link
#     email_body_with_linkedin = email_body.replace("LinkedIn - link", f'<a href="{linkedin_url}">LinkedIn</a>')
#     msg.attach(MIMEText(email_body_with_linkedin, 'html'))

#     # Connect to SMTP server and send email
#     with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
#         # server.starttls()
#         server.ehlo()
#         server.login(smtp_username, smtp_password)
#         server.sendmail(smtp_username, row['email'], msg.as_string())

# print("Emails sent successfully.")

