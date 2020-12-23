###############################################
# This is the main file that contains all the #
# functionalities related to the discord bot  #
###############################################

from run import keep_alive
import os
import discord
from dotenv import load_dotenv
from db import update_search_history, retrieve_search
from google_search import search

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user.name} with id: {client.user.id} is connected!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    channel = message.channel

    # Initial Hey
    if message.content.lower().startswith('hi'):
        response = 'Hey {0.author.mention}'.format(message)
        await channel.send(response)

    # Search functionality: Search for query using www.google.com
    if message.content.startswith('!google'):
        query = message.content.split(None, 1)[1]
        update_search_history(query)  # Add the "query" to the search history
        # returns with top five results for the "query"
        results = search(query)  # get top five search results

        # Handling for no results found
        if results:
            links = ' \n'.join(results)
            msg = 'Hello {}, you searched for "{}". The top five results are: \n {}'.format(
                message.author.mention, query, links)
        else:
            msg = 'Hello {}, you searched for "{}". \n Sorry, no matching links found.'.format(
                message.author.mention, query)
        await message.channel.send(msg)

    # Returns history if related query was already searched
    if message.content.startswith('!recent'):
        words = message.content.split("!recent ", 1)[1]
        response = retrieve_search(words)
        print("Response from search_history", response)

        if len(response):
            if len(response) > 1:
                for res in response:
                    await channel.send(res)
            else:
                await channel.send(response)
        else:
            response = "No search result found related to {}".format(words)
            await channel.send(response)


keep_alive()
client.run(TOKEN)
