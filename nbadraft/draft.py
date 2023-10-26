import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_draft_results(year):
    url = f'https://example.com/nba-draft/{year}'  # Replace with the actual URL
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f'Failed to retrieve page with status code: {response.status_code}')
        return None
    
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table', {'class': 'draft-results-table'})  # Replace with the actual class name
    
    if table is None:
        print('No draft results table found')
        return None
    
    headers = [header.text for header in table.find_all('th')]
    rows = table.find_all('tr')[1:]  # Skip header row
    data = [[cell.text for cell in row.find_all('td')] for row in rows]
    
    df = pd.DataFrame(data, columns=headers)
    df.to_csv(f'nba_draft_results_{year}.csv', index=False)
    print(f'Data saved to nba_draft_results_{year}.csv')

# Example usage
get_draft_results(2003)
