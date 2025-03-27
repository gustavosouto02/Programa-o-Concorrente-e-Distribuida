from PIL import Image
from tkinter import Tk, filedialog
import threading
import time

def converter_faixa_para_preto_e_branco(imagem, imagem_preto_branco, inicio_y, fim_y):
    largura, _ = imagem.size
    for x in range(largura):
        for y in range(inicio_y, fim_y):
            r, g, b = imagem.getpixel((x, y))
            luminancia = int(0.299 * r + 0.587 * g + 0.114 * b)
            imagem_preto_branco.putpixel((x, y), luminancia)

def converter_para_preto_e_branco_com_threads():
    try:
        root = Tk()
        root.withdraw()

        caminho_imagem = filedialog.askopenfilename(
            title="Selecione uma imagem",
            filetypes=[("Imagens", "*.jpg *.jpeg *.png *.bmp *.gif"), ("Todos os arquivos", "*.*")]
        )

        if not caminho_imagem:
            print("Nenhuma imagem foi selecionada.")
            return

        imagem = Image.open(caminho_imagem)
        imagem = imagem.convert("RGB")  # Garante que a imagem esteja no modo RGB
        largura, altura = imagem.size
        imagem_preto_branco = Image.new("L", (largura, altura))

        num_threads = 4  # Número de threads a serem utilizadas
        threads = []
        faixa_altura = altura // num_threads

        # Inicia a medição do tempo de conversão
        inicio_conversao = time.time()

        # Cria e inicia as threads
        for i in range(num_threads):
            inicio_y = i * faixa_altura
            fim_y = (i + 1) * faixa_altura if i != num_threads - 1 else altura
            thread = threading.Thread(target=converter_faixa_para_preto_e_branco, args=(imagem, imagem_preto_branco, inicio_y, fim_y))
            threads.append(thread)
            thread.start()

        # Aguarda todas as threads terminarem
        for thread in threads:
            thread.join()

        # Finaliza a medição do tempo de conversão
        fim_conversao = time.time()
        tempo_conversao = fim_conversao - inicio_conversao
        print(f"Tempo de conversão (com threads): {tempo_conversao:.2f} segundos")

        caminho_saida = filedialog.asksaveasfilename(
            title="Salvar imagem em preto e branco",
            defaultextension=".jpg",
            filetypes=[("JPEG", "*.jpg"), ("PNG", "*.png"), ("Todos os arquivos", "*.*")]
        )

        if not caminho_saida:
            print("Operação de salvamento cancelada.")
            return

        # Salva a imagem em preto e branco no caminho especificado
        imagem_preto_branco.save(caminho_saida)
        print(f"Imagem convertida com sucesso! Salva em: {caminho_saida}")

    except Exception as e:
        print(f"Erro ao processar a imagem: {e}")

# Exemplo de uso
if __name__ == "__main__":
    converter_para_preto_e_branco_com_threads()