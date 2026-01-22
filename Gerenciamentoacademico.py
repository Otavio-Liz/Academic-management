
# Nome: Otávio Moraes Lisboa
# Curso: Gestão de Tecnologia da Informação
# Atividade: Atividade Formativa - S5
# Data: 02/05/2025 
import json







#FUNÇÃO PARA SALVAR ARQUIVO
def salvar_arquivos(lista_qualquer, nome_arquivo):
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        json.dump(lista_qualquer, arquivo, ensure_ascii=False, indent= 4)

#FUNÇÃO PARA LER ARQUIVO
def ler_arquivo(arquivo):
    try:
        with open(arquivo, 'r') as file:
            lista_qualquer = json.load(file)
        return lista_qualquer
    except FileNotFoundError:
        print('Arquivo inesistente')
    return []

#FUNÇÃO PARA MOSTRAR O MENU PRINCIPAL
def menu_principal():
        print('=== MENU PRINCIPAL ===')
        print('1. Estudante')
        print('2. Disciplina')
        print('3. Professor')
        print('4. Turma')
        print('5. Matrícula')
        print('0. Sair')
        
        
        return int(input('Selecione uma das opções:'))

#BLOCO DE FUNÇÕES DE INCLUSÃO(ESTUDANTES, DISCIPLINAS, PROFESSORES, TURMAS E MATRÍCULAS.)
def incluir_disciplinas():
    disciplinas = ler_arquivo('disciplines.json')
    while True:
        #usamos a tratativas de excessões para se caso o usuário digite um valor inválido ou, por exemplo, digite uma tecla (enter).
        try:
            codigo_disciplina = int(input('Digite o código da disciplina: '))
        except ValueError:
            print('Digite um valor válido!')
            continue
        # Verificamos se o código que o usuário digitou já está cadastrado, percorrendo a lista de disciplinas e comparando os valores. 
        for disciplina in disciplinas:
            # Se o código que for inserido pelo usuário, armazenado na variável (codigo_disciplina), for igual(==), ao que já temos armazenado na lista:
            if disciplina['codigo'] == codigo_disciplina:
                print('Disciplina já cadastrada!') #Essa mensagem irá ser impressa na tela para o usuário e:
                break # O comando break irá parar o processo do código.
        
        # 'Se-não', se o código for de uma nova disciplina, vamos dar continuidade na inclusão.
        else: 
            # Pdiremos o nome da nova disciplina:
            nome = str(input('Digite o nome da disciplina'))
            # Então criaremos um dicionário que irá armazenar pares de chave-valor, contendo o código digitado e o nome que pedimos anteiormente. 
            nova_disciplina = {'codigo': codigo_disciplina,
                           'nome': nome
            }
            # Feito o discionário, agora iremos "jogar"/"colocar" ou "inserir" esse discionário à nossa lista, onde será armazenado os valores. 
            # Pois podemos precisar desses valores para atualizar, excluir ou listar.
            
            disciplinas.append(nova_disciplina)
            # Ao adicionarmos o discionário na lista de disciplinas, agora salvaremos essas informações em arquivo.
            salvar_arquivos(disciplinas, 'disciplines.json')
            print('Disciplina cadastrada com sucesso!')
        # Criamos uma nova variável que irá servir apenas para armazenar um valor. Esse valor será comparado. Vamos perguntar ao usuário se ele pretende continuar adicionando mais disciplinas. 
        #Se o valor que for inserido for igual(==) ao valor que é pra parar de cadastrar 'n', então o break irá interromper o fluxo da execução.
        incluir_mais_disciplinas = input('Deseja cadastrar uma nova disciplina?(s/n)')
        if incluir_mais_disciplinas == 'n':
            break               
	# ESSA LÓGICA SE APLICA PARA TODAS AS FUNÇÕES POSTERIORES DE INCLUSÃO DE ELEMENTOS.

