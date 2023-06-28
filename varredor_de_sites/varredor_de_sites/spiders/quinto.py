import scrapy

class QuintoScraperSpider(scrapy.Spider):
    # identidade
    name = 'quintoscraper'
    # Request
    def start_requests(self):
        urls = ['https://www.quintoandar.com.br/comprar/imovel/santa-ifigenia-sao-paulo-sp-ra/de-150000-a-600000-venda']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    # Response
    def parse(self, response):
        for linha in response.xpath("//div[@class='sc-7fnxs3-0 IUFUB']"):
        #for linha in response.xpath("//div[@data-testid='house-card-details']"):    
            # O xpath acima engloba toda a tabela.
            # Abaixo vamos iterar com cada coluna.
            yield {
                'Titulo': linha.xpath("//span[@data-testid='house-card-type']/text()").get(),
                #'Titulo': linha.xpath(".//span[@data-testid='house-card-type']/text()").get(), # este xpath é a continuação do xpath acima, pra pegar a coluna.
                'Rua': linha.xpath(".//span[@data-testid='house-card-address']/text()").get(),
                'Regiao': linha.xpath(".//span[@data-testid='house-card-region']/text()").get(),
                'Area': linha.xpath(".//small[@data-testid='house-card-area']/text()[1]").get(),
                'Preco': linha.xpath(".//div[@class='sc-1n9m1a2-1 eYbkMu']//small[@class='sc-ftvSup eBJKGf sc-papXJ gPyLfp CozyTypography']/text()").get()
                } 

            
        #Aqui funcionou para preço, porém, terá que
        # fazer outro for para o começo destrs xpath
        # //div[@class='sc-1n9m1a2-1 eYbkMu']//small[@class='sc-ftvSup eBJKGf sc-papXJ gPyLfp CozyTypography']/text()
        # //div[@class='sc-1n9m1a2-1 eYbkMu']//small[@data-testid='house-card-area']/text()").get()
        
        # //div[@class='sc-1y4z098-0 geAIvx']//span[@data-testid='house-card-type']/text()
        
        