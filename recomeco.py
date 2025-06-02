# --- Projeto Recomeço - Plataforma de Apoio Psicológico Pós-Desastre ---

# Texto de boas-vindas exibido ao iniciar o programa
TEXTO_BOAS_VINDAS = """
==================================================
Bem-vindo(a) ao Recomeço - Apoio Console
Sua fonte de apoio psicológico pós-desastre.
==================================================
Este programa oferece informações e técnicas de autocuidado.
Lembre-se: isto NÃO substitui ajuda profissional qualificada.
Em caso de emergência ou crise, procure ajuda imediatamente.
"""

# Dicionário com contatos de emergência importantes
CONTATOS_EMERGENCIA = {
    "CVV (Centro de Valorização da Vida)": "188 (Apoio emocional 24h)",
    "SAMU (Serviço de Atendimento Móvel de Urgência)": "192 (Emergências médicas)",
    "Polícia Militar": "190 (Emergências de segurança)",
    "Defesa Civil": "199 (Alertas e suporte em desastres)",
    "Corpo de Bombeiros": "193 (Resgate e emergências)"
}

# Dicionário com listas de reações comuns ao trauma, separadas por categoria
REACOES_TRAUMA = {
    "Emocionais": [
        "Ansiedade e preocupação excessiva",
        "Tristeza profunda ou episódios de choro",
        "Medo intenso ou sensação de pânico",
        "Irritabilidade ou raiva desproporcional",
        "Sensação de vazio ou desconexão",
        "Culpa ou autorresponsabilização",
        "Dificuldade de sentir prazer ou alegria"
    ],
    "Físicas": [
        "Dificuldade para dormir ou pesadelos",
        "Fadiga constante ou falta de energia",
        "Dores de cabeça frequentes",
        "Tensão muscular ou dores no corpo",
        "Problemas digestivos ou perda de apetite",
        "Sensação de sufocamento ou respiração acelerada",
        "Palpitações ou coração acelerado"
    ],
    "Comportamentais e Cognitivas": [
        "Evitar lugares, pessoas ou conversas que lembrem o evento",
        "Isolamento social ou dificuldade de concentração",
        "Hipervigilância (estar sempre em alerta)",
        "Flashbacks ou lembranças intrusivas",
        "Dificuldade para tomar decisões",
        "Mudanças nos hábitos alimentares ou de sono",
        "Esquecimento ou confusão mental"
    ]
}

# Lista de itens para auto-observação emocional
AUTO_OBSERVACAO_ITENS = [
    "Tenho tido dificuldade para dormir nos últimos dias ou tenho dormido mais que o usual.",
    "Sinto-me constantemente em alerta, tenso(a) ou nervoso(a).",
    "Evito pensar, falar ou fazer coisas que me lembram o que aconteceu.",
    "Tenho menos interesse em atividades que antes me davam prazer.",
    "Sinto-me desconectado(a) das pessoas ao meu redor ou tenho me isolado.",
    "Tenho tido flashbacks, pesadelos ou lembranças indesejadas do evento.",
    "Sinto que minha vida mudou completamente e de forma negativa após o evento.",
    "Tenho dificuldade para me concentrar no trabalho, estudos ou em tarefas simples."
]

# Lista de sinais de alerta para buscar ajuda profissional
QUANDO_BUSCAR_AJUDA = [
    "Sintomas que persistem por mais de um mês sem melhora significativa.",
    "Pensamentos sobre se machucar, morrer ou desaparecer (ideação suicida).",
    "Incapacidade de realizar atividades básicas do dia a dia (higiene, alimentação).",
    "Uso aumentado ou problemático de álcool ou outras drogas para lidar com o sofrimento.",
    "Isolamento social extremo e prolongado.",
    "Sentimento de que os sintomas estão piorando com o tempo.",
    "Sofrimento emocional que parece insuportável ou fora de controle."
]

