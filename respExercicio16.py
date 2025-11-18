# respExercicio16.py

class ProcessadorPagamento:
    def processar_pagamento(self, valor, cartao):
        pass

class PayPalAPI:
    def make_payment(self, amount, credit_card_number):
        return f"PayPal: Processando ${amount} no cartão {credit_card_number}"

class PayPalAdapter(ProcessadorPagamento):
    def _init_(self, paypal_api):
        self.paypal_api = paypal_api

    def processar_pagamento(self, valor, cartao):
        return self.paypal_api.make_payment(valor, cartao)

class ProcessadorPagamentoInterno(ProcessadorPagamento):
    def processar_pagamento(self, valor, cartao):
        return f"Interno: Processando pagamento de ${valor} no cartão {cartao}"

class SistemaPagamento:
    def _init_(self, processador_pagamento: ProcessadorPagamento):
        self.processador_pagamento = processador_pagamento

    def realizar_pagamento(self, valor, cartao):
        resultado = self.processador_pagamento.processar_pagamento(valor, cartao)
        print(resultado)

# Demonstração do uso:
if _name_ == "_main_":
    # Sistema com processador interno
    processador_interno = ProcessadorPagamentoInterno()
    sistema1 = SistemaPagamento(processador_interno)
    sistema1.realizar_pagamento(100.0, "1234-5678")

    # Sistema com PayPal via Adapter
    paypal_api = PayPalAPI()
    paypal_adapter = PayPalAdapter(paypal_api)
    sistema2 = SistemaPagamento(paypal_adapter)
    sistema2.realizar_pagamento(200.0, "8765-4321")