# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3

class VarredorDeSitesPipeline:
    def open_spider(self, spider):
        self.connection = sqlite3.connect('proxies.db')   # aqui é a conexão com o banco de dados. Dentro, é o nome escolhido do banco.
        self.cursor = self.connection.cursor() # aqui é o local de pesquisa no banco de dados.
        
        # Criar a tabela.
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS proxies(
                IP_Adress TEXT NOT NULL PRIMARY KEY,
                Port NUMBER,
                Code TEXT,
                Country TEXT,
                Anonymity TEXT,
                Google TEXT,
                Https TEXT,
                Last_Checked TEXT  
                
            )                
        ''')
        self.connection.commit()
    def close_spider(self, spider):
        self.connection.close()
        
    def process_item(self, item, spider):
        self.cursor.execute('''
            INSERT OR IGNORE INTO proxies(IP_Adress, Port, Code, Country, Anonymity, Google, Https, Last_Checked) VALUES(?,?,?,?,?,?,?,?)               
        ''',(
            item.get('IP_Adress'),
            item.get('Port'),
            item.get('Code'),
            item.get('Country'),
            item.get('Anonymity'),
            item.get('Google'),
            item.get('Https'),
            item.get('Last_Checked')  # aqui é para que haja segurança na hora da consulta. Assim utilizamos o método get
        ))
        
        self.connection.commit()  # Este comando serve para salvar as config acima no banco de dados.
        return item
        
