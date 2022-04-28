#! python3
import pyperclip
import re

# Create Regex for phone numbers
phoneRegex = re.compile(r'''
# 415-5555-0000, 555-0000, (415) 555-0000, 555-0000 ext. 12345, x12345

(((\d\d\d) | (\(\d\d\d\)))?    # area code (optional)
(\s|-)    # first seperator
\d\d\d    # first 3 digits
-    # seperator
\d\d\d\d    # last 4 digits
(((ext(\.)?\s)|x)    # extension word-part (optional)
 (\d{2,5}))?)
''', re.VERBOSE)
# Create Regex for email addresses
emailRegex = re.compile(r'''
[a-zA-Z\d_.+]+    # name part
@                 # @ symbol
[a-zA-Z\d_.+]+    # domain name part
''', re.VERBOSE)
# Get the text off the clipboard
text = pyperclip.paste
# Extract the email/phone from this text
extracted_phone = phoneRegex.findall('''870-864-7190    brjones@southark.edu
870-864-7122	barron@southark.edu''')
extracted_email = emailRegex.findall('''870-864-7190    brjones@southark.edu
870-864-7122	barron@southark.edu''')

allPhoneNumbers = []
for phoneNumber in extracted_phone:
    allPhoneNumbers.append(phoneNumber[0])

# Copy the extracted email/phone to the clipboard.
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extracted_email)
pyperclip.copy(results)
