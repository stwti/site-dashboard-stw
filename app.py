# app.py
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'chave-secreta-supersegura'  # Troque por algo mais forte em produção

# Usuários fixos (simples, sem banco de dados)
usuarios = {
    'Douglas': {
        'senha': 'senha123',
        'dashboards': [
            {'nome': 'Campanha Loreal - Rebouças',
             'slug': 'campanha_loreal_rb',
             'icone': 'dashboard1.png',
             'embed': 'https://app.powerbi.com/view?r=eyJrIjoiNTg2N2JhNmItZjBhMy00MGQwLThkZmYtNmI3MmU0Zjg1ZDExIiwidCI6ImQ2MzMwOTY2LWY4NWItNGY0MS04NTFkLWE4OGZjOTNlOGM4YiJ9'
            },
            
            {'nome': 'Campanha Loreal - Rede',
             'slug': 'campanha_loreal_rede',
             'icone': 'dashboard2.png',
             'embed': 'https://app.powerbi.com/view?r=eyJrIjoiZGRkYzY5ZDItNjBmOS00OGZmLWJlZTItYjI0MTk4YmY4MjRjIiwidCI6ImQ2MzMwOTY2LWY4NWItNGY0MS04NTFkLWE4OGZjOTNlOGM4YiJ9'
            },

            {'nome': 'Campanha Wella - Assistentes',
             'slug': 'campanha_wella_assistentes',
             'icone': 'dashboard3.png',
             'embed': 'https://app.powerbi.com/view?r=eyJrIjoiNDhhYjUxYzctYWMzZS00NTJlLThmZjAtOTIzODkxY2VmNjQ5IiwidCI6ImQ2MzMwOTY2LWY4NWItNGY0MS04NTFkLWE4OGZjOTNlOGM4YiJ9'
            },

            {'nome': 'Campanha Wella - Rede',
             'slug': 'campanha_wella_rede',
             'icone': 'dashboard4.png',
             'embed': 'https://app.powerbi.com/view?r=eyJrIjoiYmZlNzIxYTgtYWYwMy00YzhmLWEyZWEtODYzMTM3N2Q2ZjVjIiwidCI6ImQ2MzMwOTY2LWY4NWItNGY0MS04NTFkLWE4OGZjOTNlOGM4YiJ9'
            }
        ]
    },
    'bmedeiros': {
        'senha': 'minhasenha',
        'dashboards': [
            {'nome': 'Vendas - Julho',
             'slug': 'Vendas_Julho',
             'icone': 'dashboard3.png',
             'embed': 'https://app.powerbi.com/view?r=eyJrIjoiM2VkMjU5NTYtOTk0NC00MTlmLTlmN2UtOWRhM2I5ZTM0N2JmIiwidCI6ImQ2MzMwOTY2LWY4NWItNGY0MS04NTFkLWE4OGZjOTNlOGM4YiJ9'
            },
            {'nome': 'Vendas - Agosto',
             'slug': 'Vendas_Agosto',
             'icone': 'dashboard3.png',
             'embed': 'https://app.powerbi.com/view?r=eyJrIjoiYmZlNzIxYTgtYWYwMy00YzhmLWEyZWEtODYzMTM3N2Q2ZjVjIiwidCI6ImQ2MzMwOTY2LWY4NWItNGY0MS04NTFkLWE4OGZjOTNlOGM4YiJ9'
            }
        ]
    }
}

@app.route('/')
def home():
    if 'usuario' in session:
        return redirect(url_for('painel'))
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['usuario']
        senha = request.form['senha']
        if usuario in usuarios and usuarios[usuario]['senha'] == senha:
            session['usuario'] = usuario
            return redirect(url_for('painel'))
        return render_template('login.html', erro='Usuário ou senha inválidos.')
    return render_template('login.html')

@app.route('/painel')
def painel():
    if 'usuario' not in session:
        return redirect(url_for('home'))
    
    usuario = session['usuario']
    dashboards = usuarios[usuario]['dashboards']
    return render_template('painel.html', usuario=usuario, dashboards=dashboards)

@app.route('/dashboard/<slug>')
def dashboard(slug):
    if 'usuario' not in session:
        return redirect(url_for('home'))

    usuario = session['usuario']
    dashboards = usuarios[usuario]['dashboards']

    for dash in dashboards:
        if dash.get('slug') == slug:
            return render_template('dashboard.html', nome=dash['nome'], embed_link=dash['embed'])

    return "Acesso negado", 403


@app.route('/embed/<slug>')
def embed(slug):
    if 'usuario' not in session:
        return "Não autorizado", 401

    usuario = session['usuario']
    dashboards = usuarios[usuario]['dashboards']

    for dash in dashboards:
        if dash.get('slug') == slug:
            return redirect(dash['embed'])

    return "Dashboard não encontrado", 404


@app.route('/logout')
def logout():
    session.pop('usuario', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
