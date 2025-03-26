import veiculo
import locale
import pytz
from datetime import datetime

class Carro(veiculo.Veiculo):
  def interacao(self):
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    hora_atual = datetime.now(pytz.timezone('America/Sao_Paulo')).strftime('%d/%m/%Y %H:%M:%S')
    valor_formatado = locale.currency(self.getValor(), symbol = True, grouping = True, international = False)
    print(f"Marca: {self.getMarca()}")
    print(f"Modelo: {self.getModelo()}")
    print(f"Cor: {self.getCor()}")
    print(f"Ano: {self.getAno()}")
    print(f"Valor: {valor_formatado}")
    print(f"Código compilado em: {hora_atual}")