# Dicionário com técnicas de autocuidado, organizadas por categoria e situação
TECNICAS_AUTOCUIDADO = {
    "Alertas Imediatos": {
        "Flashback": [
            "Lembre-se: você está SEGURO(A) no presente.",
            "Olhe ao redor e nomeie 5 objetos que você vê.",
            "Toque uma superfície e descreva sua textura.",
            "Respire profundamente e devagar.",
            "Diga em voz alta: 'Isso já passou, estou seguro(a) agora.'"
        ],
        "Ataque de Pânico": [
            "Sente-se ou deite-se em um local seguro.",
            "Lembre-se: isso vai passar, você não está em perigo.",
            "Use a respiração 4-2-6 (Inspire por 4s, segure por 2s, expire por 6s).",
            "Coloque os pés firmemente no chão.",
            "Se possível, ligue para alguém de confiança."
        ]
    },
    "Exercício de Respiração Guiada (4-7-8)": [
        "Sente-se confortavelmente ou deite-se.",
        "1. Inspire calmamente pelo nariz contando mentalmente até 4.",
        "2. Segure a respiração contando mentalmente até 7.",
        "3. Expire completamente pela boca, fazendo um som suave, contando mentalmente até 8.",
        "4. Isto completa uma respiração. Repita o ciclo de 3 a 7 vezes ou até se sentir mais calmo(a)."
    ],
    "Técnicas Universais": {
        "Respiração 4-2-6": [
            "Técnica de respiração para reduzir ansiedade aguda:",
            "1. Inspire contando até 4.",
            "2. Segure a respiração por 2 segundos.",
            "3. Expire lentamente contando até 6.",
            "4. Repita por 5-10 ciclos."
        ],
        "Técnica 5-4-3-2-1 (Aterramento Sensorial)": [
            "Grounding sensorial para momentos de dissociação ou flashbacks:",
            "Nomeie:",
            "- 5 coisas que você pode VER ao seu redor.",
            "- 4 coisas que você pode TOCAR.",
            "- 3 coisas que você pode OUVIR.",
            "- 2 coisas que você pode CHEIRAR.",
            "- 1 coisa que você pode SABOREAR (ou uma emoção que está sentindo)."
        ],
        "Lugar Seguro Mental": [
            "Visualização para criar sensação de segurança:",
            "1. Feche os olhos e imagine um lugar real ou fictício onde você se sente completamente seguro(a) e em paz.",
            "2. Tente incluir detalhes sensoriais: o que você vê, ouve, cheira, sente na pele?",
            "3. Permaneça nesse lugar mental por alguns minutos, absorvendo a calma.",
            "4. Pratique 'visitar' este lugar regularmente, especialmente em momentos de ansiedade."
        ]
    },
    "Por Tipo de Desastre": {
        "Incêndios": {
            "Segurança no Agora (Aterramento)": [
                "Traga sua atenção ao presente para reduzir a sobrecarga de lembranças.",
                "1. Veja: 5 coisas ao redor não ligadas ao incêndio.",
                "2. Sinta: 4 texturas (roupas, cadeira).",
                "3. Ouça: 3 sons do ambiente atual.",
                "4. Afirme: 'O incêndio passou. Estou seguro(a) agora.'"
            ],
            "Ambiente de Calma": [
                "Crie um espaço que promova tranquilidade, longe de gatilhos.",
                "1. Identifique gatilhos: Cheiros (queimado) ou sons (sirenes) que causam ansiedade.",
                "2. Use cheiros calmantes: Lavanda, camomila (difusor) ou cozinhe algo agradável.",
                "3. Crie sons positivos: Músicas relaxantes, sons da natureza."
            ]
        },
        "Inundações": {
            "Ancoragem na Incerteza": [
                "Recrie um senso de normalidade e segurança.",
                "1. Rotina Mínima: Mantenha horários para dormir, acordar e comer.",
                "2. Espaço 'Seu': Organize um canto com seus pertences.",
                "3. Limite Notícias: Informe-se do essencial, evite excesso sobre o desastre."
            ],
             "Enfrentando o Medo com Preparação": [
                "Medo de novas chuvas é comum. Preparação e calma ajudam.",
                "1. Plano de Segurança: Tenha um kit de emergência e ponto de encontro familiar.",
                "2. Respiração Calmante: Pratique respiração diafragmática (lenta e profunda) ao sentir medo.",
                "3. Distração Positiva: Tenha atividades que acalmem (ler, ouvir música)."
            ]
        },
        "Deslizamentos": {
            "Encontrando Chão Firme": [
                "Deslizamentos abalam a segurança física. Crie um ambiente seguro e previsível.",
                "1. Local Seguro: Busque abrigo seguro. Informe-se antes de retornar.",
                "2. Atenção ao Corpo: Observe reações ao estresse. Use respiração para acalmar, especialmente com chuva/ruídos."
            ],
            "Acalmando Mente e Corpo": [
                "Memórias intrusivas e medo são comuns. Aterramento ajuda.",
                "1. Aterramento (5 sentidos): Reconecte-se ao presente durante flashbacks ou ansiedade.",
                "2. Valide Sentimentos: Converse sobre seus medos com alguém de confiança."
            ] 
        }
    }
}

