import pandas as pd
import smtplib
import os
from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import time
import random

load_dotenv()

logging.basicConfig(filename='email_log.log', level=logging.INFO)

excel_file = 'your csv file.csv'
df = pd.read_csv(excel_file)

smtp_username = os.getenv('SMTP_USERNAME')
smtp_password = os.getenv('SMTP_PASSWORD')
server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.login(smtp_username, smtp_password)

email_body_template = """
Hi {name},
<br>
<br>
I hope this message finds you well. My name is Tanishq Ranjan, a 4th Year engineering undergraduate at the National Institute of Technology Delhi. I am reaching out to express my interest in an internship opportunity at {company}.
<br>
<br>
<strong>About Me:</strong>
<br>
<br>
<strong>1. Education:</strong>
<br>
- B.Tech Major in Electronics and Communication Engineering with a Minor in AI & ML from NIT Delhi, Graduating 2025.
<br>
<br>
<strong>2. Project Experience:</strong>
<br>
- SDE Intern at Mavenir Systems Pvt Ltd
<br>
- Machine Learning Project Intern at DRDO - LRDE
<br>
- Big Data Analytics & ML Intern at DRDO - ISSA
<br>
- AI Project Intern at Ministry of Electronics & IT, Govt. of India
<br>
- Full Stack Web Development Intern at CYRAN AI Solutions, IIT Delhi
<br>
<br>
<strong>3. Technical Skills:</strong>
<br>
- Programming Languages: C++, Python, JavaScript
<br>
- Machine Learning & AI: PyTorch, TensorFlow, Neural Networks, NLP, Computer Vision
<br>
- Web Development: MongoDB, MySQL, Express.js, Node.js, CSS
<br>
- Big Data & DevOps: Apache Kafka, Apache Spark
<br>
- Frameworks & Libraries: Streamlit, JQuery, Scikit-Learn, Pandas, Numpy, Seaborn
<br>
<br>
<strong>4. Achievements:</strong>
<br>
- LeetCode Rating: 1930+ (Knight ranked)
<br>
- Selected for Amazon ML School 2024
<br>
- Secured 98.4th Percentile out of 1.1 million candidates in JEE Mains 2021
<br>
<br>
I would be thrilled to discuss how my background, skills, and projects align with the goals of {company}. If you're available, I would love to schedule a call to explore this opportunity further.
<br>
<br>
Thank you for your time and consideration. I look forward to the possibility of contributing to {company}.
<br>
<br>
Please find my resume attached. You can also connect with me on:
<br>
<a href="{linkedin_link}">LinkedIn</a> | <a href="{github_link}">GitHub</a> | <a href="{portfolio_link}">Leetcode</a>
<br>
<br>
Best Regards,
<br>
<br>
<strong>Tanishq Ranjan</strong>
<br>
4th Year Undergraduate Student
<br>
Department of Electronics and Communication Engineering
<br>
National Institute of Technology Delhi
<br>
<br>
<strong>Email:</strong> 211220058@nitdelhi.ac.in
<br>
<strong>Phone:</strong> (+91) 9113963397
<br>
<br>
====================================================================
<br>
NATIONAL INSTITUTE OF TECHNOLOGY DELHI [NITD]
"""


for index, row in df.iterrows():
    time.sleep(random.randint(1, 5))

    message = MIMEMultipart()
    message['Subject'] = f"Internship Inquiry cum Application @{row['Company']} - Tanishq Ranjan, NIT Delhi"
    message['From'] = smtp_username
    message['To'] = row['Email']

    email_body = email_body_template.format(
        name=row['First Name'], 
        company=row['Company'], 
        linkedin_link="https://in.linkedin.com/in/tanishq-ranjan-26a52740",
        github_link="https://github.com/x-INFiN1TY-x",
        portfolio_link="https://leetcode.com/u/211220058/"
    )
    message.attach(MIMEText(email_body, 'html'))

    pdf_path = "./path to pdf.pdf"
    with open(pdf_path, "rb") as pdf_file:
        pdf_attachment = MIMEApplication(pdf_file.read(), _subtype="pdf")
        pdf_attachment.add_header('Content-Disposition', f'attachment; filename={pdf_path}')
        message.attach(pdf_attachment)

    try:
        server.sendmail(smtp_username, row['Email'], message.as_string())
        logging.info(f"Email sent to {row['Email']}")
    except Exception as e:
        logging.error(f"Error sending email to {row['Email']}: {e}")

server.quit()