#Função para Incluir professores
def incluir_professores():
    professores = ler_arquivo('teachers.json')
    while True:
        try:
            codigo_professor = int(input('Digite o código do professor'))
        except ValueError:
            print('Digite um valor válido!')
            continue
        # Verifica se o código já está cadastrado
        for professor in professores:
            if professor['codigo'] == codigo_professor:
                print('Professor já cadastrado!')
                break
        else:
            nome = str(input('Digite o nome do professor:'))
            cpf = str(input('Digite o cpf do professor:'))
            novo_professor = {
                        'codigo': codigo_professor,
                        'nome': nome,
                        'cpf': cpf
            }
            
            professores.append(novo_professor)
            salvar_arquivos(professores, 'teachers.json')
            print('Professor cadastrado com sucesso!')  
        
        incluir_mais_professores = input('Deseja cadastrar um novo professor(a)?(s/n)')
        if incluir_mais_professores == 'n':
            break
#Função para Incluir turmas
def incluir_turmas():
    turmas = ler_arquivo('classes.json')
    while True:
        try:
            codigo_turma = int(input('Digite o código da turma:'))
        except ValueError:
            print('Digite um valor válido!')
            continue
        # Verifica se o código já está cadastrado
        for turma in turmas:
            if turma['codigo'] == codigo_turma:
                print('Turma já cadastrado!')
                break
        else:
            codigo_professor = int(input('Digite o código do professor:'))
            codigo_disciplina = int(input('Digite o código da disciplina:'))

            nova_turma = {
                    'codigo': codigo_turma,
                    'codigo_professor': codigo_professor,
                    'codigo_disciplina': codigo_disciplina
            }
            
            turmas.append(nova_turma)
            salvar_arquivos(turmas, 'classes.json')
            print('Turma inclusa com sucesso!')
        incluir_mais_turmas = input('Deseja cadastrar uma nova turma?(s/n)')
        if incluir_mais_turmas == 'n':
            break

#Função para Incluir matrículas
def incluir_matricula():
    matriculas = ler_arquivo('licenseplates.json')
    while True:
        try:
            codigo_turma = int(input('Digite o código da turma:'))
        except ValueError:
            print('Digite um valor válido!')
            continue
        # Verifica se o código já está cadastrado
        for matricula in matriculas:
            if matricula['codigo_turma'] == codigo_turma:
                print('Matricula já cadastrada!')
                break
        else:
            codigo_estudante = int(input('Digite o código do estudante'))
            nova_matricula = {
                        'codigo_turma': codigo_turma,
                        'codigo_estudante': codigo_estudante
            }
            
            matriculas.append(nova_matricula)
            salvar_arquivos(matriculas, 'licenseplates.json')
            print('Matrícula inclusa com sucesso!')

        incluir_mais_matricula = input('Deseja cadastrar uma nova matrícula?(s/n)')
        if incluir_mais_matricula == 'n':
            break

#Função para Incluir estudantes
def incluir_estudantes():
    estudantes = ler_arquivo('student.json')
    while True:
        try:
            codigo = int(input('Digite o código do estudante: '))
        except ValueError:
            print('Digite um valor válido!')
            continue

        # Verifica se o código já está cadastrado
        for estudante in estudantes:
            if estudante['codigo'] == codigo:
                print('Estudante já cadastrado!')
                break
        else:
            nome = str(input('Digite o nome do estudante:'))
            cpf = str(input('Digite o CPF do estudante: '))
            novo_estudante = {
                'codigo': codigo,
                'nome': nome,
                'cpf': cpf
            }
            
            estudantes.append(novo_estudante)
            salvar_arquivos(estudantes, "student.json")
            print('Estudante incluído com sucesso!')
            

        mais_estudantes = input('Deseja cadastrar outro estudante? (s/n): ')
        if mais_estudantes == 'n':
            break
###############################################################################################################################################################################################        
                            
