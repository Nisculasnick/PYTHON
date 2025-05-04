import json
arquivo_estudantes="estudantes.json"
arquivo_professores="professores.json"
arquivo_disciplinas="disciplinas.json"
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
        código_para_excluir=int(input('Qual o código?: '))
        disciplina_para_ser_removido=None
        for dicionario_disciplina in lista_disciplinas:
                if dicionario_disciplina['código']==código_para_excluir:
                        disciplina_para_ser_removido=dicionario_disciplina
                        break
        if disciplina_para_ser_removido is None:
                print(f'Disciplina com o código {código_para_excluir} não encontrada!')
        else:
                lista_disciplinas.remove(disciplina_para_ser_removido)
                print('\nDisciplina removida com sucesso!\n')
                salvar_arquivo(lista_disciplinas, arquivo_disciplinas)
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
        else:
               print('EM DESENVOLVIMENTO')