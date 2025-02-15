
import PyPDF2   # Biblioteca python para leitura de pdf

# definir caminho do arquivo pdf

caminho_arquivo = r"C:\\Users\\Anderson G Lignelli\\Downloads\\Data-Science\\anderson_gouveia_lignelli(DFE).pdf"



# abri e ler o arquivo pdf

with open (caminho_arquivo,"rb") as arquivo:
    leitor_pdf = PyPDF2.PdfReader(arquivo)
    texto = ""
    for pagina in leitor_pdf.pages:
        texto += pagina.extract_text()
        
        

 
# Exibição do conteúdo do arquivo pdf

print("Conteudo do arquivo PDF")
print(texto)


  
  
  