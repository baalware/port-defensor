import os
from pystyle import *

os.system("cls")

baalware = """
     NO!                          MNO!
    MNO!!       [BAALWARE]         MNNOO!
  MMNO!                           MNNOO!!
MNOONNOO!   MMMMMMMMMMPPPOII!   MNNO!!!!
!O! NNO! MMMMMMMMMMMMMPPPOOOII!! NO!
      ! MMMMMMMMMMMMMPPPPOOOOIII! !
       MMMMMMMMMMMMPPPPPOOOOOOII!!
       MMMMMOOOOOOPPPPPPPPOOOOMII!
       MMMMM..    OPPMMP    .,OMI!
       MMMM::   o.,OPMP,.o   ::I!!
         NNM:::.,,OOPM!P,.::::!!
        MMNNNNNOOOOPMO!!IIPPO!!O!
        MMMMMNNNNOO:!!:!!IPPPPOO!
         MMMMMNNOOMMNNIIIPPPOO!!
            MMMONNMMNNNIIIOO!
          MN MOMMMNNNIIIIIO! OO
         MNO! IiiiiiiiiiiiI OOOO
    NNN.MNO!   O!!!!!!!!!O   OONO NO!
   MNNNNNO!    OOOOOOOOOOO    MMNNON!
     MNNNNO!    PPPPPPPPP    MMNON!
        OO!                   ON!\n               
"""

diretorio_scripts = "scripts"
os.system("cls")
categorias = {
    "killport": "baalware_killport.py",
    "chkport": "baalware_chkport.py",
    "author": "baalware_author.py"
}

pilha_categorias = []


print(Colorate.Horizontal(Colors.red_to_yellow,Center.XCenter(baalware)))
while True:
    for categoria in categorias:
        print(Colorate.Horizontal(Colors.red_to_yellow,Center.XCenter(categoria)))
    print("")

    entrada = input("> ")
    if entrada == "voltar":
        if pilha_categorias:
            categoria_anterior = pilha_categorias.pop()
            print(f"Voltando para a categoria '{categoria_anterior}'\n")
        else:
            print("Não há categorias anteriores.\n")
        continue
    os.system("cls")
    print(Colorate.Horizontal(Colors.red_to_yellow,Center.XCenter(baalware)))
    if entrada in categorias:
        categoria = entrada

        pilha_categorias.append(categoria)

        script = categorias[categoria]
        caminho_script = os.path.join(diretorio_scripts, script)

        os.system(f"python {caminho_script}")
        print("")

