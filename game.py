import mlbgame
import datetime

date_now = datetime.datetime.now()

year = date_now.year
month = date_now.month
day = date_now.day
hour = date_now.hour
minute = date_now.minute

# Returns today's games, scores, and first pitch times
def games_today():
    today_games = f'```MLB Games Today ({month}/{day}/{year}):\n'
    games = tuple(mlbgame.day(year, month, day))
    
    # No games for specified date
    if not games:
        today_games += 'No Games Today. So Sad...'
        return today_games

    for game in games:
        game_status = game.game_status
        away_team = game.away_team
        home_team = game.home_team
        start_time = game.game_start_time

        # Game has not started
        if game_status == 'PRE_GAME':
            today_games += f'{away_team} at {home_team} - {start_time}\n'
        
        # Game has ended
        elif game_status == 'FINAL':
            today_games += f'{str(game)} - {game_status}\n'
        
        # Game is in progress
        elif game_status == 'IN_PROGRESS':
            
            box_score = mlbgame.game.box_score(game.game_id)
            inning = tuple(box_score)[-1]

            # Check if home team is batting
            if box_score[inning]['home'] == type(str):
                current_inning = f'TOP {inning}'
            
            else:
                current_inning = f'BOT {inning}'

            today_games += f'{away_team} {game.away_team_runs} at {home_team} {game.home_team_runs} - {current_inning}\n'

        # TODO: Game has been delayed or postponed
        else:
            pass
    
    return today_games + '```'

# Returns games, scores, and first pitch times on specified date
def games_on_date(month, day, year):
    specified_date_games = f'MLB Games on ({month}/{day}/{year}):\n'
    games = mlbgame.day(year, month, day)

    # No games for specified date
    if not games:
        specified_date_games += f'No Games on {month}/{day}/{year}. How unfortunate...'
        return specified_date_games

    for game in games:
        game_status = game.game_status
        away_team = game.away_team
        home_team = game.home_team
        start_time = game.game_start_time

        # Game has not started
        if game_status == 'PRE_GAME':
            specified_date_games += f'{away_team} at {home_team} - {start_time}\n'
        
        # Game has ended
        elif game_status == 'FINAL':
            specified_date_games += f'{str(game)} - {game_status}\n'
        
        # elif
        # TODO: Game has been delayed or postponed

        # Game is in progress
        else:
            pass
    
    return specified_date_games
