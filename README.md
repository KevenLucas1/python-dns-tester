# 🌐 Python DNS Tester com Latência

Utilitário avançado de diagnóstico de rede desenvolvido em Python para testar a resolução de URLs/domínios em diferentes servidores DNS globais, calculando o tempo exato de resposta (latência) de cada provedor.

## 🚀 Tecnologias e Funcionalidades
* **Linguagem:** Python 3
* **Módulos Nativos:** `subprocess` (execução de comandos do sistema operacional), `platform` (compatibilidade multiplataforma) e `time` (medição de performance).
* **Principais Recursos:**
  * Tratamento e limpeza automática de URLs informadas pelo usuário.
  * Teste simultâneo nos principais servidores DNS do mundo (`Google`, `Cloudflare`, `Quad9` e `OpenDNS`).
  * Medição precisa de **latência em milissegundos (ms)** para avaliar qual DNS responde mais rápido na sua rota atual.
  * Exibição detalhada do registro de endereçamento retornado.

## ⚙️ Como executar
1. Certifique-se de ter o Python instalado.
2. Baixe o arquivo `dns_tester.py`.
3. Execute no seu terminal:
   ```bash
   python dns_tester.py
4. Digite o domínio desejado (ex: github.com) e analise o desempenho e a resposta de cada DNS.
