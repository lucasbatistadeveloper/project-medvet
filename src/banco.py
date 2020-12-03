import sqlite3

class database():
    def bdConnect(self):
        self.conn= sqlite3.connect("database.bd")
        self.cursor=self.conn.cursor()
        print("Conectando ao banco de dados")
        
    def bdDisconnect(self):
        self.conn.close()
        print("Desconectando do banco de dados")
        
    def montaTabelaCliente(self):
        self.bdConnect()
        self.cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS clientes(
            nome_cliente CHAR(40) NOT NULL,
            password_cliente CHAR(20) NOT NULL,
            telefone CHAR(20)
        );    """)
        self.conn.commit(); print("Banco de dados criado")
        self.bdDisconnect()
        
    def montaTabelaAnimal(self):
        self.bdConnect()
        self.cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS clientes(
            nome_animal CHAR(40) NOT NULL,
            especie CHAR(20) NOT NULL,
            idade INTEGER(20),
            proprietario CHAR(20)
            );    """)
        self.conn.commit(); print("Banco de dados criado")
        self.bdDisconnect()
        