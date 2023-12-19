# Manager_de_CS

Um jogo rápido de simulação de partidas do jogo Counter Strike.

Uma das maiores franquias do mundo, o Counter Strike é um jogo cheio de ação e estratégia, milhares de jogadores buscam melhorar seu desempenho todo dia para tentar jogar profissionalmente, enquanto assistem seus ídolos jogarem nos maiores palcos do mundo. Assim como outros jogos de esportes, como o Fifa, Madden e NBA, todo fã já pensou em como seria ser um técnico do esporte favorito. Nesse intuito foi criado esse Jogo, aonde o usuário toma decisões que influenciam na vitória (ou derrota) de seu time. 

Os elencos dos times são baseados em sua maioria no tempo logo antes do lançamento do CS2 e com times representando todas as principais regiões do cenário competitivo. O usuário escolhe seu time e o time que irá jogar contra. Após isso, ira vetar os mapas (A partida é sempre MD3) e para cada mapa definirá sua tática, seus pontos fortes de defesa e ataque e como irá gerenciar sua economia. Após isso o algoritmo trabalha e entrega o resultado do jogo, aonde você pode ver quem desempenhou bem ou mal no seu time e o placar. Ao final da partida temos os dados totais e uma tabela com o histórico do usuário comandando algum time (aparecerem apenas os cinco primeiros usuarios_time diferentes, se você jogou com dois times diferentes irá aparecer na tabela duas vezes seu nome, com suas estatísticas referentes a cada time controlado)


# Instruções de instalação

É necessário ter:

Python 3.10 ou acima 

Rich 13.7 ou acima

matplotlib 3.8.2 ou acima

numpy 1.26.2 ou acima

mysql.connector 2.2.9 ou acima


Demais módulos já vem instalados com o Python 3.10 ou acima

É necessário baixar o aplicativo MySQL Workbench 8.0 e criar uma conxeão localhost com nome de usuário = "root" e executar o script cspython4.sql dentro dessa conexão no workbench.
É aconselhável usar o aplicativo Xampp para estabelecer a conexão local, um vídeo explicando como: https://www.youtube.com/watch?v=f_EGF3027qs

Possivelmente é necessário deixar a pasta e todos os arquivos no grupo de Sistema para poder mexer com arquivos

Execute o arquivo manager_de_cs.py

# Feedback/Reports

Reporte qualquer problema que estiver tendo com esse programa em https://github.com/raphaelpercycefet/CS-Manager-Simulator/issues.