# Lista de emoções disponíveis para o check-in emocional
EMOÇÕES_CHECKIN = [
    "Feliz", "Triste", "Ansioso(a)", "Calmo(a)", "Irritado(a)",
    "Cansado(a)", "Esperançoso(a)", "Confuso(a)", "Grato(a)", "Outro"
]
# Lista para armazenar o histórico de check-ins emocionais da sessão
historico_checkin = []

# --- Funções Utilitárias ---

# Limpa a tela do terminal, compatível com Windows e Unix
def limpar_tela():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

# Pausa a execução até o usuário pressionar Enter
def pausar_e_continuar():
    input("\nPressione Enter para continuar...")

# Solicita e valida uma escolha numérica do usuário dentro de um intervalo
def obter_escolha_numerica(min_val, max_val, mensagem_erro="Opção inválida."):
    while True:
        try:
            escolha = int(input("Escolha uma opção: "))
            if min_val <= escolha <= max_val:
                return escolha
            else:
                print(f"{mensagem_erro} Por favor, escolha um número entre {min_val} e {max_val}.")
        except ValueError:
            print(f"{mensagem_erro} Por favor, digite um número.")

# Exibe uma lista numerada de itens, com título opcional
def exibir_lista_com_numeros(lista_itens, titulo=""):
    if titulo:
        print(f"\n--- {titulo} ---")
    for i, item in enumerate(lista_itens, 1):
        print(f"{i}. {item}")

# --- Funções dos Módulos ---

# Exibe os contatos de emergência cadastrados
def mostrar_contatos_emergencia():
    limpar_tela()
    print("--- Contatos de Emergência ---")
    if not CONTATOS_EMERGENCIA:
        print("Nenhum contato de emergência cadastrado.")
    else:
        for servico, numero in CONTATOS_EMERGENCIA.items():
            print(f"- {servico}: {numero}")
    print("\nLembre-se: Em caso de perigo imediato à vida, ligue para o SAMU (192) ou Bombeiros (193).")
    print("Para apoio emocional urgente, o CVV (188) está disponível 24h.")
    pausar_e_continuar()

# Módulo para entender emoções e reações ao trauma
# Oferece submenus para ver reações, auto-observação e sinais de alerta
def entender_emocoes():
    while True:
        limpar_tela()
        print("--- Entendendo Suas Emoções e Reações ---")
        print("É normal ter diversas reações após um evento traumático. Conhecê-las é o primeiro passo.")
        print("1. Ver Reações Comuns ao Trauma")
        print("2. Auto-observação Guiada (Reflexão)")
        print("3. Quando Buscar Ajuda Profissional")
        print("4. Voltar ao Menu Principal")

        escolha = obter_escolha_numerica(1, 4)

        if escolha == 1:
            limpar_tela()
            print("--- Reações Comuns ao Trauma ---")
            for categoria, lista_reacoes in REACOES_TRAUMA.items():
                exibir_lista_com_numeros(lista_reacoes, categoria)
                print("-" * 20)
            pausar_e_continuar()
        elif escolha == 2:
            fazer_auto_observacao()
        elif escolha == 3:
            limpar_tela()
            exibir_lista_com_numeros(QUANDO_BUSCAR_AJUDA, "Sinais Importantes: Quando Buscar Ajuda Profissional")
            print("\nSe você se identifica com vários destes sinais, especialmente ideação suicida, procure ajuda URGENTEMENTE.")
            pausar_e_continuar()
        elif escolha == 4:
            break

