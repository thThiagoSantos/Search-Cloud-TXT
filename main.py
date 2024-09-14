import os
import re
from colorama import init, Fore, Style

# Inicializar colorama
init(autoreset=True)

# Diretório de entrada e saída
input_dir = './input'
output_file = './output/result.txt'

# Banner ASCII
banner = rf"""
{Fore.GREEN}{Style.BRIGHT}
  _____                     _     _____  _  __
 / ____|                   | |   |  __ \| |/ /
| (___   ___  __ _ _ __ ___| |__ | |__) | ' / 
 \___ \ / _ \/ _` | '__/ __| '_ \|  ___/|  <  
 ____) |  __/ (_| | | | (__| | | | |    | . \ 
|_____/ \___|\__,_|_|  \___|_| |_|_|    |_|\_\\
"""

print(banner)

# Solicitar ao usuário a URL ou parte dela que deseja procurar
user_url = input(f"{Fore.CYAN}Digite a URL ou parte dela que deseja procurar: ")

# Expressão regular para encontrar URLs que contenham a entrada do usuário
url_regex = re.compile(rf'((https?:\/\/)?[^\s]*{re.escape(user_url)}[^\s]*)')

# Função para verificar se uma linha contém uma URL
def contains_url(line):
    return url_regex.search(line) is not None

# Função para processar um arquivo
def process_file(file_path, output_stream):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                if contains_url(line):
                    output_stream.write(line.strip() + '\n')
                    print(f"{Fore.YELLOW}{line.strip()}")
    except UnicodeDecodeError:
        with open(file_path, 'r', encoding='latin-1') as file:
            for line in file:
                if contains_url(line):
                    output_stream.write(line.strip() + '\n')
                    print(f"{Fore.YELLOW}{line.strip()}")

# Função principal para processar todos os arquivos .txt na pasta
def process_files():
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, 'w', encoding='utf-8') as output_stream:
        for root, _, files in os.walk(input_dir):
            for file in files:
                if file.endswith('.txt'):
                    file_path = os.path.join(root, file)
                    process_file(file_path, output_stream)
    print(f"{Fore.GREEN}Resultados escritos em {output_file}")
    print(f"{Fore.GREEN}Extração de URLs finalizada!")

# Executar a função principal
if __name__ == '__main__':
    process_files()