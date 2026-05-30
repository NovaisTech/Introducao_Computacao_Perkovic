import os
import sys
from pdf2docx import Converter
from docx2pdf import convert

def converter_arquivo(caminho_arquivo):
    # Garante que o caminho seja absoluto e limpo
    caminho_absoluto = os.path.abspath(caminho_arquivo)
    
    if not os.path.exists(caminho_absoluto):
        print(f"❌ Erro: O arquivo não foi encontrado em '{caminho_absoluto}'")
        return

    # Separa o nome do arquivo da extensão (ex: "documento" e ".pdf")
    nome_base, extensao = os.path.splitext(caminho_absoluto)
    extensao = extensao.lower()

    # --- Cenário 1: PDF para Word ---
    if extensao == '.pdf':
        novo_caminho = nome_base + ".docx"
        print(f"📄 Identificado: PDF -> Convertendo para Word...")
        try:
            cv = Converter(caminho_absoluto)
            cv.convert(novo_caminho, start=0, end=None)
            cv.close()
            print(f"✅ Sucesso! Salvo em: {novo_caminho}\n")
        except Exception as e:
            print(f"❌ Erro ao converter PDF: {e}\n")

    # --- Cenário 2: Word para PDF ---
    elif extensao in ['.docx', '.doc']:
        novo_caminho = nome_base + ".pdf"
        print(f"📝 Identificado: Word -> Convertendo para PDF...")
        try:
            # O docx2pdf abrirá o Word em segundo plano na sua máquina e salvará como PDF
            convert(caminho_absoluto, novo_caminho)
            print(f"✅ Sucesso! Salvo em: {novo_caminho}\n")
        except Exception as e:
            print(f"❌ Erro ao converter Word: {e}\n")
            print("👉 Certifique-se de que o Microsoft Word está instalado e feche o arquivo se ele estiver aberto.")

    else:
        print(f"⚠️ Formato {extensao} não suportado. Use apenas .pdf, .docx ou .doc\n")

if __name__ == "__main__":
    # Verifica se você passou arquivos por linha de comando
    if len(sys.argv) > 1:
        # Loop para permitir converter vários arquivos de uma vez só se quiser
        for arquivo in sys.argv[1:]:
            converter_arquivo(arquivo)
    else:
        # Caso você execute apenas com "python conversor.py", ele pede o caminho
        print("--- CONVERSOR DE ARQUIVOS LOCAL ---")
        caminho = input("Cole o caminho completo do arquivo ou arraste-o aqui: ").strip('"\'')
        converter_arquivo(caminho)