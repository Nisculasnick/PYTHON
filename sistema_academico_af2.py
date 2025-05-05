import json
arquivo_estudantes="estudantes.json"
arquivo_professores="professores.json"
arquivo_disciplinas="disciplinas.json"
arquivo_turmas="turmas.json"
arquivo_matriculas="matriculas.json"
#funções para menu -----------------------------------------
def menu_principal():
        print('''
        [1] Gerenciar estudantes
        [2] Gerenciar professores
        [3] Gerenciar disciplinas
        [4] Gerenciar turmas
        [5] Gerenciar matrículas
        [9] Sair
        ''')
        return int(input('Informe a opção desejada: '))

def menu_secundário(tipo):
        print(f'***** {tipo}: MENU DE OPERAÇÕES *****')
        print(''' 
        [1] Incluir
        [2] Listar
        [3] Atualizar
        [4] Excluir
        [9] Voltar ao Menu Principal\n''')

        return int(input('Informe a opção desejada: '))

#funções para estudantes ----------------------------------
def incluir_estudantes(lista_estudantes):
    lista_estudantes = ler_arquivo(arquivo_estudantes)
    while True:
        try:
            code = int(input('Digite o código: '))
            codigo_existe = False
            for estudante in lista_estudantes:
                if estudante['código'] == code:
                    codigo_existe = True
                    break
            if codigo_existe:
                print('Este código já está sendo usado. Por favor, digite outro código.')
            else:
                break
        except ValueError:
            print('Por favor, digite um código numérico válido.')

    nome = str(input('Digite o nome: ')).strip().title()
    cpf = str(input('Digite o CPF: '))

    if nome and cpf:
        dados_estudantes = {"código": code, "nome": nome, "CPF": cpf}
        lista_estudantes.append(dados_estudantes)
        salvar_arquivo(lista_estudantes, arquivo_estudantes)
        print('-=' * 20)
        print(f'{nome} foi adicionado(a) com sucesso!')
        print('-=' * 20)
    else:
        print("Não foi possível adicionar!")

def listar_estudantes(lista_estudantes):
        lista_estudantes=ler_arquivo(arquivo_estudantes)
        if lista_estudantes:
            print('\nLista de Estudantes:')
            for estudante in lista_estudantes:
                   print(f"\n Código: {estudante['código']}", f"Nome: {estudante['nome']}", f"CPF: {estudante['CPF']}\n")
        else:
                print('\n Lista vazia, nenhum estudante encontrado\n')
        input('Pressione ENTER para continuar')

def atualizar_estudantes(lista_estudantes):
        lista_estudantes=ler_arquivo(arquivo_estudantes)
        codigo_para_editar = int(input('\nQual o código do estudante que deseja editar? '))
        estudante_encontrado = None

        for estudante in lista_estudantes:
                if estudante['código'] == codigo_para_editar:
                        estudante_encontrado = estudante
                        break

        if estudante_encontrado is None:
                print(f'\nEstudante com código {codigo_para_editar} não encontrado\n')
        
        else:
                estudante_encontrado['código'] = int(input('Digite novo código: '))
                estudante_encontrado['nome'] = str(input('Digite novo nome: ')).strip().title()
                estudante_encontrado['CPF'] = str(input('Digite novo CPF: '))
                print('\nEstudante atualizado com sucesso!\n')
                salvar_arquivo(lista_estudantes, arquivo_estudantes)

def excluir_estudantes(lista_estudantes):
        lista_estudantes=ler_arquivo(arquivo_estudantes)
        código_para_excluir=int(input('Qual o código?: '))
        estudande_para_ser_removido=None
        for dicionario_estudante in lista_estudantes:
                if dicionario_estudante['código']==código_para_excluir:
                        estudande_para_ser_removido=dicionario_estudante
                        break
        if estudande_para_ser_removido is None:
                print(f'Estudante com o código {código_para_excluir} não encontrado!')
        else:
                lista_estudantes.remove(estudande_para_ser_removido)
                print('\nEstudante removido com sucesso!\n')
                salvar_arquivo(lista_estudantes, arquivo_estudantes)

