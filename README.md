video : https://youtu.be/Gvu8omlebcA

## Script de Gerenciamento de Conexões de Rede
Este script em Python permite visualizar e interromper conexões de rede estabelecidas por programas em execução no Windows. Ele utiliza a biblioteca psutil para obter informações sobre as conexões de rede e os processos associados.

## Requisitos
Este é um arquivo de requisitos (requirements.txt) que lista as bibliotecas necessárias para executar o script. Certifique-se de ter essas bibliotecas instaladas em seu ambiente Python antes de executar o script.
* psutil
* os
* time
* webbrowser

## Instalação
Certifique-se de estar no diretório que contém o arquivo requirements.txt ao executar o comando acima.
````
pip install -r requirements.txt
````
## Uso
Baixe o código-fonte do script e salve-o em seu sistema.

Certifique-se de que os arquivos programas_perigosos.txt e portas_perigosas.txt estejam presentes no mesmo diretório do script. Esses arquivos contêm a lista de programas e portas considerados perigosos. Você pode adicionar ou remover entradas nesses arquivos conforme necessário.

Execute o script no prompt de comando do Windows com privilégios de administrador:
````
python port defensor.py
````
O script exibirá uma lista de programas com conexões de rede estabelecidas. Cada conexão será numerada e exibirá as seguintes informações:
* Programa: nome do programa associado à conexão.
* Caminho: caminho completo para o executável do programa.
* Endereço local: endereço IP e porta local da conexão.
* Endereço remoto: endereço IP e porta remota da conexão.
* Se um programa na lista for considerado perigoso de acordo com o arquivo programas_perigosos.txt, ele será marcado como tal.

Digite o número da conexão que deseja interromper e pressione Enter. Se preferir sair sem interromper nenhuma conexão, digite 0.

Se a conexão for interrompida com sucesso, o script exibirá a mensagem "Programa encerrado com sucesso.". Caso contrário, exibirá a mensagem "Não foi possível encerrar o programa.".

O script será executado novamente, exibindo uma nova lista de conexões, até que você escolha sair digitando 0.
## Observações
Este script foi desenvolvido e testado no Windows. Ele requer privilégios de administrador para permitir o encerramento de programas.
O script fornece uma ajuda para interromper conexões de programas perigosos, incluindo trojans. No entanto, é importante lembrar que a remoção de trojans requer uma abordagem abrangente de segurança e pode exigir o uso de um software antivírus confiável.
Este script não desativa programas na inicialização do sistema. Ele apenas permite interromper conexões de rede estabelecidas por programas em execução.
