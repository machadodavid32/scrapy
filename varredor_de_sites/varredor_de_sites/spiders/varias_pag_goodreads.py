import scrapy

class GoodReadsSpider(scrapy.Spider):
    #Identidade
    name = 'variaspag_goodreads'
    #Request
    def start_requests(self):
       urls = ['https://www.goodreads.com/quotes?page=1']
       
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
        numero_proxima_pagina = response.xpath("//a[@class='next_page']/@href").get().split('=')[1]
        print('#' * 20)  # para ficar melhor organizado no painel do terminal.
        print(numero_proxima_pagina)
        print('#' * 20)
        if numero_proxima_pagina is not None:
            link_proxima_pagina = f'https://www.goodreads.com/quotes?page={numero_proxima_pagina}'
            print('#' * 20)
            print(link_proxima_pagina)
            print('#' * 20)
            yield scrapy.Request(url=link_proxima_pagina, callback=self.parse)
            
            

            
            
            
            
            
            

# Para rodar, abra o terminal aqui em baixo, vá até a pasta do projeto e digite:
# scrapy crawl nomedobot
# Aqui seria a pasta "varredor_de_sites" e scrapy crawl frasebot            

#PARA SALVAR NO CSV PELO terminal
#scrapy crawl nomedobot -O nomedoarquivo.csv

# Vá no scrapy shell e digite o comando: response.xpath("//a[@class='next_page']/@href").get().split('=')[1]
# Como precisamos apenas do numero da pagina seguinte, pegamos esse codigo acima com o xpath e criamos uma...
# ....variavel com response.xpath e colocomos o codigo nela, conforme acima linha 22