# Permite ao usuário refletir sobre seus sentimentos recentes, respondendo a itens de auto-observação
# Dá um feedback baseado na quantidade de respostas positivas
def fazer_auto_observacao():
    limpar_tela()
    print("--- Auto-observação Guiada ---")
    print("Esta não é uma avaliação diagnóstica, mas um convite para você observar como tem se sentido.")
    print("Responda 's' para sim ou 'n' para não para cada item abaixo:")

    respostas_positivas = 0
    for i, item in enumerate(AUTO_OBSERVACAO_ITENS, 1):
        while True:
            resposta = input(f"{i}. {item} (s/n): ").strip().lower()
            if resposta in ['s', 'n']:
                if resposta == 's':
                    respostas_positivas += 1
                break
            else:
                print("Resposta inválida. Por favor, digite 's' ou 'n'.")
    
    print("\n--- Feedback da Reflexão ---")
    print(f"Você marcou 'sim' para {respostas_positivas} de {len(AUTO_OBSERVACAO_ITENS)} itens.")

    # Feedback personalizado conforme o número de respostas positivas
    if respostas_positivas == 0:
        print("Que bom que você está se observando. Mesmo sem marcar itens 'sim',")
        print("refletir sobre seu bem-estar é um passo importante.")
    elif 1 <= respostas_positivas <= 3:
        print("É comum vivenciar algumas dessas reações após um evento difícil.")
        print("Observar seus sentimentos é um bom começo. Continue se cuidando e,")
        print("se algo te preocupar mais intensamente ou persistir, considere conversar")
        print("com alguém de confiança ou um profissional.")
    elif 4 <= respostas_positivas <= 6:
        print("Marcar vários itens indica que você pode estar passando por um momento")
        print("desafiador e sentindo o impacto do evento de forma mais significativa.")
        print("É importante não minimizar suas experiências. Se esses sentimentos são")
        print("intensos ou duram mais de algumas semanas, buscar apoio profissional")
        print("pode te ajudar a lidar melhor com eles.")
    else: # >= 7
        print("Você marcou uma quantidade considerável de itens, o que sugere que o impacto")
        print("emocional do evento pode estar sendo bastante intenso e afetando diversas áreas")
        print("da sua vida. É muito importante que você não passe por isso sozinho(a).")
        print("Considerar seriamente uma conversa com um profissional de saúde mental")
        print("pode ser um passo crucial para sua recuperação e bem-estar.")
    
    print("\nLembre-se: este é apenas um exercício de reflexão. Para um diagnóstico ou")
    print("apoio especializado, procure um profissional de saúde mental.")
    pausar_e_continuar()

# Menu principal das técnicas de autocuidado, com submenus para cada categoria
# Permite navegar entre técnicas imediatas, universais, por desastre, etc.
def tecnicas_autocuidado_menu():
    while True:
        limpar_tela()
        print("--- Técnicas de Autocuidado ---")
        print("Escolha uma categoria de técnica:")
        print("1. Alertas Imediatos (Flashback / Ataque de Pânico)")
        print("2. Exercício de Respiração Guiada (4-7-8)")
        print("3. Técnicas Universais de Acalmamento")
        print("4. Técnicas por Tipo de Desastre")
        print("5. Voltar ao Menu Principal")

        escolha_tecnica = obter_escolha_numerica(1, 5)

        if escolha_tecnica == 1:
            sub_menu_alertas_imediatos()
        elif escolha_tecnica == 2:
            limpar_tela()
            print("--- Exercício de Respiração Guiada (4-7-8) ---")
            for passo in TECNICAS_AUTOCUIDADO["Exercício de Respiração Guiada (4-7-8)"]:
                print(f"- {passo}")
            pausar_e_continuar()
        elif escolha_tecnica == 3:
            sub_menu_tecnicas_universais()
        elif escolha_tecnica == 4:
            sub_menu_tecnicas_por_desastre()
        elif escolha_tecnica == 5:
            break