#BLOCO PARA MOSTRAR O MENU DE OPERAÇÕES SEMPRE QUE PRECISARMOS PARA INCLUIR, LISTAR, ATUALIZAR, EXCLUIR ALGUM ELEMENTO DA LISTA CORRESPONDENTE, OU VOLTAR PARA O MENU PRINCIPAL.
def menu_de_operacoes():
        print('(=== MENU DE OPERAÇÕES ===)')
        print('1. Incluir')
        print('2. Listar')
        print('3. Atualizar')
        print('4. Excluir')
        print('0. Voltar ao Menu Principal')
            
        
        return int(input('Selecione uma Opção:')) 
########################

#FUNÇÃO PARA LISTAR ELEMENTOS INCLUSOS NA LISTA(ESTUDANTES, DISCIPLINAS, PROFESSORES, TURMAS OU MATRÍCULAS.)
def listagem(nome_do_arquivo):
    lista = ler_arquivo(nome_do_arquivo)
    if not lista:
        print('Não à cadastro na lista!')
        return
    for elemento in lista:
        print(elemento)
#######################
           
# BLOCO DE FUNÇÕES DE ATUALIZAÇÃO DE DADOS
def atualizar_estudante():
    estudantes = ler_arquivo('student.json')
    atualizar_estu = int(input('Digite o código do estudante:'))
    for estudante in estudantes:
        if estudante['codigo'] == atualizar_estu:
            while True:
                try:
                    estudante['nome'] = str(input('Digite um novo nome:'))
                    estudante['cpf'] = str(input('Digite um novo cpf:'))
                except ValueError:
                    print('Digite um valor válido!')
                    continue
                salvar_arquivos(estudantes, 'student.json')
                print('Estudante atualizado com Sucesso!')
                continuar_atualizar_estudante = input('Deseja atualizar outro estudante? (s/n)')
                if continuar_atualizar_estudante == 'n':
                    break
                return
    else:
        print('Código de estudante não encontrado!')

def atualizar_professor():
    professores = ler_arquivo('teachers.json')
    atualizar_prof = int(input('Digite o código do professor que deseja atualizar seus dados:'))
    
    for professor in professores:
        if professor['codigo'] == atualizar_prof:
                while True:
                    try:
                        professor['nome'] = str(input('Digite o novo nome:'))
                        professor['cpf'] = str(input('Digite o cpf:'))
                    except ValueError:
                        print('Digite um valor válido!')
                        continue
                    salvar_arquivos(professores, 'teachers.json')
                    print('Professor atualizado com sucesso!')     
                    continuar_atualizar_professor = input('Deseja atualizar outro professor(a)? (s/n)')
                    if continuar_atualizar_professor == 'n':
                        break
                    return   
    else:
        print('Professor não encontrado no banco de dados!')

def atualizar_disciplinas():
    disciplinas = ler_arquivo('disciplines.json')
    atualizar_discip = int(input('Digite o código da disciplina que deseja atualizar:'))
    
    for disciplina in disciplinas:
        if disciplina['codigo'] == atualizar_discip:
            while True:
                try:
                    disciplina['nome'] = str(input('Digite o novo nome da disciplina'))
                except ValueError:
                    print('Digite um valor válido!')
                    continue
                salvar_arquivos(disciplinas, 'disciplines.json')
                print('Disciplina atualizada com sucesso!')
                continuar_atualizar = input('Deseja atualizar outra disiciplina? (s/n)')
                if continuar_atualizar == 'n':
                    break
                return
    else:
        print('Disciplina não encontrada em banco de dados')

def atualizar_turmas():
    turmas = ler_arquivo('classes.json')
    atualizar_tur = int(input('Digite o código da turma que deseja atualizar:'))

    for turma in turmas:
        if turma['codigo'] == atualizar_tur:
                    while True:
                        try:
                            turma['codigo_professor'] = int(input('Digite o novo código do professor:'))
                            turma['codigo_disciplina'] = int(input('Digite o novo código da disciplina:'))
                        except ValueError:
                            print('Digite um valor válido!')
                            continue

                        salvar_arquivos(turmas, 'classes.json')
                        print('Turma atualizada com sucesso!')
                        continuar_atualizar_turma = input('Deseja atualizar outr turma? (s/n)')
                        if continuar_atualizar_turma == 'n':
                            break
                        return   
    else:
        print('Turma não encontrada em banco de dados!')

