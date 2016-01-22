# vagalume-download-lyrics

 A crawler that downloads all the lyrics of an artist / band from [Vagalume.com.br](http://www.vagalume.com.br).

**Dependencies**:

- python-slugify (install using `pip install python-slugify`)
- scrapy (install using `pip install scrapy`)

## How to use

First of all, go to [Vagalume](http://www.vagalume.com.br), find the artist that you want to download the lyrics and copy the URL of the artist's page.

If you want to download Pink Floyd lyrics (for example) you'll find the following url: *http://www.vagalume.com.br/pink-floyd/*. Now exclude "http://www.vagalume.com.br" from the URL and the remaining string paste at the `vagalume_spide.py` source code (in the `artist_page` attribute).

```
http://www.vagalume.com.br/pink-floyd/   --->    /pink-floyd/
```

Now you're ready to crawl the lyrics. In order to do that, run `scrapy runspider vagalume_spider.py` from your Terminal and wait the process finish. After that, the lyrics from the choosen artist should be available at `lyrics` folder. 

If you want to delete all the lyrics, just run `./delete_lyrics.sh` from your Terminal.

## About

This very small crawler was created by Fernando Paladini as a part of another Github project. 




	