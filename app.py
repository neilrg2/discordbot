import discord

# Authorize and invite your bot with the server of your choice
# Replace CLIENT_ID and PERMISSION_INT with your own
# https://discordapp.com/oauth2/authorize?client_id={CLIENT_ID}&scope=bot&permissions={PERMISSION_INT}

# Create txt file to store & read token from which will be stored in a variable
with open('token.txt', 'w') as file:
    file.write('{YOUR OWN TOKEN}')  # Enter your own token here

bot_token = open('token.txt').read()

discord_client = discord.Client()

discord_client.run(bot_token)