# Submenu para técnicas de alerta imediato (flashback ou ataque de pânico)
def sub_menu_alertas_imediatos():
    limpar_tela()
    print("--- Alertas Imediatos ---")
    print("Se você está tendo um...")
    print("1. Flashback AGORA")
    print("2. Ataque de Pânico AGORA")
    print("3. Voltar")
    escolha_alerta = obter_escolha_numerica(1, 3)
    if escolha_alerta == 1:
        limpar_tela()
        exibir_lista_com_numeros(TECNICAS_AUTOCUIDADO["Alertas Imediatos"]["Flashback"], "Lidando com Flashback")
        pausar_e_continuar()
    elif escolha_alerta == 2:
        limpar_tela()
        exibir_lista_com_numeros(TECNICAS_AUTOCUIDADO["Alertas Imediatos"]["Ataque de Pânico"], "Lidando com Ataque de Pânico")
        pausar_e_continuar()

# Submenu para técnicas universais de acalmamento
def sub_menu_tecnicas_universais():
    while True:
        limpar_tela()
        print("--- Técnicas Universais de Acalmamento ---")
        opcoes_universais = list(TECNICAS_AUTOCUIDADO["Técnicas Universais"].keys())
        exibir_lista_com_numeros(opcoes_universais)
        print(f"{len(opcoes_universais) + 1}. Voltar")
        
        escolha = obter_escolha_numerica(1, len(opcoes_universais) + 1)
        if escolha == len(opcoes_universais) + 1:
            break
        else:
            tecnica_selecionada = opcoes_universais[escolha-1]
            limpar_tela()
            exibir_lista_com_numeros(TECNICAS_AUTOCUIDADO["Técnicas Universais"][tecnica_selecionada], tecnica_selecionada)
            pausar_e_continuar()

# Submenu para técnicas por tipo de desastre (incêndios, inundações, deslizamentos)
def sub_menu_tecnicas_por_desastre():
    while True:
        limpar_tela()
        print("--- Técnicas por Tipo de Desastre ---")
        tipos_desastre = list(TECNICAS_AUTOCUIDADO["Por Tipo de Desastre"].keys())
        exibir_lista_com_numeros(tipos_desastre)
        print(f"{len(tipos_desastre) + 1}. Voltar")

        escolha_tipo = obter_escolha_numerica(1, len(tipos_desastre) + 1)
        if escolha_tipo == len(tipos_desastre) + 1:
            break
        else:
            desastre_selecionado = tipos_desastre[escolha_tipo-1]
            while True:
                limpar_tela()
                print(f"--- Técnicas para {desastre_selecionado} ---")
                tecnicas_especificas = list(TECNICAS_AUTOCUIDADO["Por Tipo de Desastre"][desastre_selecionado].keys())
                exibir_lista_com_numeros(tecnicas_especificas)
                print(f"{len(tecnicas_especificas) + 1}. Voltar para Tipos de Desastre")
                
                escolha_tecnica_especifica = obter_escolha_numerica(1, len(tecnicas_especificas) + 1)
                if escolha_tecnica_especifica == len(tecnicas_especificas) + 1:
                    break
                else:
                    nome_tecnica = tecnicas_especificas[escolha_tecnica_especifica-1]
                    limpar_tela()
                    exibir_lista_com_numeros(TECNICAS_AUTOCUIDADO["Por Tipo de Desastre"][desastre_selecionado][nome_tecnica], nome_tecnica)
                    pausar_e_continuar()