def atualizar_matriculas():
    matriculas = ler_arquivo('licenseplates.json')
    atualizar_matri = int(input('Digite o código da matricula que deseja atualizar'))
   
    for matricula in matriculas:
        if matricula['codigo_turma'] == atualizar_matri:
            while True:
                try:
                    matricula['codigo_estudante'] = int(input('Digite o novo código do estudante'))
                except ValueError:
                    print('Digite um valor válido!')
                    continue
                salvar_arquivos(matriculas, 'licenseplates.json')
                print('Matricula atualizada com sucesso')
                continuar_atualizar_matricula = input('Deseja atualizar outra matricula? (s/n)')
                if continuar_atualizar_matricula == 'n':
                    break
                return   
    else:
        print('Matrícula não encontrada no banco de dados!')
###################################################################################################################################################################################################

#BLOCO DE FUNÇÃO - EXCLUIR
def excluir(lista, nome_do_arquivo):
        
        excluir_item = int(input(f'Digite o código do item que deseja remover '))
        for item in lista:
            if item['codigo'] == excluir_item:
                lista.remove(item)
                salvar_arquivos(lista, nome_do_arquivo)
                print('Item removido da lista com Sucesso!')
                break
             
            continuar_excluir = input('Deseja excluir cadastro?(s/n)')
            if continuar_excluir == 'n':
                break
        else:
            print('Código de estudante não encontrado!')
#########################                

def menu_de_operações_para_estudante():
    while True:
            try:
                opcao_estudantes = menu_de_operacoes()
            except ValueError:
                print('Digite um valor válido!')
                continue
    
            if opcao_estudantes == 1:
                print('Icluir Estudantes!')
                try:
                    incluir_estudantes()
                except ValueError:
                    print('Digite um valor válido!')
                    continue
                    
            elif opcao_estudantes == 2:
                estudantes = ler_arquivo('student.json')
                print('Lista de Estudantes!')
                listagem('student.json')
                
            
            elif opcao_estudantes == 3:
                print('Atualizar Estudantes!')
                atualizar_estudante()
            
            elif opcao_estudantes == 4:
                print('Excluir Estudantes!')
                excluir(estudantes, 'student.json')
            
            elif opcao_estudantes == 0:
                print('Voltando ao Menu Principal')
                break
            else:
                print('Valor inválido. Selecione um valor correspondente!')

def menu_de_operações_para_disciplinas():
    while True:
            try:
                opcao_disciplinas = menu_de_operacoes()        
            except ValueError:
                print('Digite um valor válido!')
                continue
            
            if opcao_disciplinas == 1:
                print('Icluir disciplinas!')
                try:
                    incluir_disciplinas()
                except ValueError:
                    print('Digite um valor válido!')
                    continue
                        
            elif opcao_disciplinas == 2:
                disciplinas = ler_arquivo('disciplines.json')
                print('Lista de disciplinas!')
                listagem('disciplines.json')
                
            
            elif opcao_disciplinas == 3:
                print('Atualizar disciplinas!')
                atualizar_disciplinas()
            
            elif opcao_disciplinas == 4:
                print('Excluir disciplinas!')
                excluir(disciplinas, 'disciplines.json')
                
            
            elif opcao_disciplinas == 0:
                 print('Voltando ao Menu Principal')
                 break
            else:
                print('Valor inválido. Selecione um valor correspondente!')

def menu_de_operações_para_professores():
    while True:
            try:
                opcao_de_professores = menu_de_operacoes()
            except ValueError:
                print('Digite um valor válido!')
                continue
            
            if opcao_de_professores == 1:
                print('Icluir professor!')
                try:
                    incluir_professores()
                except ValueError:
                    print('Digite um valor válido!')
                    continue
            
            elif opcao_de_professores == 2:
                print('Lista de professor!')
                listagem('teachers.json')       
            
            elif opcao_de_professores == 3:
                print('Atualizar professor!')
                atualizar_professor()
            
            elif opcao_de_professores == 4:
                excluir('professores', 'teachers.json')  
                print('Excluir professor!')
                   
            
            elif opcao_de_professores == 0:
                print('Voltando ao Menu Principal')
                break     
            else:
                print('Valor inválido. Selecione um valor correspondente!')