#funções para professores ---------------------------------
def incluir_professores(lista_professores):
        lista_professores=ler_arquivo(arquivo_professores)
        code=int(input('Digite o código: '))
        nome=str(input('Digite o nome: ')).strip().title()
        cpf=str(input('Digite o CPF: '))
        if nome and cpf:
                dados_professores={"código":code,"nome":nome,"CPF":cpf}
                lista_professores.append(dados_professores)
                salvar_arquivo(lista_professores, arquivo_professores)
                print('-='*20)
                print(f'{nome} foi adiconado(a) com sucesso!')
                print('-='*20)
        else:
                print("Não foi possível adicionar!")

def listar_professores(lista_professores):
        lista_professores=ler_arquivo(arquivo_professores)
        if lista_professores:
                print('\nLista de Professores')
                for professor in lista_professores:
                        print(f'\nCódigo: {professor['código']}', f'Nome: {professor['nome']}', f'CPF: {professor['CPF']}\n')
        else:
                print('\n Lista vazia, nenhum professor encontrado\n')
        input('Pressione ENTER para continuar')

def atualizar_professores(lista_professores):
        lista_professores=ler_arquivo(arquivo_professores)
        codigo_para_editar = int(input('\nQual o código do professor que deseja editar? '))
        professor_encontrado = None

        for professor in lista_professores:
                if professor['código'] == codigo_para_editar:
                        professor_encontrado = professor
                        break

        if professor_encontrado is None:
                print(f'\nProfessor com código {codigo_para_editar} não encontrado\n')
        else:
                professor_encontrado['código'] = int(input('Digite novo código: '))
                professor_encontrado['nome'] = str(input('Digite novo nome: ')).strip().title()
                professor_encontrado['CPF'] = str(input('Digite novo CPF: '))
                print('\nProfessor atualizado com sucesso!\n')
                salvar_arquivo(lista_professores, arquivo_professores)

def excluir_professores(lista_professores):
        lista_professores=ler_arquivo(arquivo_professores)
        código_para_excluir=int(input('Qual o código?: '))
        professor_para_ser_removido=None
        for dicionario_professores in lista_professores:
                if dicionario_professores['código']==código_para_excluir:
                        professor_para_ser_removido=dicionario_professores
                        break
        if professor_para_ser_removido is None:
                print(f'Professor com o código {código_para_excluir} não encontrado!')
        else:
                lista_professores.remove(professor_para_ser_removido)
                print('\nProfessor removido com sucesso!\n')
                salvar_arquivo(lista_professores, arquivo_professores)

#funções para disciplinas ---------------------------------
def incluir_disciplinas(lista_disciplinas):
        lista_disciplinas=ler_arquivo(arquivo_disciplinas)
        code=int(input('Digite o código: '))
        nome=str(input('Digite o nome: ')).strip().title()
        if nome and code:
                dados_disciplina={"código":code,"nome":nome}
                lista_disciplinas.append(dados_disciplina)
                salvar_arquivo(lista_disciplinas, arquivo_disciplinas)
                print('-='*20)
                print(f'{nome} foi adiconado(a) com sucesso!')
                print('-='*20)
        else:
                print("Não foi possível adicionar!")

def listar_disciplinas(lista_disciplinas):
        lista_disciplinas=ler_arquivo(arquivo_disciplinas)
        if lista_disciplinas:
            print('\nLista de Disciplinas:')
            for disciplina in lista_disciplinas:
                   print(f"\n Código: {disciplina['código']}", f"Nome: {disciplina['nome']}\n")
        else:
                print('\n Lista vazia, nenhuma disciplina encontrada\n')
        input('Pressione ENTER para continuar')

def atualizar_diciplinas(lista_disciplinas):
        lista_disciplinas=ler_arquivo(arquivo_disciplinas)
        codigo_para_editar = int(input('\nQual o código da disciplinas que deseja editar? '))
        disciplina_encontrada = None

        for disciplina in lista_disciplinas:
                if disciplina['código'] == codigo_para_editar:
                        disciplina_encontrada = disciplina
                        break

        if disciplina_encontrada is None:
                print(f'\nDisciplina com código {codigo_para_editar} não encontrada\n')
        else:
                disciplina_encontrada['código'] = int(input('Digite novo código: '))
                disciplina_encontrada['nome'] = str(input('Digite novo nome: ')).strip().title()
                print('\nDisciplina atualizada com sucesso!\n')
                salvar_arquivo(lista_disciplinas, arquivo_disciplinas)

