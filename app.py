from flask import Flask, render_template, request, redirect, url_for, session
from usuarios import usuarios
from dashboards import todos_dashboards

app = Flask(__name__)
app.secret_key = 'chave-super-secreta-segura'

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
    dados = usuarios[usuario]
    nome = dados['nome']
    slugs = dados['acesso']
    dashboards = [{**todos_dashboards[slug], 'slug': slug} for slug in slugs if slug in todos_dashboards]
    return render_template('painel.html', nome=nome, dashboards=dashboards)

@app.route('/dashboard/<slug>')
def dashboard(slug):
    if 'usuario' not in session:
        return redirect(url_for('home'))
    usuario = session['usuario']
    if slug not in usuarios[usuario]['acesso']:
        return "Acesso negado", 403
    dash = todos_dashboards.get(slug)
    if dash:
        return render_template('dashboard.html', nome=dash['nome'], embed_link=dash['embed'])
    return "Dashboard não encontrado", 404

@app.route('/logout')
def logout():
    session.pop('usuario', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
