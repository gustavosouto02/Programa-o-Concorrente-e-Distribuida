'''
Q01 Crie um sistema bancário simples em Python onde múltiplas threads realizam transações (depósitos e
saques) em contas compartilhadas.
Observações:
• Identifique e corrija condições de corrida no saldo das contas.
• Garanta que o saldo nunca fique inconsistente, mesmo com operações concorrentes.


Q02 Simule um pedágio com múltiplas cabines de pagamento e carros chegando simultaneamente.
Observações:
• Use locks para garantir que cada carro pague em apenas uma cabine.
• Evite deadlocks caso um carro tente acessar uma cabine ocupada.


Q03 Um estacionamento tem 10 vagas disponíveis e múltiplos carros tentam entrar ao mesmo tempo.
Observações:
• Use semáforos para controlar o acesso às vagas.
• Garanta que nenhum carro seja bloqueado indefinidamente (evitar starvation).


Q04 Um sistema de reserva permite que múltiplos usuários reservem assentos em um voo com capacidade
limitada.
Observações:
• Garanta que dois usuários não reservem o mesmo assento simultaneamente.
• Minimize o overhead de sincronização para permitir reservas rápidas.
'''