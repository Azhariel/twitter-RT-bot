import tweepy
import time
import os
from dotenv import load_dotenv

#Documentação do Tweepy:
#https://tweepy.readthedocs.org/

#NOTE Este projeto utilizará quatro chaves necessárias para autenticação na API do Twitter
# As chaves são definidas e armazenadas no arquivo .env
load_dotenv()
CONSUMER_KEY = os.getenv('CONSUMER_KEY')
CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')
ACCESS_KEY = os.getenv('ACCESS_KEY')
ACCESS_SECRET = os.getenv('ACCESS_SECRET')

# O processo de autenticação é manejado pelo Tweepy, passando as credenciais da conta que dará o like/RT
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

# Cada usuário possui um ID único no twitter, que não é aparente mas pode ser consultado via chamada na API.
# Para achar a ID do usuário, é realizada a chamada api.get_user('usuario').id
# No caso de múltiplos usuários, pode-se utilizar uma lista. Neste exemplo, há apenas meu usuário (@azhariel)
members_id=[13830742]

# O programa pesquisará novos tweets a partir de um certo tweet, que é definido e armazenado no arquivo a seguir.
FILE_NAME = 'last_seen_id.txt'

# Funções para ler o arquivo e escrever o último tweet visto no mesmo.
def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

# Função principal
def like_and_rt():
    print('Like & RT rodando, procurando por menções!', flush=True)
    # NOTE: use 1060651988453654528 para testar.
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    
    #guarda as últimas menções (@) na variável mentions
    mentions = api.mentions_timeline(since_id=last_seen_id, tweet_mode='extended')
    #para cada tweet, em ordem reversa (mais antigos primeiro)
    for mention in reversed(mentions):
        #printa o tweet na tela com o seu ID na frente
        print('USER: ['+ str(mention.user.screen_name) +'] USER ID ['+str(mention.user.id)+'] MENTION ID ['+ str(mention.id) + ']: ' + mention.full_text, flush=True)
        #atualiza o último visto para o último ID lido (o mais recente)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        
        #verifica se o id do usuário é membro do grupo e indica o nome de usuário:
        if mention.user.id in members_id: 
            print('Menção de membro: '+ mention.user.screen_name)
            
            #se o texto da mention conter a hashtag necessária - nesse exemplo, #soberanatv, em qualquer capitalização
            if '#soberanatv' in mention.full_text.lower():
            #avisa no terminal que achou a hashtag
                print('Usando a hashtag #soberanatv', flush=True)

                #verifica se a menção já foi retuitada, pois a API retorna erro ao tentar dar RT quando já foi dado RT
                if mention.retweeted == False:
                    print('Tweet ainda não retuitado - retuitando!', flush=True)
                                      
                    #retweeta a mention
                    api.retweet(mention.id)
                
                #verifica se o tweet foi curtido, pois a API retorna erro ao tentar dar like quando já foi dado like
                if mention.favorited == False:
                    print('Tweet ainda não curtido - curtindo!', flush=True)
                    
                    #curte o tweet
                    api.create_favorite(mention.id)

# Verifica novas menções a cada 30s
while True:
    like_and_rt()
    time.sleep(30)