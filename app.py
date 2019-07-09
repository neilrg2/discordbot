import discord
import game

# Authorize and invite your bot with the server of your choice
# Replace CLIENT_ID and PERMISSION_INT with your own
# https://discordapp.com/oauth2/authorize?client_id={CLIENT_ID}&scope=bot&permissions={PERMISSION_INT}

# Create txt file to store & read token from which will be stored in a variable
with open('token.txt', 'w') as file:
    file.write('{YOUR OWN TOKEN}')  # Enter your own token here

bot_token = open('token.txt').read()

discord_client = discord.Client()

@discord_client.event
async def on_ready():   # Method gets called when bot starts up
    print(f'Logged in as: {discord_client.user}')

@discord_client.event
async def on_message(message):
    print(f'{message.channel}: {message.author}: {message.author.name}: {message.content}')
    if (str(message.content).lower() == 'test'):

        today_games = game.games_today()
        await message.channel.send(today_games)

discord_client.run(bot_token)