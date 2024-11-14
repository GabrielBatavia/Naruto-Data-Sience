# Naruto Data Science Project

## Overview
This project focuses on performing web scraping, utilizing machine learning models, and fine-tuning them for data analysis and theme classification. The primary objective is to analyze data from the Naruto universe, such as jutsus and scripts, to extract insights and categorize themes effectively. The pipeline integrates advanced techniques such as Natural Language Processing (NLP) and web crawling.

---

## Features
- **Web Scraping**:
  - Extracts data about Naruto's jutsus from [Naruto Fandom](https://naruto.fandom.com/wiki/Special:BrowseData/Jutsu).
  - Cleans data to ensure relevance by removing irrelevant sections such as trivia and videos.

- **Theme Classification**:
  - Implements `facebook/bart-large-mnli` model for zero-shot classification.
  - Identifies themes such as `friendship`, `hope`, `sacrifice`, `battle`, and more in scripts.
  - Outputs sentiment scores for themes.

- **Visualization**:
  - Generates bar plots to visualize theme distributions.

---

## Project Structure
```
├── .idea/                # IDE configuration files
├── character_network/    # Tools for character relationship analysis
├── crawler/              # Web scraping scripts
├── data/                 # Dataset storage
├── theme_classifier/     # Scripts for theme classification
├── README.md             # Project documentation
└── jutsu.jsonl           # Extracted Jutsu data in JSONL format
```

---

## How It Works

### 1. Web Scraping
Using **Scrapy** and **BeautifulSoup**, the project scrapes jutsu data, cleans up irrelevant content, and structures it for further analysis. Key points:
- Jutsu name, type, and descriptions are extracted.
- Trivia and videos are removed to ensure clean data.

```python
class BlogSpider(scrapy.Spider):
    name = 'narutospider'
    start_urls = ['https://naruto.fandom.com/wiki/Special:BrowseData/Jutsu?limit=250&offset=0&_cat=Jutsu']

    def parse(self, response):
        # Extract and follow links to jutsu pages
        ...

    def parse_jutsu(self, response):
        # Extract jutsu name, type, and description
        ...
```

### 2. Theme Classification
The `facebook/bart-large-mnli` model is used to classify themes within scripts using a zero-shot classification pipeline.
- Themes such as `friendship`, `betrayal`, `love`, etc., are scored based on their relevance to each script.
- Implements sentence tokenization and batch processing for efficiency.

```python
from transformers import pipeline

def get_themes(script):
    # Tokenize and batch script sentences
    ...

    # Apply theme classification
    emotion_output = theme_classifier(script_batches, candidate_labels, multi_label=True)
    ...
    return emotions
```

### 3. Visualization
The project summarizes and visualizes theme scores using bar plots. For example:
```python
sns.barplot(data=theme_output, x="theme", y="score")
plt.xticks(rotation=45)
plt.show()
```
![Theme Distribution Visualization](theme_distribution.png)

---

## Setup and Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/naruto-data-science.git
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up the Scrapy environment:
   ```bash
   scrapy startproject crawler
   ```

4. Install the required Python packages:
   ```bash
   pip install transformers numpy pandas matplotlib seaborn beautifulsoup4
   ```

5. Run the web scraper:
   ```bash
   scrapy crawl narutospider
   ```

6. Perform theme classification:
   ```python
   python theme_classifier/classify_themes.py
   ```

---

## Results
- **Theme Analysis:**
  Example themes extracted from scripts:
  | Theme          | Score       |
  |----------------|-------------|
  | Betrayal       | 118.84      |
  | Battle         | 153.25      |
  | Sacrifice      | 156.42      |
  | Friendship     | 71.73       |

- **Web Scraping:**
  Cleaned and structured data of jutsus available in `jutsu.jsonl`.

---

## Future Enhancements
- Expand theme categories for a more comprehensive analysis.
- Implement network analysis for character relationships.
- Integrate deep learning models for improved accuracy in classification.

---

## Contributors
- **Gabriel Batavia**  
  Developer and maintainer of the project.

---

## License
This project is licensed under the [MIT License](LICENSE).

---

## Acknowledgments
- [Transformers Library by Hugging Face](https://huggingface.co/transformers/)
- [Naruto Fandom Wiki](https://naruto.fandom.com/)

