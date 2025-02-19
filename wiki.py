import requests
from bs4 import BeautifulSoup
import re
from rich.console import Console

console = Console()

# Banner
console.print(
    """[medium_spring_green]
  ______                                        ______                                    __       
 /      \                                      /      \                                  |  \      
|  $$$$$$\  ______    ______   _______        |  $$$$$$\  ______   ______   __   __   __ | $$      
| $$  | $$ /      \  /      \ |       \       | $$   \$$ /      \ |      \ |  \ |  \ |  \| $$      
| $$  | $$|  $$$$$$\|  $$$$$$\| $$$$$$$\      | $$      |  $$$$$$\ \$$$$$$\| $$ | $$ | $$| $$      
| $$  | $$| $$  | $$| $$    $$| $$  | $$      | $$   __ | $$   \$$/      $$| $$ | $$ | $$| $$      
| $$__/ $$| $$__/ $$| $$$$$$$$| $$  | $$      | $$__/  \| $$     |  $$$$$$$| $$_/ $$_/ $$| $$      
 \$$    $$| $$    $$ \$$     \| $$  | $$       \$$    $$| $$      \$$    $$ \$$   $$   $$| $$      
  \$$$$$$ | $$$$$$$   \$$$$$$$ \$$   \$$        \$$$$$$  \$$       \$$$$$$$  \$$$$$\$$$$  \$$      
          | $$                                                                                     
          | $$                                                                                     
           \$$                                                               [bold]v 1.0.0[/bold]  
    [/medium_spring_green]"""
)



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
                summary = "No summary available for this topic, lol (what did you even search)"
                for para in soup.find_all("p"):
                    if para.text.strip() and len(para.text.strip()) > 5:
                        summary = para.text.strip()
                        break

                # Extracting the first image
                image_url = "No image available for this topic"
                image_table = soup.find("table", class_="infobox") # Finding the infobox table

                if image_table:
                    image_tag = image_table.find("img") # Finding the tag of first image, for example image_tag =  <img src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Example.jpg/250px-Example.jpg" alt="Example image">
                    image_url = f"https:{image_tag['src']}" if image_tag else "No image available"
                
                else:
                    print("No image available")

                # Extracting related links
                links = []

                for link in soup.find_all("a", href=True):
                    href = link['href']
                    if re.match(r"^/wiki/[^:]+$", href):  # Ignore non-article links
                        links.append(f"https://en.wikipedia.org{href}")

                # Fetching last edited date
                last_edit = soup.find("li", id="footer-info-lastmod")
                last_edit_date = last_edit.text.strip() if last_edit else "Cannot find last edited date"


                
                

                # Now, lets display all the stuffs
                console.print("\n" + "=" * 60, style="bold yellow")
                console.print(f"📌 [bold cyan]Title:[/bold cyan] {title}\n")
                console.print(f"📖 [bold green]Summary:[/bold green] {summary}\n")
                console.print(f"🖼 [bold magenta]Image:[/bold magenta] {image_url}\n")
                console.print(f"🕒 [bold blue]{last_edit_date}[/bold blue]\n")
                console.print("🔗 [bold red]Related Links:[/bold red]")
                for lnk in links[:5]:  # Show only the first 5 links
                    console.print(lnk, style="cyan")
                console.print("=" * 60 + "\n", style="bold yellow")

            else:
                console.print("❌ Failed to fetch the Wikipedia page.", style="bold red")
        else:
            console.print("❌ No results found for the given topic.", style="bold red")
    else:
        console.print("❌ Failed to fetch search results from Wikipedia.", style="bold red")


                
                


                
        
# Input the topic to search



topic = input("Enter a Wikipedia topic: ")

scrap_wiki(topic)
