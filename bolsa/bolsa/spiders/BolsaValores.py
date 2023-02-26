import scrapy


class BolsavaloresSpider(scrapy.Spider):
    name = "BolsaValores"
    start_urls = ["https://economia.uol.com.br/cotacoes/bolsas/"]

    def parse(self, response):
        for dados in response.css('tr.dadosRankings'):
            yield {
                'titulo': dados.css('td:nth-child(1) a::text').get(),
                'variacao': dados.css('td:nth-child(2) a::text').get(),
                'valor': dados.css('td:nth-child(3) a::text').get()
            }
