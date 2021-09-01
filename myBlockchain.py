from hashlib import sha256	#sha256 para criptografar blocos (string com 64 caracteres)
import json
from datetime import datetime   #datetime p/ ter a data de criação (timestamp) dos blocos

#Criar a estrutura de dados para a Blockchain (inicialmente vazia)
block_chain = []	#blockchain será uma lista de hashes, cada um com 64 caracteres. 

#função para gerar o Timestamp (e assim ver a hora que transação foi efetivada)
def get_time():
	return datetime.utcnow().timestamp()   #timestamp da data atual
	
#DIFFICULTY: forma de validar o hash.
#	No nosso caso, um hash será válido se começar com quatro “0” (por exemplo, “0000abc…”)
#	Quanto maior essa dificuldade, mais tempo vai levar para encontrar um hash válido.
def isValidHashDifficulty(hash, difficulty):
	count = 0
	for i in hash:
		count += 1
		if(i != '0'):
			break
	return count > difficulty

#função para gerar o Hash
def generate_hash(block):
	#NONCE: simples número inteiro que vamos incrementar sempre que um hash não for válido.
	#em resumo, o Nonce é um iterador: contador p/ fazer iterações até achar um HASH válido
	nonce = 0
	block["nonce"] = nonce
	hash = sha256(json.dumps(block).encode('utf-8')).hexdigest()
	while(not isValidHashDifficulty(hash, 4)):
		nonce = nonce + 1
		block["nonce"] = nonce
		hash = sha256(json.dumps(block).encode('utf-8')).hexdigest()
	return hash

#função p/ adicionar blocos na Blockchain
def add_block(block):
	if(len(block_chain) == 0):	#se block_chain estiver vazia (1º bloco a ser adicionado)
		block["timestamp"] = get_time()
		block["hash"] = generate_hash(block)
	else:
		block["timestamp"] = get_time()
		last_block = block_chain[-1]
		#validação dos blocos anteriores
    	#validação de ORIGEM e DESTINO
		while block["origem"] != last_block["destino"]:
			origem = input("Origem errada! Por favor, digite novamente: ")
			if origem == last_block["destino"]:
				block['origem'] = origem

		#validação de Código do Produto
		while block["codigo"] != last_block["codigo"]:
			codigo = input("Código do Produto errado! Digitar novamente: ")
			if codigo == last_block["codigo"]:
				block['codigo'] = codigo

		block["previous_Hash"] = last_block["hash"]
		block["hash"] = generate_hash(block)	
	
	#Após todas as validações serem feitas, adicionar bloco na Blockchain
	block_chain.append(block)	


#Esperando um Evento
# Evento --> informação de adicionar ou não o bloco na Blockchain
while 1:
	print("\n########################################")
	resp = input("Deseja adicionar alguma informação?(S/N) ")
	if resp == 's' or resp == 'S':
		data = {}	#bloco contendo informação
		
		origem = input("Origem do Produto: ")
		destino = input("Destino do Produto: ")
		codigo = input("Codigo do Produto: ")
		empresa = input("Empresa responsável: ")

		data['origem'] = origem
		data['destino'] = destino
		data['codigo'] = codigo
		data['empresa'] = empresa

		json_data = json.dumps(data)
		add_block(data)
		print("=== Cadastro realizado com sucesso! ===")

	else:
		break



###################################
print('\n###################################')
print("Blockchain criada: ")
print(block_chain)

print("Nº de Blocos na Blockchain: ", len(block_chain))
