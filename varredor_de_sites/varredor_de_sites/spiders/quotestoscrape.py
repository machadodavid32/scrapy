import scrapy

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
        with open('pagina.html', 'wb') as arquivo:
            arquivo.write(response.body)
            
# Este pequeno projeto é para clonar uma página html.
# Para rodar, abra o terminal aqui em baixo, vá até a pasta do projeto e digite:
# scrapy crawl nomedobot
# Aqui seria a pasta "varredor_de_sites" e scrapy crawl frasebot            