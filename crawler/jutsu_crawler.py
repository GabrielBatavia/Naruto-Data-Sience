import scrapy
from bs4 import BeautifulSoup


class BlogSpider(scrapy.Spider):
    name = 'narutospider'
    start_urls = ['https://naruto.fandom.com/wiki/Special:BrowseData/Jutsu?limit=250&offset=0&_cat=Jutsu']

    def parse(self, response):
        for href in response.css('div.smw-columnlist-container')[0].css('a::attr(href)').extract():
            extracted_data = scrapy.Request("https://naruto.fandom.com" + href, callback=self.parse_jutsu)
            yield extracted_data

        for next_page in response.css('a.mw-numlink'):
            yield response.follow(next_page, self.parse)

    def parse_jutsu(self, response):
        jutsu_name = response.xpath('//*[@id="firstHeading"]/span/text()').get()

        # Menggunakan XPath untuk id "content"
        div_selector = response.xpath('//*[@id="content"]').get()

        # Cek apakah div_selector ditemukan
        if div_selector is None:
            self.logger.warning(f"Div selector not found for URL: {response.url}")
            return  # Hentikan jika tidak ditemukan

        # Memproses div_selector dengan BeautifulSoup
        soup = BeautifulSoup(div_selector, 'html.parser')

        # Menghapus elemen h2 dengan id "Trivia"
        trivia_section = soup.find('h2', {'id': 'Trivia'})
        if trivia_section:
            trivia_section.decompose()

        # Menghapus elemen video jika ada
        for video in soup.find_all('video'):
            video.decompose()

        # Mengambil jenis jutsu dari elemen 'aside'
        jutsu_type = ""
        if soup.find('aside'):
            aside = soup.find('aside')
            for cell in aside.find_all('div', {'class': 'pi-data'}):
                if cell.find('h3'):
                    cell_name = cell.find('h3').text.strip()
                    if cell_name == 'Classification':
                        jutsu_type = cell.find('div').text.strip()

            # Menghapus elemen 'aside' setelah mendapatkan informasi yang diperlukan
            aside.decompose()

        # Mendapatkan deskripsi jutsu, dengan menghapus teks setelah 'Trivia' jika ada
        jutsu_description = soup.get_text()
        jutsu_description = jutsu_description.split('Trivia')[0].strip()

        if jutsu_name:
            jutsu_name = jutsu_name.strip()
            yield {
                "jutsu_name": jutsu_name,
                "jutsu_type": jutsu_type,
                "jutsu_description": jutsu_description,
            }
