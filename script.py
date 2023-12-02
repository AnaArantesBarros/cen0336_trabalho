import sys
input_nome = sys.argv[1]
input_numero = sys.argv[2]

insetos_cana_de_acucar = [
    {
        'Nome Científico': 'Diatraea saccharalis',
        'Nome Comum': 'Broca da cana',
        'É Praga?': True,
        'C': 3,
        'DE': 6,
        'Controle Biológico': 'Parasitoides Cotesia flavipes e Trichogramma galoi',
        'Controle Cultural': 'Rotação de culturas e manejo de restos culturais',
        'Benefícios': '',
        'Link': 'https://agrofit.agricultura.gov.br/agrofit_cons/!ap_praga_detalhe_cons?p_id_cultura_praga=2806'
    },
    {
        'Nome Científico': 'Sphenophorus levis',
        'Nome Comum': 'Bicudo',
        'É Praga?': True,
        'C': 15,
        'DE': 35,
        'Controle Biológico': 'Fungo Beauveria bassiana e Nematoides entomopatogênicos',
        'Controle Cultural': 'Controle de plantas daninhas e Rotação de culturas',
        'Benefícios': '',
        'Link': 'https://agrofit.agricultura.gov.br/agrofit_cons/!ap_praga_detalhe_cons?p_id_cultura_praga=5203'
    },
    {
        'Nome Científico': 'Heterotermes tenuis',
        'Nome Comum': 'Cupim Heterotermes',
        'É Praga?': True,
        'C': 25,
        'DE': 35,
        'Controle Biológico': 'Nematoides entomopatogênicos e Preservação de inimigos naturais',
        'Controle Cultural': 'Destruição de soqueiras',
        'Benefícios': '',
        'Link': 'https://agrofit.agricultura.gov.br/agrofit_cons/!ap_praga_detalhe_cons?p_id_cultura_praga=2815'
    },
    {
        'Nome Científico': 'Procornitermes triacifer',
        'Nome Comum': 'Cupim Proconitermes',
        'É Praga?': True,
        'C': 27,
        'DE': 37,
        'Controle Biológico': 'Nematoides entomopatogênicos e Preservação de inimigos naturais',
        'Controle Cultural': 'Destruição de soqueiras',
        'Benefícios': '',
        'Link': 'https://agrofit.agricultura.gov.br/agrofit_cons/!ap_praga_detalhe_cons?p_id_cultura_praga=2826'
    },
    {
        'Nome Científico': 'Mahanarva fimbriolata',
        'Nome Comum': 'Cigarrinha',
        'É Praga?': True,
        'C': 10,
        'DE': 17,
        'Controle Biológico': 'Fungo Metharizium anisopliae',
        'Controle Cultural': 'Quebra-vento e Manejo da Palhada',
        'Benefícios': '',
        'Link': 'https://agrofit.agricultura.gov.br/agrofit_cons/!ap_praga_detalhe_cons?p_id_cultura_praga=2816'
    },
    {
        'Nome Científico': 'Mahanarva posticata',
        'Nome Comum': 'Cigarrinha',
        'É Praga?': True,
        'C': 12,
        'DE': 20,
        'Controle Biológico': 'Fungo Metharizium anisopliae',
        'Controle Cultural': 'Quebra-vento e Manejo da palhada',
        'Benefícios': '',
        'Link': 'https://agrofit.agricultura.gov.br/agrofit_cons/!ap_praga_detalhe_cons?p_id_cultura_praga=2817'
    },
    {
        'Nome Científico': 'Migdolus fryanus',
        'Nome Comum': 'Migdolus',
        'É Praga?': True,
        'C': 20,
        'DE': 30,
        'Controle Biológico': 'Parasitoides e Fungos entomopatogênicos',
        'Controle Cultural': 'Época de plantio e Manejo da palhada',
        'Benefícios': '',
        'Link': 'https://agrofit.agricultura.gov.br/agrofit_cons/!ap_praga_detalhe_cons?p_id_cultura_praga=2818'
    },
    {
        'Nome Científico': 'Cotesia flavipes',
        'Nome Comum': 'Cotesia flavipes',
        'É Praga?': False,
        'C': 0,
        'DE': 0,
        'Controle Biológico': '',
        'Controle Cultural': '',
        'Benefícios': 'Contribui para o controle biológico de pragas na cana de açúcar',
        'Link': ''
    },
    {
        'Nome Científico': 'Trichogramma galoi',
        'Nome Comum': 'Trichogramma galoi',
        'É Praga?': False,
        'C': 0,
        'DE': 0,
        'Controle Biológico': '',
        'Controle Cultural': '',
        'Benefícios': 'Contribui para o controle biológico de pragas na cana de açúcar',
        'Link': ''
    },
    {
        'Nome Científico': 'Tesourinha',
        'Nome Comum': 'Tesourinha',
        'É Praga?': False,
        'C': 0,
        'DE': 0,
        'Controle Biológico': '',
        'Controle Cultural': '',
        'Benefícios': 'Atua como predador, contribuindo para o controle de insetos indesejados',
        'Link': ''
    },
    {
        'Nome Científico': 'Crisopídeo',
        'Nome Comum': 'Crisopídeo',
        'É Praga?': False,
        'C': 0,
        'DE': 0,
        'Controle Biológico': '',
        'Controle Cultural': '',
        'Benefícios': 'Atua como predador, contribuindo para o controle de insetos indesejados',
        'Link': ''
    },
    {
        'Nome Científico': 'Joaninha',
        'Nome Comum': 'Joaninha',
        'É Praga?': False,
        'C': 0,
        'DE': 0,
        'Controle Biológico': '',
        'Controle Cultural': '',
        'Benefícios': 'Atua como predador, contribuindo para o controle de insetos indesejados como pulgões.',
        'Link': ''
    },
]


if not isinstance(input_nome,str):
    print("O primeiro argumento precisa ser uma string.")
    sys.exit(1)

try:
    if isinstance(int(input_numero),int):
        input_numero = int(input_numero)
except:
    print("O segundo argumento precisa ser um número inteiro.")
    sys.exit(1)

count = 0
for inseto in insetos_cana_de_acucar:
    if input_nome == inseto['Nome Científico']:
        count += 1
    if count >0:
        pass
if count == 0:
    print("O inseto não está na lista.")
    sys.exit(1)


for inseto in insetos_cana_de_acucar:
    if input_nome == inseto['Nome Científico']:
        count += 1
        if inseto['É Praga?']:
            if input_numero >= inseto['DE']:
                print("O número de indivíduos atingiu o nível de dano econômico")
                print("As opções de controle para essa praga são:")
                print("Controle Biológico:", inseto['Controle Biológico'])
                print("Controle Cultural:", inseto['Controle Cultural'])
                print(f"Mais informações e recomendações de controle químico: {inseto['Link']}")

            elif inseto['C'] <= input_numero < inseto['DE']:
                print("O número de indivíduos atingiu o nível de controle.")
                print("As opções de controle para essa praga são:")
                print("Controle Biológico:", inseto['Controle Biológico'])
                print("Controle Cultural:", inseto['Controle Cultural'])
                print(f"Mais informações e recomendações de controle químico: {inseto['Link']}")
            elif input_numero < inseto['C']:
                print("O número de indivíduos está abaixo do nível de controle.")
                print(f"Para esse inseto o nível de controle é de {inseto['C']}% de touceiras infestadas")
        else:
            print("Este inseto não é uma praga. ")
            print(inseto["Benefícios"])
