
import abc  

class Conta(abc.ABC):
    def __init__(self, agencia: int, conta: int, saldo: float = 0):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo
    
    @abc.abstractmethod
    def sacar(self, valor: float) -> float:
        ...

    def depositar(self, valor):
        self.saldo += valor
        self.detalhes(f'(DEPOSITO {valor})')
        return self.saldo

    def detalhes(self, msg='') -> None:
        print(f'O seu saldo e {self.saldo:.2f} {msg}') 

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.conta!r}, {self.saldo})'
        return f'{class_name} {attrs}'

# class name contaPopanca é herança da classe Conta
        
class ContaPoupanca(Conta):
    def sacar(self, valor) -> float:
        valor_pos_saque = self.saldo - valor

        if valor_pos_saque >= 0:
            self.saldo -= valor
            self.detalhes(f'(SAQUE {valor})')
            return self.saldo
    
        print('Nao foi possivel sacar o valor desejado')
        self.detalhes(f'(SAQUE NEGADO {valor})')
        return self.saldo

# class name contaCorrente é herança da classe Conta com limite pre definido

class ContaCorrente(Conta):
    def __inti__(self, agencia: int, conta: int, saldo: float = 0, limite: float = 0):
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def sacar(self, valor) -> float:
        valor_pos_saque = self.saldo - valor
        lite_maximo = -self.limite

        if valor_pos_saque >= lite_maximo:
            self.saldo -= valor
            self.detalhes(f'(SAQUE {valor})')
            return self.saldo
        
        print('Nao foi possivel sacar o valor desejado')
        print(f'Seu limite e {-self.limite:.2f}')
        self.detalhes(f'(SAQUE NEGADO {valor})')
        return self.saldo
    

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self  .conta!r}, {self.saldo}, {self.limite} )'
        return f'{class_name} {attrs}'


if __name__ == '__main__':
    cp1 = ContaPoupanca(111, 222, 0)
    cp1.sacar(1)