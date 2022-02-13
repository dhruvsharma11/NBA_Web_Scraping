from bs4 import BeautifulSoup
import pandas as pd
import requests
from displayfunction import display

url = 'https://www.basketball-reference.com/leagues/NBA_2022_per_game.html'
r = requests.get(url)
html_text = r.text
soup = BeautifulSoup(html_text, 'lxml')
tbl = soup.find('table')

choice = ['P', 'A', 'R', 'B', 'S', 'T', 'POINT', 'POINTS', 'REBOUND', 'REBOUNDS', 'ASSIST', 'ASSISTS', 'BLOCK',
          'BLOCKS', 'STEAL', 'STEALS', 'TURNOVER', 'TURNOVERS']

while True:
    print(
        'Points \'P\', Assists \'A\', Rebounds \'R\', Blocks \'B\', Steals \'S\', Turnovers \'T\'\n'
        'What stat would you like to filter for?')
    compare_stat = input('>')
    compare_stat = compare_stat.upper()
    if compare_stat in choice:
        break
    else:
        print('Please enter a valid stat line!')

valid_num = False
while not valid_num:
    try:
        filter_num = float(input('What is your ' + compare_stat + ' filter number: '))
        if compare_stat.upper() == 'P' and 0 <= filter_num <= 35:
            valid_num = True
        elif compare_stat.upper() == 'A' and 0 <= filter_num <= 20:
            valid_num = True
        elif compare_stat.upper() == 'R' and 0 <= filter_num <= 20:
            valid_num = True
        elif compare_stat.upper() == 'B' and 0 <= filter_num <= 10:
            valid_num = True
        elif compare_stat.upper() == 'S' and 0 <= filter_num <= 10:
            valid_num = True
        elif compare_stat.upper() == 'T' and 0 <= filter_num <= 10:
            valid_num = True
    except ValueError:
        print('Please enter a valid number...')
    except TypeError:
        print('Please enter a valid number...')