def excluir_disciplinas(lista_disciplinas):
        lista_disciplinas=ler_arquivo(arquivo_disciplinas)
        código_para_excluir=int(input('\nQual o código?: \n'))
        disciplina_para_ser_removido=None
        for dicionario_disciplina in lista_disciplinas:
                if dicionario_disciplina['código']==código_para_excluir:
                        disciplina_para_ser_removido=dicionario_disciplina
                        break
        if disciplina_para_ser_removido is None:
                print(f'\nDisciplina com o código {código_para_excluir} não encontrada!\n')
        else:
                lista_disciplinas.remove(disciplina_para_ser_removido)
                print('\nDisciplina removida com sucesso!\n')
                salvar_arquivo(lista_disciplinas, arquivo_disciplinas)

#funções para turmas --------------------------------------

def incluir_turmas(lista_turmas, lista_professores, lista_disciplinas):
        lista_turmas=ler_arquivo(arquivo_turmas)
        lista_disciplinas=ler_arquivo(arquivo_disciplinas)
        lista_professores=ler_arquivo(arquivo_professores)
        code_turma=int(input('Digite o código da turma: '))
        code_professores=int(input('Digite o código do professor: '))
        code_disciplina=int(input('Digite o código da disciplina: '))
        professor_encontrado=False
        for professor in lista_professores:
               if professor["código"]==code_professores:
                professor_encontrado=True
                break
        disciplina_encontrada=False
        for disciplina in lista_disciplinas:
               if disciplina["código"]==code_disciplina:
                        disciplina_encontrada=True
                        break
        if professor_encontrado and disciplina_encontrada:
               nova_turma={'código': code_turma, 'professor': code_professores, 'disciplina': code_disciplina}
               lista_turmas.append(nova_turma)
               salvar_arquivo(lista_turmas, arquivo_turmas)
               print('\nTurma cadastrada com sucesso!\n')
        else:
                if not professor_encontrado:
                       print(f'Professor com o código {code_professores} não encontrado!')
                if not disciplina_encontrada:
                       print(f'Código da turma {code_disciplina} não encontrado!')

def listar_turmas(lista_turmas):
        lista_turmas=ler_arquivo(arquivo_turmas)
        if lista_turmas:
            print('\nLista de Turmas:\n')
            for turma in lista_turmas:
                print(f'Código da turma: {turma['código']}')
                print(f'Código do professor: {turma['professor']}')
                print(f'Código da disciplina: {turma['disciplina']}')
        else:
                print('\n Lista vazia, nenhuma disciplina encontrada\n')
        input('\nPressione ENTER para continuar\n')

def atualizar_turmas(lista_turmas):
        lista_turmas=ler_arquivo(arquivo_turmas)
        código_para_editar=int(input('\nQual o código da Turma que deseja editar? '))
        turma_encontrada=None
        for turma in lista_turmas:
              if turma['código']==código_para_editar:
                     turma_encontrada=turma
                     break
        if turma_encontrada is None:
              print(f'\nTurma com código {código_para_editar} não encontrada\n')
        else:
              turma_encontrada['código']=int(input('Digite novo código (turma): '))
              turma_encontrada['professor']=int(input('Digite novo código (professor): '))
              turma_encontrada['disciplna']=int(input('Digite novo código (disciplina): '))
              salvar_arquivo(lista_turmas, arquivo_turmas)

def excluir_turmas(lista_turmas):
        lista_turmas=ler_arquivo(arquivo_turmas)
        código_para_excluir=int(input('Qual o código? '))
        turma_para_ser_removida=None
        for dicionario_turmas in lista_turmas:
               if dicionario_turmas['código']==código_para_excluir:
                      turma_para_ser_removida=dicionario_turmas
                      break
        if turma_para_ser_removida is None:
               print(f'\nTurma com o código {código_para_excluir} não encontrada\n')
        else:
               lista_turmas.remove(turma_para_ser_removida)
               print('\nTurma removida com sucesso!\n')
               salvar_arquivo(lista_turmas)

#funções para matrículas ----------------------------------

