# python
Repositório Python Global Solution

Documentação do Projeto Recomeço - Apoio Console

1. Introdução e Descritivo do Projeto

O "Recomeço - Apoio Console" é uma aplicação em Python desenvolvida para oferecer suporte psicológico básico e informações de autocuidado para indivíduos afetados por eventos extremos e desastres. A plataforma visa ser um recurso inicial e acessível, fornecendo acesso rápido a contatos de emergência, compreensão de reações emocionais comuns ao trauma, técnicas de autocuidado e um sistema de check-in emocional. É fundamental ressaltar que o programa não substitui a ajuda profissional qualificada, mas serve como um facilitador de informações e um primeiro passo no processo de recuperação emocional.

2. Contexto e Justificativa

Eventos extremos, como desastres naturais, podem ter um impacto devastador na saúde mental e emocional das pessoas. Em momentos de crise, o acesso rápido a informações confiáveis e a ferramentas de suporte pode ser crucial. O "Recomeço" surge como uma resposta a essa necessidade, utilizando a tecnologia para oferecer um canal de apoio inicial. A justificativa para este projeto reside na lacuna de ferramentas de apoio psicológico imediato e acessível em contextos pós-desastre, onde o suporte profissional pode não estar imediatamente disponível ou onde as pessoas podem ter dificuldades em buscar ajuda. O programa busca preencher essa lacuna, promovendo o autocuidado e fornecendo recursos essenciais.

3. Objetivos do Projeto

3.1. Objetivo Geral

Fornecer uma plataforma de console acessível e informativa para apoio psicológico básico e promoção do autocuidado para indivíduos em situações de pós-desastre.

3.2. Objetivos Específicos

Acesso Rápido a Contatos de Emergência: Disponibilizar uma lista clara e acessível de telefones de emergência para situações de crise.
Educação sobre Reações ao Trauma: Informar os usuários sobre as reações emocionais, físicas, cognitivas e comportamentais comuns ao trauma, ajudando-os a entender e normalizar suas experiências.
Técnicas de Autocuidado: Oferecer um repertório de técnicas de autocuidado, como exercícios de respiração, aterramento e atenção plena, para auxiliar no manejo do estresse e da ansiedade.
Check-in Emocional Simplificado: Permitir que os usuários registrem seu estado emocional atual e visualizem um histórico rápido de seus check-ins para acompanhar seu bem-estar.
Informações sobre Assistência Alimentar: Prover acesso a informações sobre recursos e assistência relacionados à fome e segurança alimentar, um problema frequentemente agravado por desastres.
Interface Intuitiva: Desenvolver uma interface de usuário baseada em console que seja simples e fácil de navegar, mesmo para aqueles com pouco conhecimento técnico.
4. Funcionalidades Implementadas

4.1. Estrutura Modular do Código

O código do "Recomeço" é estruturado de forma modular, com funções bem definidas para cada funcionalidade. Isso facilita a manutenção, a legibilidade e a expansão futura do projeto. As principais funções e módulos incluem:

limpar_tela(): Responsável por limpar o console para uma melhor experiência do usuário.
pausar_execucao(): Pausa a execução do programa para permitir que o usuário leia as informações.
obter_escolha_numerica(minimo, maximo): Valida a entrada numérica do usuário para garantir que seja uma opção válida dentro de um intervalo.
mostrar_contatos_emergencia(): Exibe os contatos de emergência predefinidos.
entender_emocoes(): Apresenta informações sobre as reações comuns ao trauma, divididas por categorias.
tecnicas_autocuidado_menu(): Gerencia o submenu de técnicas de autocuidado.
fazer_checkin_emocional(): Permite ao usuário registrar seu estado emocional e uma breve nota.
ver_historico_checkin(): Exibe o histórico de check-ins emocionais da sessão atual.
informacoes_fome_alimentar(): Fornece informações e links relacionados à assistência alimentar.
main(): A função principal que orquestra o menu principal e a lógica do programa.
4.2. Gerenciamento de Dados

Os dados são gerenciados através de estruturas de dados Python (dicionários e listas) diretamente no código, para informações estáticas como contatos de emergência, reações ao trauma e técnicas de autocuidado. O histórico de check-ins emocionais é armazenado em uma lista durante a execução do programa e é volátil (não persistente após o fechamento).

TEXTO_BOAS_VINDAS: String que contém a mensagem de boas-vindas exibida na inicialização.
CONTATOS_EMERGENCIA: Dicionário que armazena os nomes das instituições e seus respectivos números de telefone.
REACOES_TRAUMA: Dicionário que categoriza e lista reações comuns ao trauma (Emocionais, Físicas, Cognitivas, Comportamentais).
TECNICAS_AUTOCUIDADO: Dicionário que agrupa técnicas de autocuidado por tipo (Físicas, Mentais, Emocionais, Sociais).
HISTORICO_CHECKIN: Lista global que armazena os check-ins emocionais da sessão atual.
4.3. Fluxo de Menus e Navegação

