
# Automate Cold Email

A Python script to automate sending cold emails with attachments.

## Getting Started

### Prerequisites

* Python 3.6+
* `pandas`, `python-dotenv`, and `openpyxl` libraries (install with `pip install pandas python-dotenv openpyxl`)
* A CSV file with names, company names, and email IDs of people you want to cold email
* A PDF document to attach to the email (e.g., a resume)
* A Gmail account with a password (see instructions below to set up a password for your account)

### Setup

1. Clone this repository to your local machine.
2. Create a new CSV file with the following column names: `First Name`, `Company`, `Email`. You can use Apollo.io to get emails.
3. Create a new PDF document to attach to the email (e.g., a resume).
4. Create a new file named `.env` in the root of the repository with the following format:
   ```
   SMTP_USERNAME="your email"
   SMTP_PASSWORD="your password"
   ```
   Replace `your email` and `your password` with your actual Gmail account credentials.

### Instructions

1. Update the `email_body_template` variable in the `index.py` file to match your cold email template. You can use HTML email templates to add embedded links to your email.
2. Update the file paths to your CSV file and PDF document in the `index.py` file (lines 11 and 48).
3. Run the script with `python index.py`.

### Troubleshooting

* If you encounter any issues, you can open an issue on this repository.

### Setting up a password for your Gmail account

To set up a password for your Gmail account, follow these steps:

1. Go to the [Google Account settings page](https://myaccount.google.com/)
2. Click on "Security" from the left-hand menu.
3. Scroll down to the "Signing into Google" section.
4. Click on "App passwords".
5. Select "Mail" as the app type.
6. Select "Other (Custom name)" as the device type.
7. Enter a name for the app password (e.
8. Click on "Generate".
9. Copy the generated password and paste it into your `.env` file.

Steps to get this password for your Gmail account - [link](https://www.youtube.com/shorts/n9Ooxum-iUo)



