# **Open Crawler - Wikipedia Scraper**  

## 📌 **Overview**  
My first ever web crawler. In order to keep this simple I used wikipedia page to scrape. I hope this will be of some help to people who are new to web scraping and can get to know how one works in the most basic level.   
Open Crawler is a **command-line Wikipedia scraper** that fetches details about a given topic using the **Wikipedia API and BeautifulSoup**. It retrieves the **title, summary, main image, last edited date, and related Wikipedia links** and displays them in a beautifully styled format using the **`rich`** library.  

The results are also **saved to a text file** for easy reference.  

---

## 🚀 **Features**  
✅ **Stylish ASCII Banner** – Gives a cool hacker-style feel.  
✅ **Wikipedia Search API** – Finds the most relevant page for the topic.  
✅ **BeautifulSoup Parsing** – Extracts structured data from the Wikipedia page.  
✅ **Rich Terminal Output** – Uses `rich` to add colors and emojis for a clean UI.  
✅ **Image Extraction** – Fetches the **main image** (if available).  
✅ **Related Links** – Provides useful Wikipedia links related to the topic.  
✅ **Last Edited Timestamp** – Displays when the page was last modified.  
✅ **Saves to a File** – Stores the results as a `.txt` file for later use.  

---

## 🛠 **Installation & Requirements**  
Ensure you have **Python 3.x** installed. Then, install the required dependencies:  

```bash
pip install requests beautifulsoup4 rich
```

---

## 🔥 **Usage**  
Run the script and enter a topic to search:  

```bash
python scraper.py
```

Example input:  
```
Enter a Wikipedia topic: Python programming
```

Example output:  
![Screenshot](https://github.com/irfanbroo/wiki_scraper/blob/main/Screenshot%202025-02-19%20205257.png)

```
============================================================
📌 Title: Python (programming language)
📖 Summary: Python is an interpreted, high-level and general-purpose programming language...
🖼 Image: https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg
🕒 This page was last edited on 18 February 2025, at 20:31 UTC.
🔗 Related Links:
https://en.wikipedia.org/wiki/Python_(programming_language)
https://en.wikipedia.org/wiki/Guido_van_Rossum
https://en.wikipedia.org/wiki/Software_engineering
============================================================
```
The script will also create a `Python_(programming_language).txt` file with the extracted data.

---

## 🎨 **Customization**  
- Modify the **ASCII banner** in the `console.print()` function.  
- Change the **number of related links** displayed (`links[:5]`).  
- Customize the **output file format** (currently saved as `.txt`).  

---

## 🔧 **Troubleshooting**  
1. **Getting an ImportError?**  
   → Run `pip install -r requirements.txt` to install missing packages.  
2. **No summary found?**  
   → Wikipedia pages with unconventional structures may not return summaries.  
3. **No image available?**  
   → Some topics may not have an image in the **infobox**.  

---

## 🌟 **Future Enhancements**  
- 📊 **Add a progress bar** when fetching data.  
- 📦 **Store results in JSON format** instead of `.txt`.  
- 🌍 **Support multiple languages** for Wikipedia searches.  
- 🖥 **Convert into a GUI/Desktop App** using Tkinter or PyQt.  

---

## 🎯 **Contributors & License**  
Created by **[Irfan.s]** – Feel free to modify and improve!  
📜 **License:** MIT (Free to use and modify)  

---
