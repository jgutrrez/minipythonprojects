import requests
from bs4 import BeautifulSoup

def scrape_web_dev_languages():
    url = 'https://en.wikipedia.org/wiki/List_of_programming_languages'
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        table = soup.find('table', {'class': 'wikitable'})
        
        if table:
            languages = []
            rows = table.find_all('tr')
            
            for row in rows[1:]:  # Skip the header row
                columns = row.find_all('td')
                language = columns[2].get_text().strip()
                
                # Some rows have links, extract the text if available
                if language == '':
                    link = columns[2].find('a')
                    if link:
                        language = link.get_text().strip()
                        
                languages.append(language)
            
            return languages
        else:
            print("Table not found on the page.")
    else:
        print(f"Error {response.status_code}: Unable to fetch the page.")
    
    return None

if __name__ == "__main__":
    web_dev_languages = scrape_web_dev_languages()
    if web_dev_languages:
        print("Web Development Languages:")
        for idx, language in enumerate(web_dev_languages, 1):
            print(f"{idx}. {language}")
            