import psutil
import os
import time

os.system("cls")

def get_programs_with_network_connections():
    programs = []
    connections = psutil.net_connections()

    for conn in connections:
        if conn.status == 'ESTABLISHED':
            pid = conn.pid
            program = psutil.Process(pid).name()
            local_address = f"{conn.laddr.ip}:{conn.laddr.port}"
            remote_address = f"{conn.raddr.ip}:{conn.raddr.port}"
            programs.append((program, local_address, remote_address))

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

previous_connections = []  

while True:
    connected_programs = get_programs_with_network_connections()

    if connected_programs:
        new_connections = []
        for program, local_address, remote_address in connected_programs:
            new_connections.append((program, local_address, remote_address))

            if (program, local_address, remote_address) not in previous_connections:
                if is_program_dangerous(program) or is_port_dangerous(int(local_address.split(":")[1])) or is_port_dangerous(int(remote_address.split(":")[1])):
                    print("Nova conexão potencialmente perigosa detectada!")
                    print("Programa:", program)
                    print("Endereço local:", local_address)
                    print("Endereço remoto:", remote_address)

                    if is_program_dangerous(program):
                        print("ALERTA: Este programa é potencialmente perigoso!")

                    if is_port_dangerous(int(local_address.split(":")[1])):
                        print("ALERTA: A porta local é potencialmente perigosa!")

                    if is_port_dangerous(int(remote_address.split(":")[1])):
                        print("ALERTA: A porta remota é potencialmente perigosa!")

                    print("-" * 20)

        previous_connections = new_connections  
    else:
        print("Nenhum programa com conexões de rede encontrada.")

    time.sleep(1)  
