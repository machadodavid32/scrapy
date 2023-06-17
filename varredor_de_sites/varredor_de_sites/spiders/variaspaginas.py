import scrapy

class QuotesToReadSpider(scrapy.Spider):
    # identidade
    name = 'citacao'

    # Request
    def start_requests(self):
        urls = ['https://quotes.toscrape.com/']
    
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    # Response
    def parse(self, response):
        for quote in response.xpath('//div[@class="quote"]'):
            yield {
                'frase': quote.xpath('.//span[@class="text"]/text()').get(),
                'autor': quote.xpath('.//small[@class="author"]/text()').get(),
                'tags': quote.xpath('.//div[@class="tags"]/a/text()').getall()
            }
     
        try:
            link_proxima_pagina = response.xpath(
                "//li[@class='next']/a/@href").get()
            if link_proxima_pagina is not None:
                proxima_pagina_url_completo = response.urljoin(
                    link_proxima_pagina)
                yield scrapy.Request(
                    url=proxima_pagina_url_completo, callback=self.parse)
        except:
            print('Chegamos na última página')
           
        # Como varrer varias paginas
        #Tentar encontrar o botão 'proximo', se encontrar, varrer essas páginas.
        try:
            link_proxima_pagina = response.xpath("//li[@class='next']/a/@href") # Neste xpath, o @href vai retirar as informações que estão dentro dele. ex: page3
            if link_proxima_pagina is not None:
                link_proxima_pagina_completo = response.urljoin(link_proxima_pagina)
                yield scrapy.Request(url=link_proxima_pagina_completo, callback=self.parse)
        except:
            print("Chegamos na ultima página")
        
# Para rodar, abra o terminal aqui em baixo, vá até a pasta do projeto e digite:
# scrapy crawl nomedobot
# Aqui seria a pasta "varredor_de_sites" e scrapy crawl frasebot 

# Na linha 28, o url join vai juntar a url inicial com a informação extraida da variavel link_proxima_pagina.
# Exemplo. David.com, com o url join fica david.com/page1, depois page2 e por ai vai,