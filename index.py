import pandas as pd
import smtplib
import os
from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

load_dotenv()
col_names = ['name', 'email', 'company']
excel_file = './apollo-contacts-export.csv'
df = pd.read_csv(excel_file)



smtp_username = os.getenv('SMTP_USERNAME')
smtp_password = os.getenv('SMTP_PASSWORD')


email_body_template = """Hello {name},
<br>
Chinmay here, I'm writing this cold email to apply for any Software Engineering / Fullstack development position at {company}.
<br>
A little about myself, I'm a full-stack developer and I'm passionate about coding. I like to solve real-world problems with the help of code. 
<br>
I'm always curious to learn about new technologies and challenge myself. I feel I'm a great team player as I always tend to prioritize team goals over personal achievements. 
<br>
One thing I can guarantee about myself is that I will always show up be it good days or bad, and I think you can't bet against this mindset.
<br>
I have prior experience working at startups and also at big-tech where I interned last summer at Amazon building scalable applications.
<br>
Take a look at one of my portfolio projects which was used by my college professors built using MERN stack - <a href="{portfolio_project_link}">Link</a>.
<br>
Few other side projects which I have built:
<br>
- Stackoverflow-chatpft-chrome-extension - <a href="{stackoverflow_chat_link}">Link</a> 
<br>
- YouTube-PDF-chatbot - <a href="{youtube_chatbot_link}">Link</a> 
<br>
My socials:
<br>
<a href="{linkedin_link}">LinkedIn</a> | <a href="{github_link}">GitHub</a> | <a href="{portfolio_link}">Portfolio</a>
<br>
Hoping to hear from you soon if there is a matching role.
<br>
Thanks and Regards,
<br>
Chinmay.
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
            portfolio_project_link="https://github.com/chinmaykhamkar/LoR",
            stackoverflow_chat_link="https://github.com/chinmaykhamkar/chat-gpt-stackoverflow",
            youtube_chatbot_link="https://github.com/chinmaykhamkar/youtube-pdf-chatbot",
            linkedin_link="https://www.linkedin.com/in/chinmaykhamkar/",
            github_link="https://github.com/chinmaykhamkar",
            portfolio_link="https://chinmaykhamkar-github-io.vercel.app/"
            )
        message.attach(MIMEText(email_body, 'html'))
        
        # pdf attach
        pdf_path = "./Chinmay_Khamkar_resume.pdf"
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

   