def incluir_matriculas(lista_matriculas, lista_estudantes, lista_turmas):
    lista_matriculas=ler_arquivo(arquivo_matriculas)
    lista_estudantes=ler_arquivo(lista_estudantes)
    lista_turmas=ler_arquivo(arquivo_turmas)
    code_turma = int(input('Digite o código da turma para a matrícula: '))
    code_aluno = int(input('Digite o código do estudante para a matrícula: '))
    turma_encontrada = None
    for turma in lista_turmas:
        if turma['código'] == code_turma:
            turma_encontrada = turma
            break
    aluno_encontrado = None
    for aluno in lista_estudantes:
        if aluno['código'] == code_aluno:
            aluno_encontrado = aluno
            break
    if aluno_encontrado and turma_encontrada:
        matricula_existente = False
        for matricula in lista_matriculas:
            if matricula['turma'] == code_turma and matricula['estudante'] == code_aluno:
                matricula_existente = True
                break
        if matricula_existente:
            print('\nEste estudante já está matriculado nesta turma!\n')
        else:
            nova_matricula = {'turma': code_turma, 'estudante': code_aluno}
            lista_matriculas.append(nova_matricula)
            salvar_arquivo(lista_matriculas, "matriculas.json") 
            print('\nMatrícula realizada com sucesso!\n')
    else:
        if not turma_encontrada:
            print(f'\nTurma com o código {code_turma} não encontrada!\n')
        if not aluno_encontrado:
            print(f'\nEstudante com o código {code_aluno} não encontrado!\n') 

def listar_matriculas(lista_matriculas, lista_estudantes, lista_turmas):
        lista_matriculas=ler_arquivo(arquivo_matriculas)
        lista_estudantes=ler_arquivo(lista_estudantes)
        lista_turmas=ler_arquivo(arquivo_turmas)
        if lista_matriculas:
                print('\nLista de Matrículas:')
        for matricula in lista_matriculas:
                codigo_turma = matricula['turma']
                codigo_estudante = matricula['estudante']

                nome_turma = "Turma não encontrada"
                for turma in lista_turmas:
                        if turma['código'] == codigo_turma:
                                nome_turma = turma['código'] 
                                break

                nome_estudante = "Estudante não encontrado"
                for estudante in lista_estudantes:
                        if estudante['código'] == codigo_estudante:
                                nome_estudante = estudante['nome']
                                break

                print(f"  Turma: {codigo_turma} (Código), Estudante: {codigo_estudante} ({nome_estudante})")
        else:
                print('\nNão há matrículas cadastradas.\n')

        input('Pressione ENTER para continuar')

def atualizar_matriculas(lista_matriculas, lista_estudantes, lista_turmas):
    lista_estudantes=ler_arquivo(arquivo_estudantes)
    lista_turmas=ler_arquivo(arquivo_turmas)
    codigo_turma_antigo = int(input('Digite o código da turma da matrícula que deseja atualizar: '))
    codigo_aluno_antigo = int(input('Digite o código do estudante da matrícula que deseja atualizar: '))
    matricula_encontrada = None
    for matricula in lista_matriculas:
        if matricula['turma'] == codigo_turma_antigo and matricula['estudante'] == codigo_aluno_antigo:
            matricula_encontrada = matricula
            break
    if matricula_encontrada:
        print('\nMatrícula encontrada. O que deseja atualizar?')
        print('[1] Turma')
        print('[2] Estudante')
        opcao = int(input('Informe a opção: '))
        if opcao == 1:
            novo_codigo_turma = int(input('Digite o novo código da turma: '))
            turma_existe = any(turma['código'] == novo_codigo_turma for turma in lista_turmas)
            if turma_existe:
                matricula_encontrada['turma'] = novo_codigo_turma
                salvar_arquivo(lista_matriculas, "matriculas.json")
                print('\nTurma da matrícula atualizada com sucesso!\n')
            else:
                print(f'\nTurma com código {novo_codigo_turma} não encontrada.\n')
        elif opcao == 2:
            novo_codigo_aluno = int(input('Digite o novo código do estudante: '))
            aluno_existe = any(aluno['código'] == novo_codigo_aluno for aluno in lista_estudantes)
            if aluno_existe:
                matricula_encontrada['estudante'] = novo_codigo_aluno
                salvar_arquivo(lista_matriculas, "matriculas.json")
                print('\nEstudante da matrícula atualizado com sucesso!\n')
            else:
                print(f'\nEstudante com código {novo_codigo_aluno} não encontrado.\n')
        else:
            print('\nOpção inválida.\n')
    else:
        print('\nMatrícula não encontrada.\n')      

