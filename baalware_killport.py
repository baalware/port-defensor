import psutil
import os
from pystyle import *


os.system("cls")
def get_programs_with_network_connections():
    programs = []
    connections = psutil.net_connections()

    for conn in connections:
        if conn.status == 'ESTABLISHED':
            pid = conn.pid
            program = psutil.Process(pid).name()
            program_path = psutil.Process(pid).exe()
            local_address = f"{conn.laddr.ip}:{conn.laddr.port}"
            remote_address = f"{conn.raddr.ip}:{conn.raddr.port}"
            programs.append((program, program_path, local_address, remote_address, pid))

    return programs

def is_program_dangerous(program):
    dangerous_programs = []

    with open("programas_perigosos.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            if line.startswith("#") or not line:
                continue
            dangerous_programs.append(line.lower())

    program_name = os.path.splitext(program)[0].lower()
    return any(program_name == dangerous_program for dangerous_program in dangerous_programs)

def is_port_dangerous(port):
    dangerous_ports = []

    with open("portas_perigosas.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            if line.startswith("#") or not line:
                continue
            dangerous_ports.append(int(line))

    return port in dangerous_ports

def disconnect_connection(program):
    try:
        os.system(f"taskkill /IM {program} /F")
        print("Programa encerrado com sucesso.")
    except OSError:
        print("Não foi possível encerrar o programa.")

connected_programs = get_programs_with_network_connections()

if connected_programs:
    for index, (program, program_path, local_address, remote_address, pid) in enumerate(connected_programs):
        print(f"Conexão {index + 1}:")
        print("Programa:", program)
        print("Caminho:", program_path)
        print("Endereço local:", local_address)
        print("Endereço remoto:", remote_address)
        print()

    choice = input("Digite o número da conexão que deseja interromper (ou '0' para sair): ")
    if choice.isdigit():
        choice = int(choice)
        if 0 < choice <= len(connected_programs):
            program_name = connected_programs[choice - 1][0]
            disconnect_connection(program_name)
        elif choice == 0:
            print("Programa de interrupção selecionado: Sair")
        else:
            print("Opção inválida.")
    else:
        print("Opção inválida.")

else:
    print("Nenhum programa com conexões de rede encontrada.")
os.system("cls")
