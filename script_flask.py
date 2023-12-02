from flask import Flask, render_template, request
app = Flask(__name__)

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

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/result', methods=['POST'])
def result():
    input_nome = request.form.get('input_nome')
    input_numero = request.form.get('input_numero')

    try:
        input_numero = int(input_numero)
    except ValueError:
        return "O segundo argumento precisa ser um número inteiro."

    count = 0
    for inseto in insetos_cana_de_acucar:
        if input_nome == inseto['Nome Científico']:
            count += 1
        if count > 0:
            pass
    if count == 0:
        return "O inseto não está na lista."

    for inseto in insetos_cana_de_acucar:
        if input_nome == inseto['Nome Científico']:
            count += 1
            if inseto['É Praga?']:
                if input_numero >= inseto['DE']:
                    resultado = {
                        "mensagem": "O número de indivíduos atingiu o nível de dano econômico",
                        "controle_biologico": inseto['Controle Biológico'],
                        "controle_cultural": inseto['Controle Cultural'],
                        "link": inseto['Link']
                    }
                elif inseto['C'] <= input_numero < inseto['DE']:
                    resultado = {
                        "mensagem": "O número de indivíduos atingiu o nível de controle",
                        "controle_biologico": inseto['Controle Biológico'],
                        "controle_cultural": inseto['Controle Cultural'],
                        "link": inseto['Link']
                    }
                elif input_numero < inseto['C']:
                    resultado = {
                        "mensagem": "O número de indivíduos está abaixo do nível de controle",
                        "nivel_controle": inseto['C'],
                        "beneficios": inseto['Benefícios']
                    }
            else:
                resultado = {
                    "mensagem": "Este inseto não é uma praga",
                    "beneficios": inseto['Benefícios']
                }

    return render_template('result.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