def data_filter(filter_type):
    for tr in tbl.find_all('tr', class_='full_table'):
        if filter_type.upper() == 'P':
            compare_points = float(
                tr.find('td', attrs={'class': 'right', 'data-stat': 'pts_per_g'}).text) >= filter_num
            if compare_points:
                # player_index = tr.find('th', attrs={'class': 'right', 'data-stat': 'ranker'}).text
                player_name = tr.find('td', attrs={'class': 'left', 'data-stat': 'player'}).text
                player_points = tr.find('td', attrs={'class': 'right', 'data-stat': 'pts_per_g'}).text
                player_assists = tr.find('td', attrs={'class': 'right', 'data-stat': 'ast_per_g'}).text
                player_rebounds = tr.find('td', attrs={'class': 'right', 'data-stat': 'trb_per_g'}).text
                player_blocks = tr.find('td', attrs={'class': 'right', 'data-stat': 'blk_per_g'}).text
                player_steals = tr.find('td', attrs={'class': 'right', 'data-stat': 'stl_per_g'}).text
                player_turnovers = tr.find('td', attrs={'class': 'right', 'data-stat': 'tov_per_g'}).text

                data = {'Name': [player_name],
                        'PPG': [player_points],
                        'APG': [player_assists],
                        'RBG': [player_rebounds],
                        'BPG': [player_blocks],
                        'STL': [player_steals],
                        'TOV': [player_turnovers]}

                df = pd.DataFrame(data)
                # file_name = 'NBA_Web_Scraping.xlsx'
                # df.to_excel(file_name)

                for i in range(len(df)):
                    print(df.iloc[i, 0], df.iloc[i, 1], df.iloc[i, 2], df.iloc[i, 3], df.iloc[i, 4], df.iloc[i, 5], df.iloc[i, 6])
                    file_name = 'NBA_Web_Scraping.xlsx'
                    df.to_excel(file_name)

        elif filter_type.upper() == 'A':
            compare_assists = float(
                tr.find('td', attrs={'class': 'right', 'data-stat': 'ast_per_g'}).text) >= filter_num
            if compare_assists:
                player_name = tr.find('td', attrs={'class': 'left', 'data-stat': 'player'}).text
                player_points = tr.find('td', attrs={'class': 'right', 'data-stat': 'pts_per_g'}).text
                player_assists = tr.find('td', attrs={'class': 'right', 'data-stat': 'ast_per_g'}).text
                player_rebounds = tr.find('td', attrs={'class': 'right', 'data-stat': 'trb_per_g'}).text
                player_blocks = tr.find('td', attrs={'class': 'right', 'data-stat': 'blk_per_g'}).text
                player_steals = tr.find('td', attrs={'class': 'right', 'data-stat': 'stl_per_g'}).text
                player_turnovers = tr.find('td', attrs={'class': 'right', 'data-stat': 'tov_per_g'}).text

                data = {'Name': [player_name],
                        'PPG': [player_points],
                        'APG': [player_assists],
                        'RBG': [player_rebounds],
                        'BPG': [player_blocks],
                        'STL': [player_steals],
                        'TOV': [player_turnovers]}

                df = pd.DataFrame(data)
                print(df)

        elif filter_type.upper() == 'R':
            compare_rebounds = float(
                tr.find('td', attrs={'class': 'right', 'data-stat': 'trb_per_g'}).text) >= filter_num
            if compare_rebounds:
                player_name = tr.find('td', attrs={'class': 'left', 'data-stat': 'player'}).text
                player_points = tr.find('td', attrs={'class': 'right', 'data-stat': 'pts_per_g'}).text
                player_assists = tr.find('td', attrs={'class': 'right', 'data-stat': 'ast_per_g'}).text
                player_rebounds = tr.find('td', attrs={'class': 'right', 'data-stat': 'trb_per_g'}).text
                player_blocks = tr.find('td', attrs={'class': 'right', 'data-stat': 'blk_per_g'}).text
                player_steals = tr.find('td', attrs={'class': 'right', 'data-stat': 'stl_per_g'}).text
                player_turnovers = tr.find('td', attrs={'class': 'right', 'data-stat': 'tov_per_g'}).text

                data = {'Name': [player_name],
                        'PPG': [player_points],
                        'APG': [player_assists],
                        'RBG': [player_rebounds],
                        'BPG': [player_blocks],
                        'STL': [player_steals],
                        'TOV': [player_turnovers]}

                df = pd.DataFrame(data)
                print(df)

        elif filter_type.upper() == 'B':
            compare_blocks = float(
                tr.find('td', attrs={'class': 'right', 'data-stat': 'blk_per_g'}).text) >= filter_num
            if compare_blocks:
                player_name = tr.find('td', attrs={'class': 'left', 'data-stat': 'player'}).text
                player_points = tr.find('td', attrs={'class': 'right', 'data-stat': 'pts_per_g'}).text
                player_assists = tr.find('td', attrs={'class': 'right', 'data-stat': 'ast_per_g'}).text
                player_rebounds = tr.find('td', attrs={'class': 'right', 'data-stat': 'trb_per_g'}).text
                player_blocks = tr.find('td', attrs={'class': 'right', 'data-stat': 'blk_per_g'}).text
                player_steals = tr.find('td', attrs={'class': 'right', 'data-stat': 'stl_per_g'}).text
                player_turnovers = tr.find('td', attrs={'class': 'right', 'data-stat': 'tov_per_g'}).text

                data = {'Name': [player_name],
                        'PPG': [player_points],
                        'APG': [player_assists],
                        'RBG': [player_rebounds],
                        'BPG': [player_blocks],
                        'STL': [player_steals],
                        'TOV': [player_turnovers]}

                df = pd.DataFrame(data)
                print(df)
        elif filter_type.upper() == 'S':
            compare_steals = float(
                tr.find('td', attrs={'class': 'right', 'data-stat': 'stl_per_g'}).text) >= filter_num
            if compare_steals:
                player_name = tr.find('td', attrs={'class': 'left', 'data-stat': 'player'}).text
                player_points = tr.find('td', attrs={'class': 'right', 'data-stat': 'pts_per_g'}).text
                player_assists = tr.find('td', attrs={'class': 'right', 'data-stat': 'ast_per_g'}).text
                player_rebounds = tr.find('td', attrs={'class': 'right', 'data-stat': 'trb_per_g'}).text
                player_blocks = tr.find('td', attrs={'class': 'right', 'data-stat': 'blk_per_g'}).text
                player_steals = tr.find('td', attrs={'class': 'right', 'data-stat': 'stl_per_g'}).text
                player_turnovers = tr.find('td', attrs={'class': 'right', 'data-stat': 'tov_per_g'}).text

                data = {'Name': [player_name],
                        'PPG': [player_points],
                        'APG': [player_assists],
                        'RBG': [player_rebounds],
                        'BPG': [player_blocks],
                        'STL': [player_steals],
                        'TOV': [player_turnovers]}

                df = pd.DataFrame(data)
                print(df)
        elif filter_type.upper() == 'T':
            compare_turnovers = float(
                tr.find('td', attrs={'class': 'right', 'data-stat': 'tov_per_g'}).text) >= filter_num
            if compare_turnovers:
                player_name = tr.find('td', attrs={'class': 'left', 'data-stat': 'player'}).text
                player_points = tr.find('td', attrs={'class': 'right', 'data-stat': 'pts_per_g'}).text
                player_assists = tr.find('td', attrs={'class': 'right', 'data-stat': 'ast_per_g'}).text
                player_rebounds = tr.find('td', attrs={'class': 'right', 'data-stat': 'trb_per_g'}).text
                player_blocks = tr.find('td', attrs={'class': 'right', 'data-stat': 'blk_per_g'}).text
                player_steals = tr.find('td', attrs={'class': 'right', 'data-stat': 'stl_per_g'}).text
                player_turnovers = tr.find('td', attrs={'class': 'right', 'data-stat': 'tov_per_g'}).text

                data = {'Name': [player_name],
                        'PPG': [player_points],
                        'APG': [player_assists],
                        'RBG': [player_rebounds],
                        'BPG': [player_blocks],
                        'STL': [player_steals],
                        'TOV': [player_turnovers]}

                df = pd.DataFrame(data)
                print(df)


data_filter(compare_stat)
