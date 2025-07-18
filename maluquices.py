from datetime import timedelta

class BancoDeHoras:
    def __init__(self, saldo_inicial=timedelta(0)):
        """
        Inicializa o banco de horas com um saldo inicial.

        Args:
            saldo_inicial (timedelta): O saldo inicial de horas (padrão: 0).
        """
        self.saldo = saldo_inicial

    def adicionar_horas(self, tempo):
        """
        Adiciona horas ao banco.

        Args:
            tempo (timedelta): O tempo a ser adicionado.
        """
        self.saldo += tempo

    def subtrair_horas(self, tempo):
        """
        Subtrai horas do banco, permitindo saldo negativo.

        Args:
            tempo (timedelta): O tempo a ser subtraído.
        """
        self.saldo -= tempo

    def obter_saldo(self):
        """
        Retorna o saldo atual do banco de horas.

        Returns:
            timedelta: O saldo atual.
        """
        return self.saldo

    def __str__(self):
        """
        Retorna uma representação em string do saldo.
        """
        total_segundos = self.saldo.total_seconds()
        sinal = "+" if total_segundos >= 0 else "-"
        total_segundos = abs(total_segundos)
        horas, resto = divmod(total_segundos, 3600)
        minutos, segundos = divmod(resto, 60)
        return f"{sinal}{int(horas):02}:{int(minutos):02}:{int(segundos):02}"
    

banco = BancoDeHoras(saldo_inicial=timedelta(hours=1, minutes=30)) 

horas_usadas = timedelta(hours=2)
banco.subtrair_horas(horas_usadas)
print(f"Saldo após subtrair horas: {banco}") 