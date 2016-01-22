import scrapy
from slugify import slugify

# Don't change this attribute.
base_uri = "http://www.vagalume.com.br"

# Go to http://www.vagalume.com.br and find the URL of the desired artist.
# http://www.vagalume.com.br/pink-floyd/   --->    /pink-floyd/
artist_page = "/pink-floyd/"

class VagalumeSpider(scrapy.Spider):
    name = 'vagalume-download-lyrics'
    start_urls = [base_uri + artist_page]

    def parse(self, response):
        for url in response.xpath("//*[@class='tracks']/li/a[not(@class='t')]/@href"):
            new_url = base_uri + url.extract()
            yield scrapy.Request(response.urljoin(new_url), self.parse_lyrics)

    def parse_lyrics(self, response):
        music_title = response.xpath("//*[@id='header']/h1/text()").extract()
        lyric = response.xpath("//*[@id='lyr_original']/div/text()").extract()

        better_music_title = ''.join(music_title)
        better_lyric = '\n'.join(lyric).replace("Instrumental", "")
        
        with open(''.join(["lyrics/", slugify(better_music_title), '.lyric']), "w") as text_file:
            text_file.write(better_lyric)