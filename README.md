## automate-cold-email

### instructions to use this
- ```pip install pandas python-dotenv openpyxl```
- paste the csv file with names, company names and email ids of people you want to cold email
- make sure the column names are First Name, Company, Email
- you can use Apollo.io to get emails
- paste pdf doc like a resume you want to attach
- create a .env file and add the following
  
```
SMTP_USERNAME="your email"
SMTP_PASSWORD="your password"
```
- steps to get this password for your Gmail account - [link](https://www.youtube.com/shorts/n9Ooxum-iUo)
- change the ```email_body_template``` according to your cold email. tip :- use html email template to add embedded links to your email.
- after completing the above steps, run ```python index.py``` and let the script run.
- If any issues then you can open one.
