import scrapy
from scrapy.loader import ItemLoader
from varredor_de_sites.items import CitacaoItem  # aqui para fazer funcionar o arquivo items.py


class QuotesToScrapeSpider(scrapy.Spider):
    #Identidade
    name = 'frasebot'
    #Request
    def start_requests(self):
       urls = ['https://quotes.toscrape.com/']
       
       for url in urls:
           yield scrapy.Request(url=url, callback=self.parse)
           
    #Response
    def parse(self, response):
        # Aqui é onde você deve processar o que é retornado da response
        for elemento in response.xpath("//div[@class='quote']"):
            loader = ItemLoader(item=CitacaoItem(), selector=elemento, response=response)
            loader.add_xpath('frase', ".//span[@class='text']/text()")  # xpath da frase
            loader.add_xpath('autor', ".//small[@class='author']/text()") # xpath do autor
            loader.add_xpath('tag', ".//a[@class='tag']/text()") # Xpath da tag
            yield loader.load_item()
            
            """Assim o codigo abaixo deverá ser deletado. Vou deixar como
            yield{
                'frase': elemento.xpath(".//span[@class='text']/text()").get(),
                'autor': elemento.xpath(".//small[@class='author']/text()").get(),
                'tag': elemento.xpath(".//a[@class='tag']/text()").getall()
                """
            

# Para rodar, abra o terminal aqui em baixo, vá até a pasta do projeto e digite:
# scrapy crawl nomedobot
# Aqui seria a pasta "varredor_de_sites" e scrapy crawl frasebot            