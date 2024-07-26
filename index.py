import pandas as pd
import smtplib
import os
from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

load_dotenv()
# make sure that the column names containing name, company name and email are "First Name", "Company" and "Email" resp
excel_file = 'your csv file.csv'
df = pd.read_csv(excel_file)



smtp_username = os.getenv('SMTP_USERNAME')
smtp_password = os.getenv('SMTP_PASSWORD')


email_body_template = """Hello {name},
<br>
I'm John Doe, writing this email to apply for xyx role at {company}.
<br>
your cold email body here
<br>
<a href="{linkedin_link}">LinkedIn</a> | <a href="{github_link}">GitHub</a> | <a href="{portfolio_link}">Portfolio</a>
<br>
"""

try:
    for index, row in df.iterrows():
        message = MIMEMultipart()
        message['Subject'] = f"Application for Software Engineer Position at {row['Company']}"
        message['From'] = smtp_username
        message['To'] = row['Email']

        email_body = email_body_template.format(
            name=row['First Name'], 
            company=row['Company'], 
            linkedin_link="your-linkedin-url",
            github_link="your-github-url",
            portfolio_link="your-portfolio-url"
            ## add other links as needed
            )
        message.attach(MIMEText(email_body, 'html'))
        
        # pdf attach (resume or other doc)
        pdf_path = "./path to pdf.pdf"
        with open(pdf_path, "rb") as pdf_file:
            pdf_attachment = MIMEApplication(pdf_file.read(), _subtype="pdf")
            pdf_attachment.add_header('Content-Disposition', f'attachment; filename={pdf_path}')
            message.attach(pdf_attachment)
        
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(smtp_username, row['Email'], message.as_string())
        server.quit()
        print("email sent",index+1)
except Exception as e:
    print("error",e)

   