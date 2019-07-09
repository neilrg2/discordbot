import discord
import game
import helper

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
    if (str(message.content).lower() == '!mlbtoday'):

        today_games = game.games_today()
        await message.channel.send(today_games)
        return
    
    # format: !mlbdate month day year
    elif ('!mlbdate' in str(message.content).lower()):

        date = str(message.content).lower().split()

        # Wrong number of arguments
        if len(date) != 4:
            await message.channel.send('Please enter the format as such: \'!mlbdate month day year\'')
            return 

        # 'month day year' format was not correct
        if date[1].isnumeric() and date[2].isnumeric() and date[3].isnumeric():
            valid_date = helper.date_check(date[1], date[2], date[3])

            # Valid date provided
            if valid_date:
                games_on_date = game.games_on_date(int(date[1]), int(date[2]), int(date[3]))
                await message.channel.send(games_on_date)
                return
            
            else:
                invalid_date = 'Here\'s a little resource for you to reference for a valid date:\n'
                invalid_date += 'https://www.timeanddate.com/calendar/months/'

                await message.channel.send(invalid_date)
                return

        wrong_format = 'Sigh. Wrong format buddy. Format: \'!mlbdate month day year\''
        await message.channel.send(wrong_format)


discord_client.run(bot_token)