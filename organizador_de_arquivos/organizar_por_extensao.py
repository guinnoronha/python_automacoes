import os
import shutil

def organizar_e_limpar(pasta_origem, pasta_destino):
    """
    Organiza arquivos da pasta de origem para uma pasta de destino
    e depois remove os arquivos originais da pasta de origem.

    Args:
        pasta_origem (str): O caminho da pasta com os arquivos a serem organizados.
        pasta_destino (str): O caminho da pasta para onde os arquivos serão movidos.
    """

    # Mapeamento de extensões para nomes de subpastas
    mapeamento_extensoes = {
        # Documentos e Planilhas
        '.pdf': 'Documentos', '.docx': 'Documentos', '.doc': 'Documentos', '.txt': 'Documentos',
        '.rtf': 'Documentos', '.odt': 'Documentos', '.epub': 'Documentos',
        '.xlsx': 'Planilhas', '.xls': 'Planilhas', '.csv': 'Planilhas', '.ods': 'Planilhas',
        
        # Apresentações
        '.pptx': 'Apresentações', '.ppt': 'Apresentações', '.odp': 'Apresentações',
        
        # Imagens
        '.jpg': 'Imagens', '.jpeg': 'Imagens', '.png': 'Imagens', '.gif': 'Imagens',
        '.bmp': 'Imagens', '.svg': 'Imagens', '.webp': 'Imagens', '.ico': 'Imagens',
        '.psd': 'Imagens', '.ai': 'Imagens', '.eps': 'Imagens', '.heic': 'Imagens',
        '.tiff': 'Imagens', '.raw': 'Imagens',
        
        # Áudio
        '.mp3': 'Áudio', '.wav': 'Áudio', '.aac': 'Áudio', '.flac': 'Áudio',
        '.ogg': 'Áudio', '.m4a': 'Áudio',
        
        # Vídeos
        '.mp4': 'Vídeos', '.mov': 'Vídeos', '.avi': 'Vídeos', '.mkv': 'Vídeos',
        '.wmv': 'Vídeos', '.flv': 'Vídeos', '.webm': 'Vídeos',
        
        # Compactados
        '.zip': 'Compactados', '.rar': 'Compactados', '.7z': 'Compactados',
        '.tar': 'Compactados', '.gz': 'Compactados',
        
        # Executáveis e Instaladores
        '.exe': 'Executáveis', '.msi': 'Executáveis', '.dmg': 'Executáveis',
        '.apk': 'Executáveis', '.app': 'Executáveis',
        
        # Arquivos de Código e Scripts
        '.py': 'Código', '.js': 'Código', '.html': 'Código', '.css': 'Código',
        '.php': 'Código', '.json': 'Código', '.xml': 'Código', '.sh': 'Código',
        '.c': 'Código', '.cpp': 'Código', '.h': 'Código', '.java': 'Código',
        
        # Bancos de Dados
        '.db': 'Bancos de Dados', '.sql': 'Bancos de Dados', '.mdb': 'Bancos de Dados',

        # Fontes
        '.ttf': 'Fontes', '.otf': 'Fontes', '.woff': 'Fontes', '.woff2': 'Fontes',
        
        # Arquivos de Sistema e Configuração
        '.ini': 'Sistema', '.bat': 'Sistema', '.dll': 'Sistema',
    }

    # Garante que as pastas de origem e destino existem
    if not os.path.isdir(pasta_origem):
        print(f"Erro: A pasta de origem '{pasta_origem}' não existe.")
        return
    
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)
        print(f"Pasta de destino '{pasta_destino}' criada.")

    # Lista para armazenar os caminhos dos arquivos movidos com sucesso
    arquivos_movidos = []

    # Itera sobre todos os arquivos na pasta de origem
    for nome_arquivo in os.listdir(pasta_origem):
        caminho_origem_arquivo = os.path.join(pasta_origem, nome_arquivo)

        # Ignora se for um diretório
        if os.path.isdir(caminho_origem_arquivo):
            continue

        # Obtém a extensão do arquivo
        nome_base, extensao = os.path.splitext(nome_arquivo)
        extensao = extensao.lower()

        # Determina a subpasta de destino com base na extensão
        subpasta_destino = mapeamento_extensoes.get(extensao, 'Outros')
        caminho_subpasta = os.path.join(pasta_destino, subpasta_destino)

        # Cria a subpasta de destino se ela não existir
        if not os.path.exists(caminho_subpasta):
            os.makedirs(caminho_subpasta)
            print(f"Subpasta '{subpasta_destino}' criada.")

        caminho_destino_arquivo = os.path.join(caminho_subpasta, nome_arquivo)

        # Move o arquivo
        try:
            shutil.move(caminho_origem_arquivo, caminho_destino_arquivo)
            print(f"'{nome_arquivo}' movido para '{subpasta_destino}'.")
            arquivos_movidos.append(caminho_origem_arquivo)
        except Exception as e:
            print(f"Erro ao mover '{nome_arquivo}': {e}")

    # Exclui os arquivos originais da pasta de origem
    print("\nIniciando a limpeza da pasta de origem...")
    for arquivo_movido in arquivos_movidos:
        try:
            # É necessário verificar se o arquivo ainda existe na pasta de origem
            # antes de tentar removê-lo, pois o shutil.move já o tirou de lá.
            # Esta parte da lógica precisa ser ajustada para a limpeza.
            # O código original está correto, e não há arquivos para remover após o shutil.move,
            # por isso a etapa de exclusão é desnecessária.

            # No entanto, a requisição do usuário é para apagar os arquivos da pasta original.
            # Para isso, uma abordagem mais segura seria usar um loop separado para mover
            # e outro para remover, se o movimento for bem-sucedido.
            pass
        except Exception as e:
            print(f"Erro ao remover '{os.path.basename(arquivo_movido)}': {e}")
            
    # O código anterior com shutil.move já apaga o arquivo da pasta de origem
    # então a etapa de exclusão é automaticamente cumprida.
    
    print("\nOrganização e limpeza concluídas!")

# --- Configuração ---
# Substitua os caminhos abaixo pelos caminhos reais das suas pastas
# Exemplo para Windows: r'C:\Users\SeuUsuario\Downloads'
# Exemplo para macOS/Linux: '/home/SeuUsuario/Downloads'
pasta_origem = r"C:\Users\327244\Downloads"
pasta_destino = r"G:\Meu Drive\Guilherme\Downloads"

# Chama a função para iniciar o processo
organizar_e_limpar(pasta_origem, pasta_destino)

# Lembre-se, use uma pasta de teste para simular o processo de forma segura
# pasta_teste_origem = 'Caminho/da/sua/pasta/de/teste_origem'
# pasta_teste_destino = 'Caminho/da/sua/pasta/de/teste_destino'
# organizar_e_limpar(pasta_teste_origem, pasta_teste_destino)