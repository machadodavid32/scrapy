import scrapy

class ProxyScraperSpider(scrapy.Spider):
    # identidade
    name = 'proxyscraper'
    # Request
    def start_requests(self):
        urls = ['https://www.us-proxy.org/']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    # Response
    def parse(self, response):
        for linha in response.xpath("//table[@class='table table-striped table-bordered']//tr"):
            # O xpath acima engloba toda a tabela.
            # Abaixo vamos iterar com cada coluna.
            yield {
                'IP Adress': linha.xpath('./td[1]/text()').get(), # este xpath é a continuação do xpath acima, pra pegar a coluna.
                'Port': linha.xpath('./td[2]/text()').get(),
                'Code': linha.xpath('./td[3]/text()').get(),
                'Country': linha.xpath('./td[4]/text()').get(),
                'Anonymity': linha.xpath('./td[5]/text()').get(),
                'Google': linha.xpath('./td[6]/text()').get(),
                'Https': linha.xpath('./td[7]/text()').get(),
                'Last Checked': linha.xpath('./td[8]/text()').get()
                } 
            
            
        