def excluir_turmas(lista_turmas, lista_matriculas):
    lista_turmas=ler_arquivo(lista_turmas)
    lista_matriculas=ler_arquivo(arquivo_matriculas)
    codigo_para_excluir = int(input('Digite o código da turma que deseja excluir: '))
    turma_encontrada = None
    indice_turma_remover = -1

    for indice, turma in enumerate(lista_turmas):
        if turma['código'] == codigo_para_excluir:
            turma_encontrada = turma
            indice_turma_remover = indice
            break

    if turma_encontrada:
        matriculas_para_remover = [
            matricula for matricula in lista_matriculas if matricula['turma'] == codigo_para_excluir
        ]
        for matricula in matriculas_para_remover:
            lista_matriculas.remove(matricula)

        del lista_turmas[indice_turma_remover]
        salvar_arquivo(lista_turmas, "turmas.json")
        salvar_arquivo(lista_matriculas, "matriculas.json")
        print(f'\nTurma com código {codigo_para_excluir} e suas matrículas associadas foram excluídas com sucesso!\n')
    else:
        print(f'\nTurma com código {codigo_para_excluir} não encontrada.\n')
       
# funções para arquivos em json----------------------------            
def salvar_arquivo(lista, nome_arquivo):
    with open(nome_arquivo, "w", encoding='utf-8') as arquivo:
        json.dump(lista, arquivo, ensure_ascii=False, indent=4)

def ler_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, "r", encoding='utf-8') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []
#Programa Principal----------------------------------------
lista_estudantes=ler_arquivo(arquivo_estudantes)
lista_professores=ler_arquivo(arquivo_professores)
lista_disciplinas=ler_arquivo(arquivo_disciplinas)
lista_turmas=ler_arquivo(arquivo_turmas)
lista_matriculas=ler_arquivo(arquivo_matriculas)
while True:
        option=menu_principal()
        if option==9:
                print('\n Finalizando o sistema...')
                break
        elif option==1:
                while True:
                        action = menu_secundário('Estudantes')
                        if action==9:
                                print('\n Voltando ao MENU PRINCIPAL')
                                break
                        elif action==1:
                                incluir_estudantes(lista_estudantes)
                        elif action==2:
                                listar_estudantes(lista_estudantes)
                        elif action == 3:
                               atualizar_estudantes(lista_estudantes)
                        elif action ==4:
                               excluir_estudantes(lista_estudantes)
                        else:
                               print('Opção INVÁLIDA')
        elif option==2:
               while True: 
                        action= menu_secundário('Professores')
                        if action==9:
                              print('\nVoltando ao MENU PRINCIPAL')
                              break
                        elif action == 1:
                                incluir_professores(lista_professores)
                        elif action == 2:
                                listar_professores(lista_professores)
                        elif action == 3:
                                atualizar_professores(lista_professores)
                        elif action == 4:
                                excluir_professores(lista_professores)
                        else:
                                print('Opção INVÁLIDA')    
        elif option == 3:
                while True:
                        action= menu_secundário('Disciplinas')
                        if action==9:
                                print('Voltando ao MENU PRINCIPAL')
                                break 
                        elif action == 1:
                                incluir_disciplinas(lista_disciplinas)
                        elif action == 2:
                                listar_disciplinas(lista_disciplinas)
                        elif action == 3:
                                atualizar_diciplinas(lista_disciplinas)
                        elif action == 4:
                                excluir_disciplinas(lista_disciplinas)
                        else:
                                print('Opção INVÁLIDA')
        elif option == 4:
                while True:
                        action=menu_secundário('Turmas') 
                        if action == 9:
                                print('Voltando ao MENU PRINCIPAL')
                                break 
                        if action == 1:
                               incluir_turmas(lista_turmas, lista_professores, lista_disciplinas)
                        if action == 2:
                               listar_turmas(lista_turmas)
                        if action == 3:
                               atualizar_turmas(lista_turmas)
                        if action == 4:
                               excluir_turmas(lista_turmas)
                        else:
                                print('Opção INVÁLIDA')         
        elif option == 5:
               while True:
                        action=menu_secundário('Matrículas') 
                        if action == 9:
                                print('Voltando ao MENU PRINCIPAL')
                                break 
                        elif action == 1:
                                incluir_matriculas(lista_matriculas, lista_estudantes, lista_turmas)
                        elif action == 2:
                                listar_matriculas(lista_matriculas, lista_estudantes, lista_turmas)
                        elif action == 3:
                                atualizar_matriculas(lista_matriculas, lista_estudantes, lista_turmas)
                        elif action == 4:
                                excluir_turmas(lista_turmas, lista_matriculas)
                        else:
                               print('opção INVÁLIDA')


        else:
               print('EM DESENVOLVIMENTO')
