from bs4 import BeautifulSoup
import requests

url = 'https://www.basketball-reference.com/leagues/NBA_2022_per_game.html'

r = requests.get(url)

html_text = r.text

soup = BeautifulSoup(html_text, 'lxml')

tbl = soup.find('table')

print(
    'Points \'P\', Assists \'A\', Rebounds \'R\', Blocks \'B\', Steals \'S\', Turnovers \'T\'\n'
    'What stat would you like to filter for?')
compare_stat = input('>')

if compare_stat.upper() == 'P':
    print('What is your points filter number?')
    point_filter = float(input('>'))
elif compare_stat.upper() == 'A':
    print('What is your Assists filter number?')
    assist_filter = float(input('>'))
elif compare_stat.upper() == 'R':
    print('What is your Rebounds filter number?')
    rebound_filter = float(input('>'))
elif compare_stat.upper() == 'B':
    print('What is your Blocks filter number?')
    block_filter = float(input('>'))
elif compare_stat.upper() == 'S':
    print('What is your Steals filter number?')
    steal_filter = float(input('>'))
elif compare_stat.upper() == 'T':
    print('What is your Turnovers filter number?')
    turnover_filter = float(input('>'))


def data_filter(filter_type):
    for tr in tbl.find_all('tr', class_='full_table'):
        if filter_type.upper() == 'P':
            compare_points = float(
                tr.find('td', attrs={'class': 'right', 'data-stat': 'pts_per_g'}).text) >= point_filter
            if compare_points:
                player_name = tr.find('td', attrs={'class': 'left', 'data-stat': 'player'}).text
                player_points = tr.find('td', attrs={'class': 'right', 'data-stat': 'pts_per_g'}).text
                player_assists = tr.find('td', attrs={'class': 'right', 'data-stat': 'ast_per_g'}).text
                player_rebounds = tr.find('td', attrs={'class': 'right', 'data-stat': 'trb_per_g'}).text
                player_blocks = tr.find('td', attrs={'class': 'right', 'data-stat': 'blk_per_g'}).text
                player_steals = tr.find('td', attrs={'class': 'right', 'data-stat': 'stl_per_g'}).text
                player_turnovers = tr.find('td', attrs={'class': 'right', 'data-stat': 'tov_per_g'}).text

                print(
                    f'Name: {player_name}  PPG: {player_points}  APG: {player_assists}  RBG: {player_rebounds} BPG: {player_blocks} STL: {player_steals}  TOV: {player_turnovers}\n')
        elif filter_type.upper() == 'A':
            compare_assists = float(
                tr.find('td', attrs={'class': 'right', 'data-stat': 'ast_per_g'}).text) >= assist_filter
            if compare_assists:
                player_name = tr.find('td', attrs={'class': 'left', 'data-stat': 'player'}).text
                player_points = tr.find('td', attrs={'class': 'right', 'data-stat': 'pts_per_g'}).text
                player_assists = tr.find('td', attrs={'class': 'right', 'data-stat': 'ast_per_g'}).text
                player_rebounds = tr.find('td', attrs={'class': 'right', 'data-stat': 'trb_per_g'}).text
                player_blocks = tr.find('td', attrs={'class': 'right', 'data-stat': 'blk_per_g'}).text
                player_steals = tr.find('td', attrs={'class': 'right', 'data-stat': 'stl_per_g'}).text
                player_turnovers = tr.find('td', attrs={'class': 'right', 'data-stat': 'tov_per_g'}).text

                print(
                    f'Name: {player_name}  PPG: {player_points}  APG: {player_assists}  RBG: {player_rebounds} BPG: {player_blocks} STL: {player_steals}  TOV: {player_turnovers}\n')
        elif filter_type.upper() == 'R':
            compare_rebounds = float(
                tr.find('td', attrs={'class': 'right', 'data-stat': 'trb_per_g'}).text) >= rebound_filter
            if compare_rebounds:
                player_name = tr.find('td', attrs={'class': 'left', 'data-stat': 'player'}).text
                player_points = tr.find('td', attrs={'class': 'right', 'data-stat': 'pts_per_g'}).text
                player_assists = tr.find('td', attrs={'class': 'right', 'data-stat': 'ast_per_g'}).text
                player_rebounds = tr.find('td', attrs={'class': 'right', 'data-stat': 'trb_per_g'}).text
                player_blocks = tr.find('td', attrs={'class': 'right', 'data-stat': 'blk_per_g'}).text
                player_steals = tr.find('td', attrs={'class': 'right', 'data-stat': 'stl_per_g'}).text
                player_turnovers = tr.find('td', attrs={'class': 'right', 'data-stat': 'tov_per_g'}).text

                print(
                    f'Name: {player_name}  PPG: {player_points}  APG: {player_assists}  RBG: {player_rebounds} BPG: {player_blocks} STL: {player_steals}  TOV: {player_turnovers}\n')
        elif filter_type.upper() == 'B':
            compare_blocks = float(
                tr.find('td', attrs={'class': 'right', 'data-stat': 'blk_per_g'}).text) >= block_filter
            if compare_blocks:
                player_name = tr.find('td', attrs={'class': 'left', 'data-stat': 'player'}).text
                player_points = tr.find('td', attrs={'class': 'right', 'data-stat': 'pts_per_g'}).text
                player_assists = tr.find('td', attrs={'class': 'right', 'data-stat': 'ast_per_g'}).text
                player_rebounds = tr.find('td', attrs={'class': 'right', 'data-stat': 'trb_per_g'}).text
                player_blocks = tr.find('td', attrs={'class': 'right', 'data-stat': 'blk_per_g'}).text
                player_steals = tr.find('td', attrs={'class': 'right', 'data-stat': 'stl_per_g'}).text
                player_turnovers = tr.find('td', attrs={'class': 'right', 'data-stat': 'tov_per_g'}).text

                print(
                    f'Name: {player_name}  PPG: {player_points}  APG: {player_assists}  RBG: {player_rebounds} BPG: {player_blocks} STL: {player_steals}  TOV: {player_turnovers}\n')
        elif filter_type.upper() == 'S':
            compare_steals = float(
                tr.find('td', attrs={'class': 'right', 'data-stat': 'stl_per_g'}).text) >= steal_filter
            if compare_steals:
                player_name = tr.find('td', attrs={'class': 'left', 'data-stat': 'player'}).text
                player_points = tr.find('td', attrs={'class': 'right', 'data-stat': 'pts_per_g'}).text
                player_assists = tr.find('td', attrs={'class': 'right', 'data-stat': 'ast_per_g'}).text
                player_rebounds = tr.find('td', attrs={'class': 'right', 'data-stat': 'trb_per_g'}).text
                player_blocks = tr.find('td', attrs={'class': 'right', 'data-stat': 'blk_per_g'}).text
                player_steals = tr.find('td', attrs={'class': 'right', 'data-stat': 'stl_per_g'}).text
                player_turnovers = tr.find('td', attrs={'class': 'right', 'data-stat': 'tov_per_g'}).text

                print(
                    f'Name: {player_name}  PPG: {player_points}  APG: {player_assists}  RBG: {player_rebounds} BPG: {player_blocks} STL: {player_steals}  TOV: {player_turnovers}\n')
        elif filter_type.upper() == 'T':
            compare_turnovers = float(
                tr.find('td', attrs={'class': 'right', 'data-stat': 'tov_per_g'}).text) >= turnover_filter
            if compare_turnovers:
                player_name = tr.find('td', attrs={'class': 'left', 'data-stat': 'player'}).text
                player_points = tr.find('td', attrs={'class': 'right', 'data-stat': 'pts_per_g'}).text
                player_assists = tr.find('td', attrs={'class': 'right', 'data-stat': 'ast_per_g'}).text
                player_rebounds = tr.find('td', attrs={'class': 'right', 'data-stat': 'trb_per_g'}).text
                player_blocks = tr.find('td', attrs={'class': 'right', 'data-stat': 'blk_per_g'}).text
                player_steals = tr.find('td', attrs={'class': 'right', 'data-stat': 'stl_per_g'}).text
                player_turnovers = tr.find('td', attrs={'class': 'right', 'data-stat': 'tov_per_g'}).text

                print(
                    f'Name: {player_name}  PPG: {player_points}  APG: {player_assists}  RBG: {player_rebounds} BPG: {player_blocks} STL: {player_steals}  TOV: {player_turnovers}\n')


data_filter(compare_stat)
