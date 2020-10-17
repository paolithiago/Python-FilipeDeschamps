def limpa_dado(valor_n):                            # valor entre parenteses e o que é recebido da chamada da função e sera usada como parametro
  resultado = float(valor_n.replace("$",""))        # retira o cifrao usando o replace e depois converte para float
  return resultado                                  # retorna o valor da funcao para o que foi chamado
  
limpa_dado('$424.00')
