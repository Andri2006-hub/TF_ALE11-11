from abc import ABC, abstractmethod

# Abstração
class ServicoNotificacao(ABC):
    @abstractmethod
    def enviar(self, mensagem):
        pass

# Implementações concretas
class EmailService(ServicoNotificacao):
    def enviar(self, mensagem):
        print(f"Enviando email: {mensagem}")

class SMSService(ServicoNotificacao):
    def enviar(self, mensagem):
        print(f"Enviando SMS: {mensagem}")

class PushService(ServicoNotificacao):
    def enviar(self, mensagem):
        print(f"Enviando push: {mensagem}")

# Cliente depende da abstração, não da implementação concreta
class NotificacaoService:
    def _init_(self, servico: ServicoNotificacao):
        self.servico = servico

    def notificar(self, mensagem):
        self.servico.enviar(mensagem)

# Demonstração de uso com injeção de dependência
if _name_ == "_main_":
    email_service = EmailService()
    sms_service = SMSService()
    push_service = PushService()

    notificador1 = NotificacaoService(email_service)
    notificador2 = NotificacaoService(sms_service)
    notificador3 = NotificacaoService(push_service)

    mensagem = "Bem-vindo ao sistema!"
    notificador1.notificar(mensagem)
    notificador2.notificar(mensagem)
    notificador3.notificar(mensagem)