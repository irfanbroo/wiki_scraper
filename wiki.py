import requests
from bs4 import BeautifulSoup


def scrap_wiki(topic):
    
    url = f"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch={topic}&utf8=&format=json"

    response1 = requests.get(url)

    if response1.status_code == 200:
        search_result = response1.json()

        if search_result['query']['search']:
            page_title = search_result['query']['search'][0]['title']
            page_url = f"https://en.wikipedia.org/wiki/{page_title.replace(' ', '_')}"
            page_response = requests.get(page_url)


            if page_response.status_code == 200:
                # Parse the Wikipedia page with BeautifulSoup
                soup = BeautifulSoup(page_response.text, 'html.parser')

                # Extracting title
                title = soup.find("h1", id="firstHeading").text

                # Extracting the summary (first paragraph)
                summary = soup.find("p").text.strip()

                # Extracting table of contents
                toc = soup.find("div", id="toc")
                if toc:
                    table_of_contents = [li.text for li in toc.find_all("span", class_="toctext")]
                else:
                    table_of_contents = "No Table of Contents found."





                # Now, lets display all the stuffs 

                print(f"\n Title: {title}\n")
                print(f"Summary: {summary} \n")
                print(f"Table of Contents: {table_of_contents}\n")

            else:
                print("No results for the given topic")
        else:
            print("Failed to fetch search results")
                


                
        
# Input the topic to search



topic = input("Enter a Wikipedia topic: ")

scrap_wiki(topic)
