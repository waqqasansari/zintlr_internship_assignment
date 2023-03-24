import scrapy

class Forbes20Spider(scrapy.Spider):
    name = 'forbes20'

    def start_requests(self):

        urls = [
            'https://www.forbes.com/companies/berkshire-hathaway/?list=global2000',
            'https://www.forbes.com/companies/icbc/?list=global2000',
            'https://www.forbes.com/companies/saudi-arabian-oil-company-saudi-aramco/?list=global2000',
            'https://www.forbes.com/companies/jpmorgan-chase/?list=global2000',
            'https://www.forbes.com/companies/china-construction-bank/?list=global2000',
            'https://www.forbes.com/companies/amazon/?list=global2000',
            'https://www.forbes.com/companies/apple/?list=global2000',
            'https://www.forbes.com/companies/agricultural-bank-of-china/?list=global2000',
            'https://www.forbes.com/companies/bank-of-america/?list=global2000',
            'https://www.forbes.com/companies/toyota-motor/?list=global2000',
            'https://www.forbes.com/companies/alphabet/?list=global2000',
            'https://www.forbes.com/companies/microsoft/?list=global2000',
            'https://www.forbes.com/companies/bank-of-china/?list=global2000',
            'https://www.forbes.com/companies/samsung-electronics/?list=global2000',
            'https://www.forbes.com/companies/exxon-mobil/?list=global2000',
            'https://www.forbes.com/companies/shell/?list=global2000',
            'https://www.forbes.com/companies/ping-an-insurance/?list=global2000',
            'https://www.forbes.com/companies/wells-fargo/?list=global2000',
            'https://www.forbes.com/companies/verizon-communications/?list=global2000',
            'https://www.forbes.com/companies/att/?list=global2000'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        
        name = response.xpath('/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div/div[1]/h1/text()').extract_first()
        industry = response.xpath('/html/body/div[1]/div[1]/div[3]/div[1]/div[2]/div[2]/span[2]/span/text()').extract_first()
        founded = response.xpath('/html/body/div[1]/div[1]/div[3]/div[1]/div[2]/div[3]/span[2]/span/text()').extract_first()
        headquarters = response.xpath('/html/body/div[1]/div[1]/div[3]/div[1]/div[2]/div[4]/span[2]/span/text()').extract_first()
        country = response.xpath('/html/body/div[1]/div[1]/div[3]/div[1]/div[2]/div[5]/span[2]/span/text()').extract_first()
        chief_executive_officer = response.xpath('/html/body/div[1]/div[1]/div[3]/div[1]/div[2]/div[6]/span[2]/span/text()').extract_first()
        employees = response.xpath('/html/body/div[1]/div[1]/div[3]/div[1]/div[2]/div[7]/span[2]/span/text()').extract_first()

        yield {
            'Name' : name,
            'Industry' : industry,
            'Founded' : founded,
            'Headquarters' : headquarters,
            'Country' : country,
            'Chief_Executive_Officer' : chief_executive_officer,
            'Employees' : employees,
        }


