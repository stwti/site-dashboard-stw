# app.py
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'Z6vGqP@4s9!bR1Kx#eP2UwYt$3MnL8dQ'  
# Usuários fixos (simples, sem banco de dados)
usuarios = {
    'DouglasCardoso': {
        'nome': 'Douglas Cardoso',
        'senha': 'senha123',
        'dashboards': [
            {'nome': 'Campanha Loreal - Rebouças',
             'slug': 'campanha_loreal_rb',
             'icone': 'dashboard1.png',
             'embed': 'https://app.powerbi.com/view?r=eyJrIjoiNTg2N2JhNmItZjBhMy00MGQwLThkZmYtNmI3MmU0Zjg1ZDExIiwidCI6ImQ2MzMwOTY2LWY4NWItNGY0MS04NTFkLWE4OGZjOTNlOGM4YiJ9'
            }

        ]
    },
    'bmedeiros': {
        'nome': 'Barbara Medeiros',
        'senha': 'minhasenha',
        'dashboards': [
            {'nome': 'Vendas - Julho',
             'slug': 'Vendas_Julho',
             'icone': 'dashboard3.png',
             'embed': 'https://app.powerbi.com/view?r=eyJrIjoiOGQ5OGM5ZjItOTdmOC00Mjc0LWE0YmMtMzUzYmE0Mzg3ODZlIiwidCI6ImQ2MzMwOTY2LWY4NWItNGY0MS04NTFkLWE4OGZjOTNlOGM4YiJ9'
            },
            {'nome': 'Vendas - Agosto',
             'slug': 'Vendas_Agosto',
             'icone': 'dashboard3.png',
             'embed': 'https://app.powerbi.com/view?r=eyJrIjoiNTNjZTk5OTUtZWM3YS00NDA5LThjMjItYjBlMzEzM2E4ZTQ0IiwidCI6ImQ2MzMwOTY2LWY4NWItNGY0MS04NTFkLWE4OGZjOTNlOGM4YiJ9'
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
    nome = usuarios[usuario]['nome']
    dashboards = usuarios[usuario]['dashboards']
    return render_template('painel.html', usuario=usuario, nome=nome, dashboards=dashboards)

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