def menu_de_operações_para_turmas():
    while True:
            try:
                opcao_da_turma = menu_de_operacoes()
            except ValueError:
                print('Digite um valor válido!')
                continue
            
            if opcao_da_turma == 1:
                print('Icluir turmar!')
                try:
                    incluir_turmas()
                except ValueError:
                    print('Digite um valor válido!')
                    continue
            
            elif opcao_da_turma == 2:
                print('Lista de turmar!')
                listagem('classes.json')
            
            elif opcao_da_turma == 3:
                print('Atualizar turmar!')
                atualizar_turmas()
            
            elif opcao_da_turma == 4:
                print('Excluir turmar!')
                excluir('classes.json')
            
            elif opcao_da_turma == 0:
                print('Voltando ao Menu Principal')
                break
            else:
                print('Valor inválido. Selecione um valor correspondente!')

def menu_de_operações_para_matriculas():
    while True:
            try:
                opcao_da_matriculas = menu_de_operacoes()
            except ValueError:
                print('Digite um valor válido!')
                continue
            if opcao_da_matriculas == 1:
                print('Icluir matriculas!')
                try:
                    incluir_matricula()
                except ValueError:
                    print('Digite um valor válido!')
                    continue

            elif opcao_da_matriculas == 2:
                print('Lista de matriculas!')
                listagem('licenseplates.json')
            
            elif opcao_da_matriculas == 3:
                print('Atualizar matriculas!')
                atualizar_matriculas()
            
            elif opcao_da_matriculas == 4:
                print('Excluir matriculas!')
                excluir('licenseplates.json')
            
            elif opcao_da_matriculas == 0:
                print('Voltando ao Menu Principal')
                break
            else:
                print('Valor inválido. Selecione um valor correspondente!')


#COMEÇANDO O MENU PRINCIPAL
while True:
    try:
        opcao_do_menu_principal = menu_principal()
    except ValueError:
        print('Digite um valor válido!')
        continue
    if opcao_do_menu_principal == 0:
        print('ENCERRANDO NAVEGAÇÃO')
        break
    
    #ENTRANDO NA OPÇÃO PARA FUNÇÕES DOS ESTUDANTES, ABRINDO O MENU DE OPERAÇÕES.
    elif opcao_do_menu_principal == 1:
        print('Menu de Operações para Estudantes!')
        menu_de_operações_para_estudante()
    
    #ENTRANDO NA OPÇÃO PARA FUNÇÕES DAS DISCIPLINAS, ABRINDO O MENU DE OPERAÇÕES.
    elif opcao_do_menu_principal == 2:
        print('Menu de Operações para Disciplinas!')
        menu_de_operações_para_disciplinas()
        
    
    #ENTRANDO NA OPÇÃO PARA FUNÇÕES DE PROFESSORES, ABRINDO O MENU DE OPERAÇÕES.
    elif opcao_do_menu_principal == 3:
        print('Menu de Operações para professores!')
        menu_de_operações_para_professores()

    #ENTRANDO NA OPÇÃO PARA FUNÇÕES DE TURMA, ABRINDO O MENU DE OPERAÇÕES.
    elif opcao_do_menu_principal == 4:
        print('Menu de Operações para Turmas')
        menu_de_operações_para_turmas()
        
                
    #ENTRANDO NA OPÇÃO PARA FUNÇÕES DA MATRICULA, ABRINDO O MENU DE OPERAÇÕES.
    elif opcao_do_menu_principal == 5:
        print('Menu de Operações para Matrículas!')
        menu_de_operações_para_matriculas()
                


    



        



    

        





















    
        