from bs4 import BeautifulSoup
import pandas as pd
import requests


def point_result(filter_value, tr):
    compare_points = float(
        tr.find('td', attrs={'data-stat': 'pts_per_g'}).text) >= filter_value
    if compare_points:
        player_name = tr.find('td', attrs={'data-stat': 'player'}).text
        player_points = tr.find('td', attrs={'data-stat': 'pts_per_g'}).text
        data = {'Name': player_name,
                'PPG': player_points}
        return data
    return None


def assist_result(filter_value, tr):
    compare_assists = float(
        tr.find('td', attrs={'class': 'right', 'data-stat': 'ast_per_g'}).text) >= filter_value
    if compare_assists:
        player_name = tr.find('td', attrs={'class': 'left', 'data-stat': 'player'}).text
        player_assists = tr.find('td', attrs={'class': 'right', 'data-stat': 'ast_per_g'}).text
        data = {'Name': player_name,
                'APG': player_assists}
        return data
    return None


def rebound_result(filter_value, tr):
    compare_rebounds = float(
        tr.find('td', attrs={'class': 'right', 'data-stat': 'trb_per_g'}).text) >= filter_value
    if compare_rebounds:
        player_name = tr.find('td', attrs={'class': 'left', 'data-stat': 'player'}).text
        player_rebounds = tr.find('td', attrs={'class': 'right', 'data-stat': 'trb_per_g'}).text
        data = {'Name': player_name,
                'RBG': player_rebounds}
        return data
    return None


def block_result(filter_value, tr):
    compare_blocks = float(
        tr.find('td', attrs={'class': 'right', 'data-stat': 'blk_per_g'}).text) >= filter_value
    if compare_blocks:
        player_name = tr.find('td', attrs={'class': 'left', 'data-stat': 'player'}).text
        player_blocks = tr.find('td', attrs={'class': 'right', 'data-stat': 'blk_per_g'}).text
        data = {'Name': player_name,
                'BPG': player_blocks}
        return data
    return None


def steal_result(filter_value, tr):
    compare_steals = float(
        tr.find('td', attrs={'class': 'right', 'data-stat': 'stl_per_g'}).text) >= filter_value
    if compare_steals:
        player_name = tr.find('td', attrs={'class': 'left', 'data-stat': 'player'}).text
        player_steals = tr.find('td', attrs={'class': 'right', 'data-stat': 'stl_per_g'}).text
        data = {'Name': player_name,
                'STL': player_steals}
        return data
    return None


def turnover_result(filter_value, tr):
    compare_turnovers = float(
        tr.find('td', attrs={'class': 'right', 'data-stat': 'tov_per_g'}).text) >= filter_value
    if compare_turnovers:
        player_name = tr.find('td', attrs={'class': 'left', 'data-stat': 'player'}).text
        player_turnovers = tr.find('td', attrs={'class': 'right', 'data-stat': 'tov_per_g'}).text
        data = {'Name': player_name,
                'TOV': player_turnovers}
        return data
    return None


def data_filter(filter_type, filter_value):
    list_data = []
    url = 'https://www.basketball-reference.com/leagues/NBA_2022_per_game.html'
    r = requests.get(url)
    html_text = r.text
    soup = BeautifulSoup(html_text, 'lxml')
    tbl = soup.find('table')

    for tr in tbl.find_all('tr', class_='full_table'):
        if filter_type.upper() == 'P':
            result = (point_result(filter_value, tr))
            if result is not None:
                list_data.append(result)

        elif filter_type.upper() == 'A':
            result = (assist_result(filter_value, tr))
            if result is not None:
                list_data.append(result)

        elif filter_type.upper() == 'R':
            result = (rebound_result(filter_value, tr))
            if result is not None:
                list_data.append(result)

        elif filter_type.upper() == 'B':
            result = (block_result(filter_value, tr))
            if result is not None:
                list_data.append(result)

        elif filter_type.upper() == 'S':
            result = (steal_result(filter_value, tr))
            if result is not None:
                list_data.append(result)

        elif filter_type.upper() == 'T':
            result = (rebound_result(filter_value, tr))
            if result is not None:
                list_data.append(result)

    return list_data


def stat_filter():
    choice = ['P', 'A', 'R', 'B', 'S', 'T', 'POINT', 'POINTS', 'REBOUND', 'REBOUNDS', 'ASSIST', 'ASSISTS', 'BLOCK',
              'BLOCKS', 'STEAL', 'STEALS', 'TURNOVER', 'TURNOVERS']
    while True:
        print(
            'Points \'P\', Assists \'A\', Rebounds \'R\', Blocks \'B\', Steals \'S\', Turnovers \'T\'\n'
            'What stat would you like to filter for?')
        stat_compare = input('>')
        stat_compare = stat_compare.upper()
        if stat_compare in choice:
            return stat_compare
        else:
            print('Please enter a valid stat line!')


def number_filter(filter_stat):
    valid_num = False
    while not valid_num:
        try:
            filter_number = float(input('What is your ' + filter_stat + ' filter number: '))
            if filter_stat.upper() == 'P' and 0 <= filter_number <= 35:
                return filter_number
            elif filter_stat.upper() == 'A' and 0 <= filter_number <= 20:
                return filter_number
            elif filter_stat.upper() == 'R' and 0 <= filter_number <= 20:
                return filter_number
            elif filter_stat.upper() == 'B' and 0 <= filter_number <= 10:
                return filter_number
            elif filter_stat.upper() == 'S' and 0 <= filter_number <= 10:
                return filter_number
            elif filter_stat.upper() == 'T' and 0 <= filter_number <= 10:
                return filter_number
        except ValueError:
            print('Please enter a valid number...')
        except TypeError:
            print('Please enter a valid number...')


def to_excel(df):
    df.to_excel('NBA_Player.xlsx', sheet_name='new_sheet_name')


def main():
    compare_stat = stat_filter()
    list_data = data_filter(compare_stat, number_filter(compare_stat))
    df = pd.DataFrame(list_data)
    to_excel(df)


if __name__ == "__main__":
    main()
