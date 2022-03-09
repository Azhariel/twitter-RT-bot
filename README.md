<h1 align=center>Like & RT Bot</h1>
<h4 align=center>
Funcionalidade para aumentar o alcance de membros de um determinado grupo no Twitter.
</h4>

# Introdução
O objetivo desse projeto é automatizar as funções de Like & RT de um determinado perfil no Twitter, para que sempre ative essas funções quando certos tweets passarem por certos critérios. Na implementação atual, o cenário é o seguinte:

>Membros de um determinado grupo anunciam novidades, como lives ou novos projetos, em tweets. O perfil da organização que essas pessoas fazem parte precisava verificar constantemente se os membros postaram novidades e manualmente curtir os tweets e retuitar (RT). Esta implementação permite que o perfil do grupo automaticamente curta e dê RT nos tweets que mencionem (@grupo) o perfil do grupo e utilizem uma dada hashtag (#grupo).

# Documentação
O código está completamente comentado, devendo ser o suficiente para suprir quaisquer dúvidas. O programa roda o loop da função principal, utilizando Tweepy para gerenciar a conexão com a API do Twitter, guardando as credenciais do perfil utilizado em arquivo [.env](.example_env) e utilizando um [arquivo de texto](last_seen_id.txt) para guardar o último tweet visto pelo programa.

Na implementação, o programa aceita menções apenas do meu perfil no twitter ([@azhariel](https://twitter.com/azhariel)), mas é possível incluir qualquer número de perfis a se vigiar inserindo seus respectivos IDs na variável `members_id`.

# Notas Finais
Caso tenha qualquer sugestão ou queira incrementar o projeto, sinta-se à vontade para contribuir!
Para entrar em contato comigo, todas minhas redes estão disponíveis no [Linktr.ee](https://linktr.ee/azhariel)