# Permite ao usuário registrar como está se sentindo no momento (check-in emocional)
# Armazena o registro no histórico da sessão e dá um feedback simples
def fazer_checkin_emocional():
    limpar_tela()
    print("--- Check-in Emocional ---")
    print("Como você está se sentindo predominantemente agora?")
    exibir_lista_com_numeros(EMOÇÕES_CHECKIN)
    
    escolha = obter_escolha_numerica(1, len(EMOÇÕES_CHECKIN))
    emocao_escolhida = EMOÇÕES_CHECKIN[escolha-1]

    if emocao_escolhida == "Outro":
        outra_emocao = input("Por favor, descreva a emoção: ").strip()
        if not outra_emocao:
            print("Nenhuma emoção descrita.")
            pausar_e_continuar()
            return
        emocao_escolhida = f"Outro ({outra_emocao})"

    from datetime import datetime
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    historico_checkin.append({"timestamp": timestamp, "emocao": emocao_escolhida}) # Armazenamento de dados em listas (e dicionários)
    
    print(f"\nRegistrado: {emocao_escolhida} em {timestamp}")
    print("Obrigado por compartilhar. Reconhecer suas emoções é um passo importante.")
    
    # Feedback simples baseado na emoção
    if emocao_escolhida.lower() in ["triste", "ansioso(a)", "irritado(a)", "cansado(a)", "confuso(a)"]:
        print("Lembre-se de ser gentil consigo mesmo(a). As técnicas de autocuidado podem ajudar.")
        print("Se esses sentimentos persistirem intensamente, considere conversar com alguém de confiança ou buscar apoio.")
    elif emocao_escolhida.lower() in ["feliz", "calmo(a)", "esperançoso(a)", "grato(a)"]:
        print("Que bom que você está se sentindo assim! Aproveite este momento.")
    
    pausar_e_continuar()

# Exibe o histórico de check-ins emocionais feitos na sessão atual
def ver_historico_checkin():
    limpar_tela()
    print("--- Histórico de Check-ins Emocionais (desta sessão) ---")
    if not historico_checkin:
        print("Nenhum check-in emocional feito nesta sessão.")
    else:
        for entrada in historico_checkin:
            print(f"- Em {entrada['timestamp']}: {entrada['emocao']}")
    pausar_e_continuar()

# Exibe informações e orientações sobre fome e assistência alimentar pós-desastre.
def informacoes_fome_alimentar():
    limpar_tela()
    print("--- Fome e Assistência Alimentar Pós-Desastre ---")
    print("A fome e a insegurança alimentar são consequências comuns após desastres.")
    print("Se você ou sua família estão enfrentando dificuldades para se alimentar:")
    print("- Procure o CRAS (Centro de Referência de Assistência Social) mais próximo.")
    print("- Informe-se sobre bancos de alimentos, cozinhas comunitárias e doações em sua cidade.")
    print("- Contatos úteis:")
    print("  - Disque 100 (Direitos Humanos)")
    print("  - Prefeitura Municipal / Defesa Civil")
    print("  - Igrejas e ONGs locais")
    print("\nA fome pode afetar não só o corpo, mas também a saúde emocional. Se você sentir tristeza, ansiedade ou desespero por falta de alimentos, procure apoio psicológico e social.")
    pausar_e_continuar()

# --- Menu Principal ---

# Função principal que exibe o menu inicial e gerencia a navegação entre os módulos
def menu_principal():
    print(TEXTO_BOAS_VINDAS)
    pausar_e_continuar()

    while True: # Estrutura de repetição
        limpar_tela()
        print("\n--- Menu Principal Recomeço ---")
        print("Como podemos te ajudar hoje?")
        print("1. Ver Contatos de Emergência")
        print("2. Entender Minhas Emoções e Reações")
        print("3. Técnicas de Autocuidado")
        print("4. Fazer um Check-in Emocional Rápido")
        print("5. Ver Histórico de Check-ins (desta sessão)")
        print("6. Informações sobre Fome e Assistência Alimentar")
        print("7. Sair")

        escolha = obter_escolha_numerica(1, 7) # Validação de dados de entrada

        # Estruturas de decisão
        if escolha == 1:
            mostrar_contatos_emergencia()
        elif escolha == 2:
            entender_emocoes()
        elif escolha == 3:
            tecnicas_autocuidado_menu()
        elif escolha == 4:
            fazer_checkin_emocional()
        elif escolha == 5:
            ver_historico_checkin()
        elif escolha == 6:
            informacoes_fome_alimentar()
        elif escolha == 7:
            limpar_tela()
            print("Obrigado por usar o Recomeço - Apoio Console. Cuide-se!")
            print("Lembre-se, buscar ajuda profissional é um ato de coragem e autocuidado.")
            break
            
        # Processamento adequado das informações e Exibição clara das informações de output são feitos dentro de cada função.

# Ponto de entrada do programa: executa o menu principal se o script for chamado diretamente
if __name__ == "__main__":
    menu_principal()