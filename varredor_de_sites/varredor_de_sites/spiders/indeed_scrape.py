import scrapy

class IndeedSpider(scrapy.Spider):
    # identidade
    name = 'indeedscraper'
    # Request
    def start_requests(self):
        urls = [
            'https://br.indeed.com/jobs?q=python+junior&l=Estado+de+S%C3%A3o+Paulo&from=searchOnHP&vjk=75e3442879fab6ed']
        #urls = ["https://br.indeed.com/jobs?q=dev+python&l=Estado+de+S%C3%A3o+Paulo&vjk=f9fca5e232f9fe41"]
        
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    # Response
    def parse(self, response):
        for vaga in response.xpath("//td[@class='resultContent']"):
            # O xpath acima engloba toda a tabela.
            # Abaixo vamos iterar com cada coluna.
            yield {
                'Vaga': vaga.xpath(".//span[1]/text()").get(), # este xpath é a continuação do xpath acima, pra pegar a coluna.
                'Empresa': vaga.xpath(".//span[@class='companyName']/text()").get(),
                 #'Local': vaga.xpath(".//div[@class='companyLocation']/text()").get(),
                'Local': vaga.xpath(".//div[@class='companyLocation']/span/text()").get(),
                'Link': vaga.xpath(".//a/@href").get()
                
                } 
            
            
        