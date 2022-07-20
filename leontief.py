import numpy as np

class Leontief:
     def __init__(self, matriz_tecnologica):
          self._tamanho_matriz_tecnologica = len(matriz_tecnologica)
          self.matriz_leontief_inv = np.asmatrix((np.identity(self._tamanho_matriz_tecnologica) - matriz_tecnologica).I.round(3))
          self._media_colunas = np.array([self.matriz_leontief_inv[:, coluna].mean() for coluna in range(self._tamanho_matriz_tecnologica)])
          self._media_linhas = np.array([self.matriz_leontief_inv[linha, :].mean() for linha in range(self._tamanho_matriz_tecnologica)])
     
     def calcula_backward(self):
          leontief_inv = self.matriz_leontief_inv
          media_leontif_inv = leontief_inv.mean().round(3)

          backward = self._media_colunas / media_leontif_inv # Uj
          backward = backward.round(3)
          
          return backward
     
     def calcula_forward(self):
          leontief_inv = self.matriz_leontief_inv
          media_leontif_inv = leontief_inv.mean().round(3)

          forward = self._media_linhas / media_leontif_inv # Ui
          forward = forward.round(3)
          
          return forward

     def calcula_variacao_colunas(self):
          n = self._tamanho_matriz_tecnologica
          leontief_inv = self.matriz_leontief_inv
          
          somatorio_variacao_colunas = []
          for coluna in range(n):
               soma = 0
               for linha in range(n):
                    soma += (leontief_inv[linha, coluna] - self._media_colunas[coluna]) ** 2
               somatorio_variacao_colunas.append(soma)

          variacao_colunas = [np.sqrt(somatorio_variacao_colunas[index] / (n - 1)) / self._media_colunas[index] for index in range(n)]
          variacao_colunas = np.array(variacao_colunas).round(3)
          
          return variacao_colunas
     
     def calcula_variacao_linhas(self):
          n = self._tamanho_matriz_tecnologica
          leontief_inv = self.matriz_leontief_inv

          somatorio_variacao_linhas = []
          for linha in range(n):
               soma = 0
               for coluna in range(n):
                    soma += (leontief_inv[linha, coluna] - self._media_linhas[linha]) ** 2
               somatorio_variacao_linhas.append(soma)

          variacao_linhas = [np.sqrt(somatorio_variacao_linhas[index] / (n - 1)) / self._media_linhas[index] for index in range(n)]
          variacao_linhas = np.array(variacao_linhas).round(3)
          
          return variacao_linhas