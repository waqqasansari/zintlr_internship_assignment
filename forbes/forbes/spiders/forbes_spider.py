import scrapy

class ForbesSpider(scrapy.Spider): 
    name = 'forbes'
    start_urls = {
        'https://www.forbes.com/lists/global2000/?sh=487cb9305ac0'
    }

    def parse(self, response):

        #//*[@id="table"]/div[1]/div[@class="table"] all tables not including the advertisement.
        #//*[@id="table"]/div[1]/div[@class="table"]/div/a/div[@class="rank first table-cell    rank"] rank
        # all_list = response.xpath('//*[@id="table"]/div/div/div/a')
        #(?:[\£\$\€]{1}[,\d]+.?\d*) regex for cunrrency

        rank = response.xpath('//*[@id="table"]/div/div/div/a/div[@class="rank first table-cell    rank"]/text()').extract()
        name = response.xpath('//*[@id="table"]/div/div/div/a/div[@class="organizationName second table-cell    name"]/text()').extract()
        country = response.xpath('//*[@id="table"]/div/div/div/a/div[@class="country  table-cell    country"]/text()').extract()
        sales = response.xpath('//*[@id="table"]/div/div/div/a/div[@class="revenue  table-cell    sales "]/text()').extract()
        profit = response.xpath('//*[@id="table"]/div/div/div/a/div[@class="profits  table-cell    profit "]/text()').extract()
        assets = response.xpath('//*[@id="table"]/div/div/div/a/div[@class="assets  table-cell    assets "]/text()').extract()
        market_value = response.xpath('//*[@id="table"]/div/div/div/a/div[@class="marketValue  table-cell    market value "]/text()').extract()
        link = response.xpath('//*[@id="table"]/div/div/div/a').re('href=[\'"]?([^\'" >]+)')

        # rank = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "rank", " " ))]/text()').extract()
        # name = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "name", " " ))]/text()').extract()
        # country = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "country", " " ))]/text()').extract()
        # sales = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "sales", " " ))]/text()').extract()
        # profit = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "profit", " " ))]/text()').extract()
        # assets = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "assets", " " ))]/text()').extract()
        # market_value = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "value", " " ))]/text()').extract()
        # link = response.xpath('//*[@id="table"]/div/div/div/a').re('href=[\'"]?([^\'" >]+)')
        # link = response.xpath('//*[@id="table"]/div/div/div/a').extract()
        #units = response.xpath('string(//body)').re("(Units: [\d]+)")
        
        
        yield {
            'Rank': rank,
            'Name': name,
            'Country': country,
            'Sales': sales,
            'Profit': profit,
            'Assets': assets,
            'Market_Value': market_value,
            'link': link
        }
