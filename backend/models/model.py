from sqlalchemy import create_engine, Column, String, Integer, Boolean, Float, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy_utils.types import ChoiceType

#conexao com db
db = create_engine("sqlite///banco.db")

#criacao da base para db
Base = declarative_base()

#criando as classes/tabelas da db
class Usuario(Base):
    __tablename__ = "usuarios"
    
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String, nullable=False)
    email = Column("email", String, nullable=False)
    senha = Column("senha", String)
    ativo = Column("ativo", Boolean)
    admin = Column("admin", Boolean, default=False)
    
    def __init__(self, nome, email, senha, ativo, admin=False):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo
        self.admin = admin
        
class Pedido(Base):
    __tablename__ = "pedidos"
    
    STATUS = (
        ("PENDENTE", "PENDENTE"),
        ("CANCELADO", "CANCELADO")
        ("FINALIZADO", "FINALIZADO")
    )
        
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    status = Column("status", ChoiceType(choices=STATUS))
    usuario = Column("usuario", ForeignKey("usuarios.id"))
    preco = Column("preco", Float)
    #itens = Column("itens", String)
    
    def __init__(self, usuario, status="PENDENTE", preco=0):
        self.usuario = usuario
        self.preco = preco
        self.status = status
    
class ItemPedido(Base):
    __tablename__ = "itens_pedido"
    
    TAMANHO = (
            ("MEDIA", "MEDIA"),
            ("BROTINHO", "BROTINHO")
            ("GRANDE", "GRANDE")
            ("MARACANA", "MARACANA")
        )
    
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    quantidade = Column("quantidade", Integer, nullable=False)
    sabor = Column("sabor", String)
    borda_recheada = Column("borda_recheada", Boolean)
    tamanho = Column("tamanho", ChoiceType(choices=TAMANHO))
    preco_unitario = Column("preco_unitario", Float)
    pedido = Column("pedido", ForeignKey("pedidos.id"))
    
    def __init__(self, quantidade, sabor, tamanho, preco_unitario, pedido):
            self.quantidade = quantidade
            self.sabor = sabor
            self.tamanho = tamanho
            self.preco_unitario = preco_unitario
            self.pedido = pedido
    
#executa a criacao dos metadados do seu banco (criando efetivamente a db)