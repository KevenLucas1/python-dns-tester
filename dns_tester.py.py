import subprocess
import platform
import time
import re

def consultar_dns_com_latencia(dominio, dns_ip, nome_provedor):
    print(f"\nConsultando via [{nome_provedor}] ({dns_ip})...")
    
    sistema = platform.system().lower()
    comando = ["nslookup", dominio, dns_ip]
    
    # Inicia a contagem do tempo
    inicio = time.time()
    
    try:
        resultado = subprocess.run(comando, capture_output=True, text=True, timeout=5)
        
        # Encerra a contagem do tempo
        fim = time.time()
        latencia_ms = (fim - inicio) * 1000  # Converte para milissegundos
        
        if resultado.returncode == 0:
            print(f"-> Latência de resposta: {latencia_ms:.2f} ms")
            print("-" * 20 + " Resposta do Servidor " + "-" * 20)
            print(resultado.stdout.strip())
        else:
            print(f"[Erro] Não foi possível resolver o domínio com {nome_provedor}.")
                
    except subprocess.TimeoutExpired:
        print(f"[Timeout] O servidor {nome_provedor} demorou muito para responder (> 5 segundos).")
    except Exception as e:
        print(f"[Erro inesperado] {e}")

def main():
    print("=" * 55)
    print("    TESTADOR DE DNS COM MEDIÇÃO DE LATÊNCIA")
    print("=" * 55)
    
    servidores_dns = {
        "Google": "8.8.8.8",
        "Cloudflare": "1.1.1.1",
        "Quad9": "9.9.9.9",
        "OpenDNS": "208.67.222.222"
    }
    
    dominio = input("Digite a URL ou domínio para testar (ex: google.com): ").strip()
    
    # Limpeza básica da URL caso o usuário digite http:// ou barras
    if dominio.startswith("http://"):
        dominio = dominio[7:]
    elif dominio.startswith("https://"):
        dominio = dominio[8:]
    dominio = dominio.split("/")[0]
    
    print(f"\nIniciando testes de resolução e latência para: {dominio}")
    print("=" * 55)
    
    for nome, ip in servidores_dns.items():
        consultar_dns_com_latencia(dominio, ip, nome)
        print("=" * 55)
        
    input("\nPressione ENTER para sair...")

if __name__ == "__main__":
    main()