import scrapy

class ProxyFreeSpider(scrapy.Spider):
    # Identidade
    name = 'freeproxyscraper'
    # Request
    def start_requests(self):
        urls = ['https://free-proxy-list.net/web-proxy.html']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        for linha in response.xpath("//table[@class='table table-striped table-bordered']//tr"):
            yield{
                'Proxy Name': linha.xpath('./td[1]/a/text()').get(),
                'Domain': linha.xpath('./td[2]/text()').get(),
                'Country': linha.xpath('./td[3]/text()').get(),
                'Speed': linha.xpath('./td[4]/text()').get(),
                'Popularity': linha.xpath('./td[5]/div/div/text()').get()
            }
            
            
            
            
            
            
            
            