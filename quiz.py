import json

# Perguntas e respostas do quiz
quiz_data = [
    {
        "pergunta": "Qual dos seguintes NÃO é um modelo de implantação da nuvem?",
        "opcoes": ["Pública", "Privada", "Híbrida", "Dedicada"],
        "resposta": "Dedicada"
    },
    {
        "pergunta": "O que o AWS IAM gerencia?",
        "opcoes": ["Redes Virtuais", "Usuários e permissões", "Monitoramento de custos", "Serviços de banco de dados"],
        "resposta": "Usuários e permissões"
    },
    {
        "pergunta": "Qual serviço AWS é usado para balanceamento de carga?",
        "opcoes": ["S3", "EC2", "ELB", "RDS"],
        "resposta": "ELB"
    },
    {
        "pergunta": "O que o AWS Cost Explorer ajuda a analisar?",
        "opcoes": ["Desempenho de aplicações", "Custos e padrões de uso", "Segurança e conformidade", "Alta disponibilidade"],
        "resposta": "Custos e padrões de uso"
    }
]

# Função para rodar o quiz
def executar_quiz():
    print("Simulado AWS Cloud Practitioner \n")
    pontos = 0

    for item in quiz_data:
        print(item["pergunta"])
        for i, opcao in enumerate(item["opcoes"], 1):
            print(f"{i}. {opcao}")
        
        resposta_usuario = input("\nDigite o número da opção correta: ")
        
        try:
            if item["opcoes"][int(resposta_usuario) - 1] == item["resposta"]:
                print("Correto!\n")
                pontos += 1
            else:
                print(f"Errado! A resposta correta é: {item['resposta']}\n")
        except (ValueError, IndexError):
            print("⚠️ Entrada inválida. Tente novamente.\n")

    print(f"Você acertou {pontos} de {len(quiz_data)} perguntas.")

# Iniciar o quiz
if __name__ == "__main__":
    executar_quiz()
