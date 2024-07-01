from django.test import TestCase

# Create your tests here.
#TEST------
def get_previous_matches_soccerway(team_country, team_name, team_id):
    url = urls['soccerway'].format(team_country=team_country.lower(), team_name=team_name.lower().replace(' ', '-'), team_id=team_id)
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Debug: Print the entire HTML content
        print(soup.prettify())

        matches = []
        for match in soup.select('div.match-info'):
            date = match.select_one('span.date').text.strip()
            teams = match.select_one('span.teams').text.strip()
            result = match.select_one('span.result').text.strip()
            league_position = match.select_one('span.league-position').text.strip()  # Adjust according to actual HTML structure
            matches.append({
                'date': date,
                'opponents': teams,
                'result': result,
                'league_position': league_position
            })
        
        # Debug: Print the extracted matches
        print(matches)

        return matches
    except RequestException as e:
        print(f"Error fetching data from Soccerway: {e}")
        return []

#--------