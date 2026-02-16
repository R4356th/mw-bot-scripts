# Import functions and configuration (from configuration.py).
from mw_api_client import Wiki
from configuration import WIKI_API_URL, WIKI_PASSWORD, WIKI_USERNAME, WIKI_USERAGENT

# Log in.
wiki = Wiki(WIKI_API_URL, WIKI_USERAGENT)
wiki.login(WIKI_USERNAME, WIKI_PASSWORD)

if wiki.meta.csrftoken == '+\\':
    raise WikiError('Login failed. Please check your credentials.')
else:
    print('Logged in.')

# Take user input.
cat = input('Category name (without "Category:"): ')
strtoreplace = input('Text to replace: ')
strtoreplacewith = input('Text to replace with: ')
summ = input('Summary: ')

# Edit pages.
for page in wiki.category(cat).categorymembers():
    print(page.title)
    page.replace(strtoreplace, strtoreplacewith, summ)

print('Process completed.')
