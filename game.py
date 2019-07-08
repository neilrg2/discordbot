import mlbgame
import datetime

date_now = datetime.datetime.now()

year = date_now.year
month = date_now.month
day = date_now.day

# Returns today's games, scores, and first pitch times
def games_today():
    today_games = f'MLB Games Today ({month}/{day}/{year}):\n'
    games = mlbgame.day(year, month, day)

    for game in games:
        today_games += str(game) + '\n'
    
    return today_games