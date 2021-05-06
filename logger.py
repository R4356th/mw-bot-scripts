'''
Script for logging updates sent through Discord 
'''
import discord
from mw_api_client import Wiki
from configuration import WIKI_API_URL, WIKI_PASSWORD, WIKI_USERAGENT, WIKI_USERNAME, DISCORD_PREFIX, DISCORD_TOKEN, WIKI_LOG_REV_SUMM_PREFIX

wiki = Wiki(WIKI_API_URL, WIKI_USERAGENT)
wiki.clientlogin(WIKI_USERNAME, WIKI_PASSWORD)
print("Logged in to wiki.")

class Bot(discord.Client):
    async def on_ready(self):
        print("Logged in to Discord.")
    async def on_message(self, message):
        if message.content.startswith(DISCORD_PREFIX):
            content = message.content
            content = content.replace(DISCORD_PREFIX, "")
            page = wiki.page("Changelog")
            pagecontent = page.read()
            pagecontent += "\n" + "* ~~~~~ - " + content
            summ = WIKI_LOG_REV_SUMM_PREFIX + content
            page.edit(pagecontent, summ)

client = Bot()
client.run(DISCORD_TOKEN)
