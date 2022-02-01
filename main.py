from bs4 import BeautifulSoup
import requests

url = 'https://www.basketball-reference.com/leagues/NBA_2022_per_game.html'

r = requests.get(url)

html_text = r.text

soup = BeautifulSoup(html_text, 'lxml')

tbl = soup.find('table')

for tr in tbl.find_all('tr', class_='full_table'):

    player_name = tr.find('td', attrs={'class': 'left', 'data-stat': 'player'}).text
    player_points = tr.find('td', attrs={'class': 'right', 'data-stat': 'pts_per_g'}).text
    player_assists = tr.find('td', attrs={'class': 'right', 'data-stat': 'ast_per_g'}).text
    player_rebounds = tr.find('td', attrs={'class': 'right', 'data-stat': 'trb_per_g'}).text
    player_blocks = tr.find('td', attrs={'class': 'right', 'data-stat': 'blk_per_g'}).text
    player_steals = tr.find('td', attrs={'class': 'right', 'data-stat': 'stl_per_g'}).text
    player_turnovers = tr.find('td', attrs={'class': 'right', 'data-stat': 'tov_per_g'}).text

    print(f'Name: {player_name}  PPG: {player_points}  APG: {player_assists}  RBG: {player_rebounds} BPG: {player_blocks} STL: {player_steals}  TOV: {player_steals}\n')

    # if player_name is not None and player_points is not None and player_rebounds is not None and player_assists is not None:




















