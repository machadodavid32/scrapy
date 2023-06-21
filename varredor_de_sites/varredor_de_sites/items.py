# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst, Join

def tirar_espaco_em_branco(valor):
    valor.strip()  # função que remove um espaço em branco.

def processar_caracteres_especiais(valor):
    return valor.replace(u"u201c", '').replace(u"u201d", '') # Aqui estamos pegando codigos unicode que foram localizados em tal arquivo...
    # ...e substituindo por nada''

class CitacaoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    frase = scrapy.Field(
        input_processor=MapCompose(tirar_espaco_em_branco, processar_caracteres_especiais),
        output_processor=TakeFirst() # retorna sempre o primeiro resultado.
    ) # o MapCompose vai chamar as funções que estão dentro dele de forma sequencial.
    autor = scrapy.Field(
        output_processor=TakeFirst()  # não vamos mexer no campo 'autor'
    )
    tag = scrapy.Field(
        output_processor=Join(',') # unir as tags por virgulas
    )
    
    
# Após configurar este arquivo, vá na spider que você quer e importe essas funções    
    
