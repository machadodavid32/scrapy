import scrapy

class GoodReadsSpider(scrapy.Spider):
    #Identidade
    name = 'frasebot'
    #Request
    def start_requests(self):
       urls = ['https://www.goodreads.com/quotes']
       
       for url in urls:
           yield scrapy.Request(url=url, callback=self.parse)
           
    #Response
    def parse(self, response):
        # Aqui é onde você deve processar o que é retornado da response
        for elemento in response.xpath("//div[@class='quoteDetails']"):
            yield{
                'frase': elemento.xpath(".//div[@class='quoteText']/text()").get(),
                'autor': elemento.xpath(".//span[@class='authorOrTitle']/text()").get(),
                'tag': elemento.xpath(".//div[@class='greyText smallText left']/text()").getall()
            }

# Para rodar, abra o terminal aqui em baixo, vá até a pasta do projeto e digite:
# scrapy crawl nomedobot
# Aqui seria a pasta "varredor_de_sites" e scrapy crawl frasebot            

#PARA SALVAR NO CSV PELO terminal
#scrapy crawl nomedobot -O nomedoarquivo.csv