O programa opera através de um sistema de menus interativos, guiando o usuário pelas diferentes funcionalidades.

4.3.1. Menu Principal (main()):

O ponto de entrada do programa, exibindo uma mensagem de boas-vindas e as opções principais.

Opções:

1. Ver Contatos de Emergência: Redireciona para a funcionalidade de exibição de contatos.
2. Entender Minhas Emoções e Reações: Redireciona para a funcionalidade de explicação sobre reações ao trauma.
3. Técnicas de Autocuidado: Acessa o submenu de técnicas de autocuidado.
4. Fazer um Check-in Emocional Rápido: Permite registrar um novo check-in.
5. Ver Histórico de Check-ins (desta sessão): Exibe os check-ins realizados na sessão atual.
6. Informações sobre Fome e Assistência Alimentar: Fornece informações relevantes sobre o tema.
7. Sair: Encerra o programa.
Processo:

Exibe o TEXTO_BOAS_VINDAS.
Entra em um loop contínuo que exibe o "Menu Principal Recomeço".
Solicita ao usuário uma escolha numérica (validada pela função obter_escolha_numerica).
Utiliza uma estrutura if/elif/else para direcionar a execução para a função correspondente à escolha do usuário.
Em caso de escolha inválida, exibe uma mensagem de erro e repete o menu.
Se a escolha for "Sair", limpa a tela, exibe uma mensagem de despedida e encerra o loop.
4.3.2. Submenu de Técnicas de Autocuidado (tecnicas_autocuidado_menu()):

Acessível através da opção "3. Técnicas de Autocuidado" no Menu Principal.

Opções:

1. Técnicas Físicas: Exibe técnicas de autocuidado focadas no corpo.
2. Técnicas Mentais: Exibe técnicas de autocuidado focadas na mente.
3. Técnicas Emocionais: Exibe técnicas de autocuidado para o manejo das emoções.
4. Técnicas Sociais: Exibe técnicas de autocuidado relacionadas à interação social.
5. Voltar ao Menu Principal: Retorna ao menu anterior.
Processo:

Exibe o "Menu de Técnicas de Autocuidado".
Solicita uma escolha numérica (validada).
Com base na escolha, exibe as técnicas correspondentes do dicionário TECNICAS_AUTOCUIDADO.
Após exibir as informações, pausa a execução e, em seguida, retorna ao próprio submenu até que o usuário escolha "Voltar".
4.4. Detalhamento das Funcionalidades

Ver Contatos de Emergência (mostrar_contatos_emergencia):

Exibe uma lista formatada dos contatos de emergência, incluindo o nome da instituição e seu respectivo número de telefone, conforme definido em CONTATOS_EMERGENCIA.
Exemplo: CVV (Centro de Valorização da Vida): 188 (Apoio emocional 24h).
Entender Minhas Emoções e Reações (entender_emocoes):

Apresenta uma explicação inicial sobre a normalidade das reações ao trauma.
Lista as reações comuns ao trauma, categorizadas em "Emocionais", "Físicas", "Cognitivas" e "Comportamentais", utilizando o dicionário REACOES_TRAUMA.
Cada categoria é exibida com seus respectivos itens.
Fazer um Check-in Emocional Rápido (fazer_checkin_emocional):

Solicita ao usuário que avalie seu estado emocional em uma escala de 1 a 5.
Pede uma breve nota sobre o que está sentindo.
Registra a data e hora do check-in.
Armazena o check-in (avaliação, nota, data/hora) na lista HISTORICO_CHECKIN.
Ver Histórico de Check-ins (desta sessão) (ver_historico_checkin):

Verifica se há check-ins no HISTORICO_CHECKIN.
Se houver, exibe cada check-in com a data, hora, avaliação e nota.
Se não houver check-ins, informa o usuário.
Informações sobre Fome e Assistência Alimentar (informacoes_fome_alimentar):

Fornece uma mensagem de introdução sobre a importância da assistência alimentar.
Lista informações como "Bancos de Alimentos Locais", "Programas Sociais do Governo" e "Organizações Não Governamentais (ONGs)" com descrições genéricas e a recomendação de buscar informações específicas na região do usuário.
5. Conclusão

O "Recomeço - Apoio Console" representa um esforço para utilizar a programação Python no desenvolvimento de uma ferramenta de suporte psicossocial em momentos de necessidade. Ao oferecer acesso facilitado a informações de emergência, educação sobre o trauma, técnicas de autocuidado e um sistema de autoavaliação emocional, o projeto busca empoderar os usuários e guiá-los para um caminho de recuperação e bem-estar. Embora não substitua a intervenção profissional, o "Recomeço" serve como um recurso valioso de primeiro contato, demonstrando o potencial da tecnologia para promover a saúde mental e a resiliência em comunidades afetadas por eventos extremos. A simplicidade e a acessibilidade de sua interface de console garantem que ele possa ser utilizado em diversas situações, reforçando a mensagem de que "buscar ajuda profissional é um ato de coragem e autocuidado."
