from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from requests.exceptions import RequestException

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

urls = {
    'soccerway': 'https://ke.soccerway.com/teams/{team_country}/{team_name}/{team_id}/',
    'sofascore': 'https://www.sofascore.com/team/football/{team_name}/{team_id}',
    'fctables': 'https://www.fctables.com/teams/{team_name}-{team_id}/',
    'forebet': 'https://www.forebet.com/en/football-tips-and-predictions-for-today',
    
}

def fetch_page(url):
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return BeautifulSoup(response.content, 'html.parser')
    except RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        return None


#get team ids
#use Google search to find the team page URLs on each respective website and 
# then extract the team IDs from those URLs
def get_sofascore_team_id(team_name):
    search_url = f"https://www.google.com/search?q={team_name}+site:sofascore.com"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find the first result link that leads to SofaScore
    link = soup.find('a', href=True)
    if link:
        href = link['href']
        start = href.find('/team/')
        if start != -1:
            team_info = href[start:]
            team_id = team_info.split('/')[-1]
            return team_id
    #return None
    return team_id 

def get_soccerway_team_id(team_country, team_name):
    search_url = f"https://www.google.com/search?q={team_country}+{team_name}+site:soccerway.com"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find the first result link that leads to Soccerway
    link = soup.find('a', href=True)
    if link:
        href = link['href']
        start = href.find('/teams/')
        if start != -1:
            team_info = href[start:]
            team_id = team_info.split('/')[-2]
            return team_id
    #return None
    return team_id 

def get_sofascore_team_id(team_name):
    search_url = f"https://www.google.com/search?q={team_name}+site:sofascore.com"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find the first result link that leads to SofaScore
    link = soup.find('a', href=True)
    if link:
        href = link['href']
        start = href.find('/team/')
        if start != -1:
            team_info = href[start:]
            team_id = team_info.split('/')[-1]
            return team_id
    #return None
    return team_id 

def get_fctables_team_id(team_name):
    search_url = f"https://www.google.com/search?q={team_name}+site:fctables.com"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find the first result link that leads to FC Tables
    link = soup.find('a', href=True)
    if link:
        href = link['href']
        start = href.find('/teams/')
        if start != -1:
            team_info = href[start:]
            team_id = team_info.split('-')[-1].split('.')[0]
            return team_id
    #return None
    return team_id 
#-----end of team_ids

#get previous matches
def get_previous_matches_soccerway(team_country, team_name, team_id):
    #team_id = get_soccerway_team_id(team_country, team_name)
    url = urls['soccerway'].format(team_country=team_country.lower(), team_name=team_name.lower().replace(' ', '-'), team_id=team_id)
    soup = fetch_page(url)
    if soup is None:
        return []
    
    matches = []
    for match in soup.select('div.match-info'):
        date = match.select_one('span.date').text.strip()
        teams = match.select_one('span.teams').text.strip()
        result = match.select_one('span.result').text.strip()
        matches.append((date, teams, result))
    return matches[:10]  # Return the last 10 matches



#get current form
def get_current_form_sofascore(team_name, team_id):
    #team_id = get_sofascore_team_id(team_name)
    url = urls['sofascore'].format(team_name=team_name.lower().replace(' ', '-'), team_id=team_id)
    soup = fetch_page(url)
    if soup is None:
        return []
    
    form = []
    for form_icon in soup.select('.form-icon'):
        form.append(form_icon['title'])
    return form

#get player statistics
def get_player_statistics_fctables(team_name, team_id):
    #team_id = get_fctables_team_id(team_name)
    url = urls['fctables'].format(team_name=team_name.lower().replace(' ', '-'), team_id=team_id)
    soup = fetch_page(url)
    if soup is None:
        return []
    
    player_stats = []
    for player in soup.select('.player-statistics .player'):
        name = player.select_one('.player-name').text.strip()
        goals = player.select_one('.goals').text.strip()
        assists = player.select_one('.assists').text.strip()
        yellow_cards = player.select_one('.yellow-cards').text.strip()
        red_cards = player.select_one('.red-cards').text.strip()
        player_stats.append((name, goals, assists, yellow_cards, red_cards))
    return player_stats

#get team stats
def get_team_statistics(home_team_country, home_team, home_team_id, away_team_country, away_team, away_team_id):
    home_team_matches = get_previous_matches_soccerway(home_team_country, home_team, home_team_id)
    away_team_matches = get_previous_matches_soccerway(away_team_country, away_team, away_team_id)

    home_team_form = get_current_form_sofascore(home_team, home_team_id)
    away_team_form = get_current_form_sofascore(away_team, away_team_id)

    home_team_players = get_player_statistics_fctables(home_team, home_team_id)
    away_team_players = get_player_statistics_fctables(away_team, away_team_id)

    statistics = {
        'home_team_previous_matches': home_team_matches,
        'away_team_previous_matches': away_team_matches,
        'home_team_form': home_team_form,
        'away_team_form': away_team_form,
        'home_team_players': home_team_players,
        'away_team_players': away_team_players,
    }

    return statistics
 #forebet 
def forebet_predictions(request):
    source = requests.get('https://www.forebet.com/en/football-tips-and-predictions-for-today').text
    soup = BeautifulSoup(source, 'html.parser')
    predictions = []

    teams = soup.find_all('a', class_='tnmscn')
    for team in teams:
        try:
            hometeam = team.find('span', class_='homeTeam').text.strip()
            predictedscore = team.select_one('div.ex_sc.tabonly').text.strip()
            awayteam = team.find('span', class_='awayTeam').text.strip()
            date = team.find('span', class_='date_bah').text.strip()
            #location = team.find('address', class_='content').text.strip()
            #weather = team.find('span', class_='wnums').text.strip()
            predictions.append({
                'hometeam': hometeam,
                'predictedscore': predictedscore,
                'awayteam': awayteam,
                'date': date,
                #'location': location,
                #'weather': weather
            })
            print(predictions)
        except AttributeError:
            continue

    return render(request, 'stats/predictions.html', {'predictions': predictions})#the predictions list is passed to html


def index(request):
    return render(request, 'stats/index.html')

def results(request):
    home_team_country = request.GET.get('home_team_country')
    home_team = request.GET.get('home_team')
    home_team_id = "your_home_team_id"  # Replace with actual logic to fetch the ID
    away_team_country = request.GET.get('away_team_country')
    away_team = request.GET.get('away_team')
    away_team_id = "your_away_team_id"  # Replace with actual logic to fetch the ID
    match_date = request.GET.get('match_date')

    statistics = get_team_statistics(home_team_country, home_team, home_team_id, away_team_country, away_team, away_team_id)

    return render(request, 'stats/results.html', {'statistics': statistics, 'home_team': home_team, 'away_team': away_team, 'match_date': match_date})
