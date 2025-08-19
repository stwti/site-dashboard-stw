# app.py
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'Z6vGqP@4s9!bR1Kx#eP2UwYt$3MnL8dQ'  
# Usuários fixos 
usuarios = {
    'stwti': {
        'nome': 'Tecnologia da Informação',
        'senha': 'Studiow@2025',
        'dashboards': [
            {'nome': 'Campanha Loreal - Rebouças',
             'slug': 'campanha_loreal_rb',
             'icone': 'dashboard1.png',
             'embed': 'https://app.powerbi.com/view?r=eyJrIjoiNTg2N2JhNmItZjBhMy00MGQwLThkZmYtNmI3MmU0Zjg1ZDExIiwidCI6ImQ2MzMwOTY2LWY4NWItNGY0MS04NTFkLWE4OGZjOTNlOGM4YiJ9'
            },
            {'nome': 'Vendas - Agosto',
             'slug': 'Vendas_Agosto',
             'icone': 'dashboard1.png',
             'embed': 'https://app.powerbi.com/view?r=eyJrIjoiNWE4YTVhNDMtZWE3NC00MGVhLTkzODQtM2YxM2FhNWU2MDE0IiwidCI6ImQ2MzMwOTY2LWY4NWItNGY0MS04NTFkLWE4OGZjOTNlOGM4YiJ9'
            }

        ]
    },
    'greboucas': {
        'nome': 'Gerência Rebouças',
        'senha': 'PwbiRb@1808',
        'dashboards': [
            {'nome': 'Vendas - Julho',
             'slug': 'Vendas_Julho',
             'icone': 'dashboard3.png',
             'embed': 'https://app.powerbi.com/view?r=eyJrIjoiOGQ5OGM5ZjItOTdmOC00Mjc0LWE0YmMtMzUzYmE0Mzg3ODZlIiwidCI6ImQ2MzMwOTY2LWY4NWItNGY0MS04NTFkLWE4OGZjOTNlOGM4YiJ9'
            },
            {'nome': 'Vendas - Agosto',
             'slug': 'Vendas_Agosto',
             'icone': 'dashboard2.png',
             'embed': 'https://app.powerbi.com/view?r=eyJrIjoiNWE4YTVhNDMtZWE3NC00MGVhLTkzODQtM2YxM2FhNWU2MDE0IiwidCI6ImQ2MzMwOTY2LWY4NWItNGY0MS04NTFkLWE4OGZjOTNlOGM4YiJ9'
            },
            {'nome': 'Campanha Wella Assistentes',
             'slug': 'Wella_Assistentes',
             'icone': 'dashboard1.png',
             'embed': 'https://app.powerbi.com/view?r=eyJrIjoiM2QwZjFhYjEtYjg1NC00ZGFhLTgzYjEtNGU4Y2Q5YmZiOGE3IiwidCI6ImQ2MzMwOTY2LWY4NWItNGY0MS04NTFkLWE4OGZjOTNlOGM4YiJ9'
            },
            {'nome': 'Campanha Wella Rede',
             'slug': 'Wella_Rede',
             'icone': 'dashboard4.png',
             'embed': 'https://app.powerbi.com/view?r=eyJrIjoiZWIzMGMxMDQtYWI4ZS00NTAwLTlhNmItNjY3OWI0MjAxNzFlIiwidCI6ImQ2MzMwOTY2LWY4NWItNGY0MS04NTFkLWE4OGZjOTNlOGM4YiJ9'
            },
            {'nome': 'Campanha Loreal Coloração',
             'slug': 'Loreal_Coloracao',
             'icone': 'dashboard3.png',
             'embed': 'https://app.powerbi.com/view?r=eyJrIjoiNWZjYTdiZjAtN2FmZC00N2Q1LWJkMGMtNWY1NjdjMGYzYjYzIiwidCI6ImQ2MzMwOTY2LWY4NWItNGY0MS04NTFkLWE4OGZjOTNlOGM4YiJ9'
            },
            {'nome': 'Campanha Loreal Rede',
             'slug': 'Loreal_Rede',
             'icone': 'dashboard4.png',
             'embed': 'https://app.powerbi.com/view?r=eyJrIjoiMjQ0M2Y5YWYtYTE4NC00NDk3LWIxNTAtMjc5NjhiMzBlNGIyIiwidCI6ImQ2MzMwOTY2LWY4NWItNGY0MS04NTFkLWE4OGZjOTNlOGM4YiJ9'
            },
            {'nome': 'Campanha Gerentes - Wella',
             'slug': 'Wella_Gerentes',
             'icone': 'dashboard2.png',
             'embed': 'https://app.powerbi.com/view?r=eyJrIjoiYjVkMDVhYWMtNTc4Zi00NmM5LWJhYWItODg4ZWMxOGE4ZGM0IiwidCI6ImQ2MzMwOTY2LWY4NWItNGY0MS04NTFkLWE4OGZjOTNlOGM4YiJ9'
            },
            {'nome': 'Campanha Gerentes - Loreal',
             'slug': 'Loreal_Gerentes',
             'icone': 'dashboard1.png',
             'embed': 'https://app.powerbi.com/view?r=eyJrIjoiYjU0YmE1YjctYWE5ZC00ZjdmLWJjYTAtOThmZjYwZmVlMTgyIiwidCI6ImQ2MzMwOTY2LWY4NWItNGY0MS04NTFkLWE4OGZjOTNlOGM4YiJ9'
            }
        ]
    },
    'ghigi': {
        'nome': 'Gerência Higienópolis',
        'senha': 'PwbiHg@1809',
        'dashboards': [
            {'nome': 'Campanha Wella Assistentes',
             'slug': 'Wella_Assistentes',
             'icone': 'dashboard1.png',
             'embed': 'https://app.powerbi.com/view?r=eyJrIjoiM2QwZjFhYjEtYjg1NC00ZGFhLTgzYjEtNGU4Y2Q5YmZiOGE3IiwidCI6ImQ2MzMwOTY2LWY4NWItNGY0MS04NTFkLWE4OGZjOTNlOGM4YiJ9'
            },
            {'nome': 'Campanha Wella Rede',
             'slug': 'Wella_Rede',
             'icone': 'dashboard4.png',
             'embed': 'https://app.powerbi.com/view?r=eyJrIjoiZWIzMGMxMDQtYWI4ZS00NTAwLTlhNmItNjY3OWI0MjAxNzFlIiwidCI6ImQ2MzMwOTY2LWY4NWItNGY0MS04NTFkLWE4OGZjOTNlOGM4YiJ9'
            },
            {'nome': 'Campanha Loreal Coloração',
             'slug': 'Loreal_Coloracao',
             'icone': 'dashboard3.png',
             'embed': 'https://app.powerbi.com/view?r=eyJrIjoiNWZjYTdiZjAtN2FmZC00N2Q1LWJkMGMtNWY1NjdjMGYzYjYzIiwidCI6ImQ2MzMwOTY2LWY4NWItNGY0MS04NTFkLWE4OGZjOTNlOGM4YiJ9'
            },
            {'nome': 'Campanha Loreal Rede',
             'slug': 'Loreal_Rede',
             'icone': 'dashboard4.png',
             'embed': 'https://app.powerbi.com/view?r=eyJrIjoiMjQ0M2Y5YWYtYTE4NC00NDk3LWIxNTAtMjc5NjhiMzBlNGIyIiwidCI6ImQ2MzMwOTY2LWY4NWItNGY0MS04NTFkLWE4OGZjOTNlOGM4YiJ9'
            },
            {'nome': 'Campanha Gerentes - Wella',
             'slug': 'Wella_Gerentes',
             'icone': 'dashboard2.png',
             'embed': 'https://app.powerbi.com/view?r=eyJrIjoiMGM4ZjhmY2YtODFjNi00NjdjLWE4NjQtOTIxNTU3M2RhOTBjIiwidCI6ImQ2MzMwOTY2LWY4NWItNGY0MS04NTFkLWE4OGZjOTNlOGM4YiJ9'
            },
            {'nome': 'Campanha Gerentes - Loreal',
             'slug': 'Loreal_Gerentes',
             'icone': 'dashboard1.png',
             'embed': 'https://app.powerbi.com/view?r=eyJrIjoiNmFmNzFhODQtMTRiMC00ZTk1LWJjYWEtMWNiZjhkOTI1MzFjIiwidCI6ImQ2MzMwOTY2LWY4NWItNGY0MS04NTFkLWE4OGZjOTNlOGM4YiJ9'
            }

        ]
    },
    'gjk': {
        'nome': 'Gerência JK',
        'senha': 'PwbiJk@1811',
        'dashboards': [
            {'nome': 'Campanha Wella Assistentes',
             'slug': 'Wella_Assistentes',
             'icone': 'dashboard1.png',
             'embed': 'https://app.powerbi.com/view?r=eyJrIjoiM2QwZjFhYjEtYjg1NC00ZGFhLTgzYjEtNGU4Y2Q5YmZiOGE3IiwidCI6ImQ2MzMwOTY2LWY4NWItNGY0MS04NTFkLWE4OGZjOTNlOGM4YiJ9'
            },
            {'nome': 'Campanha Wella Rede',
             'slug': 'Wella_Rede',
             'icone': 'dashboard4.png',
             'embed': 'https://app.powerbi.com/view?r=eyJrIjoiZWIzMGMxMDQtYWI4ZS00NTAwLTlhNmItNjY3OWI0MjAxNzFlIiwidCI6ImQ2MzMwOTY2LWY4NWItNGY0MS04NTFkLWE4OGZjOTNlOGM4YiJ9'
            },
            {'nome': 'Campanha Loreal Coloração',
             'slug': 'Loreal_Coloracao',
             'icone': 'dashboard3.png',
             'embed': 'https://app.powerbi.com/view?r=eyJrIjoiNWZjYTdiZjAtN2FmZC00N2Q1LWJkMGMtNWY1NjdjMGYzYjYzIiwidCI6ImQ2MzMwOTY2LWY4NWItNGY0MS04NTFkLWE4OGZjOTNlOGM4YiJ9'
            },
            {'nome': 'Campanha Loreal Rede',
             'slug': 'Loreal_Rede',
             'icone': 'dashboard4.png',
             'embed': 'https://app.powerbi.com/view?r=eyJrIjoiMjQ0M2Y5YWYtYTE4NC00NDk3LWIxNTAtMjc5NjhiMzBlNGIyIiwidCI6ImQ2MzMwOTY2LWY4NWItNGY0MS04NTFkLWE4OGZjOTNlOGM4YiJ9'
            },
            {'nome': 'Campanha Gerentes - Wella',
             'slug': 'Wella_Gerentes',
             'icone': 'dashboard2.png',
             'embed': 'https://app.powerbi.com/view?r=eyJrIjoiMTY3YjI0MjEtZWYyNy00NGFhLWJjNTMtMzJkNTUwMzM4ZmJkIiwidCI6ImQ2MzMwOTY2LWY4NWItNGY0MS04NTFkLWE4OGZjOTNlOGM4YiJ9'
            },
            {'nome': 'Campanha Gerentes - Loreal',
             'slug': 'Loreal_Gerentes',
             'icone': 'dashboard1.png',
             'embed': 'https://app.powerbi.com/view?r=eyJrIjoiOTFkMTZjYzItNjE1OC00YmMyLTg4MzMtODU1MzhjOGEwYjc0IiwidCI6ImQ2MzMwOTY2LWY4NWItNGY0MS04NTFkLWE4OGZjOTNlOGM4YiJ9'
            }

        ]
    },
    'gritu': {
        'nome': 'Gerência Ritu',
        'senha': 'PwbiRitu@1812',
        'dashboards': [
            {'nome': 'Campanha Wella Assistentes',
             'slug': 'Wella_Assistentes',
             'icone': 'dashboard1.png',
             'embed': 'https://app.powerbi.com/view?r=eyJrIjoiM2QwZjFhYjEtYjg1NC00ZGFhLTgzYjEtNGU4Y2Q5YmZiOGE3IiwidCI6ImQ2MzMwOTY2LWY4NWItNGY0MS04NTFkLWE4OGZjOTNlOGM4YiJ9'
            },
            {'nome': 'Campanha Wella Rede',
             'slug': 'Wella_Rede',
             'icone': 'dashboard4.png',
             'embed': 'https://app.powerbi.com/view?r=eyJrIjoiZWIzMGMxMDQtYWI4ZS00NTAwLTlhNmItNjY3OWI0MjAxNzFlIiwidCI6ImQ2MzMwOTY2LWY4NWItNGY0MS04NTFkLWE4OGZjOTNlOGM4YiJ9'
            },
            {'nome': 'Campanha Loreal Coloração',
             'slug': 'Loreal_Coloracao',
             'icone': 'dashboard3.png',
             'embed': 'https://app.powerbi.com/view?r=eyJrIjoiNWZjYTdiZjAtN2FmZC00N2Q1LWJkMGMtNWY1NjdjMGYzYjYzIiwidCI6ImQ2MzMwOTY2LWY4NWItNGY0MS04NTFkLWE4OGZjOTNlOGM4YiJ9'
            },
            {'nome': 'Campanha Loreal Rede',
             'slug': 'Loreal_Rede',
             'icone': 'dashboard4.png',
             'embed': 'https://app.powerbi.com/view?r=eyJrIjoiMjQ0M2Y5YWYtYTE4NC00NDk3LWIxNTAtMjc5NjhiMzBlNGIyIiwidCI6ImQ2MzMwOTY2LWY4NWItNGY0MS04NTFkLWE4OGZjOTNlOGM4YiJ9'
            },
            {'nome': 'Campanha Gerentes - Wella',
             'slug': 'Wella_Gerentes',
             'icone': 'dashboard2.png',
             'embed': 'https://app.powerbi.com/view?r=eyJrIjoiYjVkMDVhYWMtNTc4Zi00NmM5LWJhYWItODg4ZWMxOGE4ZGM0IiwidCI6ImQ2MzMwOTY2LWY4NWItNGY0MS04NTFkLWE4OGZjOTNlOGM4YiJ9'
            },
            {'nome': 'Campanha Gerentes - Loreal',
             'slug': 'Loreal_Gerentes',
             'icone': 'dashboard1.png',
             'embed': 'https://app.powerbi.com/view?r=eyJrIjoiYjU0YmE1YjctYWE5ZC00ZjdmLWJjYTAtOThmZjYwZmVlMTgyIiwidCI6ImQ2MzMwOTY2LWY4NWItNGY0MS04NTFkLWE4OGZjOTNlOGM4YiJ9'
            }

        ]
    },
    'gcampinas': {
        'nome': 'Gerência Campinas',
        'senha': 'PwbiCamp@1813',
        'dashboards': [
            {'nome': 'Campanha Wella Assistentes',
             'slug': 'Wella_Assistentes',
             'icone': 'dashboard1.png',
             'embed': 'https://app.powerbi.com/view?r=eyJrIjoiM2QwZjFhYjEtYjg1NC00ZGFhLTgzYjEtNGU4Y2Q5YmZiOGE3IiwidCI6ImQ2MzMwOTY2LWY4NWItNGY0MS04NTFkLWE4OGZjOTNlOGM4YiJ9'
            },
            {'nome': 'Campanha Wella Rede',
             'slug': 'Wella_Rede',
             'icone': 'dashboard4.png',
             'embed': 'https://app.powerbi.com/view?r=eyJrIjoiZWIzMGMxMDQtYWI4ZS00NTAwLTlhNmItNjY3OWI0MjAxNzFlIiwidCI6ImQ2MzMwOTY2LWY4NWItNGY0MS04NTFkLWE4OGZjOTNlOGM4YiJ9'
            },
            {'nome': 'Campanha Loreal Coloração',
             'slug': 'Loreal_Coloracao',
             'icone': 'dashboard3.png',
             'embed': 'https://app.powerbi.com/view?r=eyJrIjoiNWZjYTdiZjAtN2FmZC00N2Q1LWJkMGMtNWY1NjdjMGYzYjYzIiwidCI6ImQ2MzMwOTY2LWY4NWItNGY0MS04NTFkLWE4OGZjOTNlOGM4YiJ9'
            },
            {'nome': 'Campanha Loreal Rede',
             'slug': 'Loreal_Rede',
             'icone': 'dashboard4.png',
             'embed': 'https://app.powerbi.com/view?r=eyJrIjoiMjQ0M2Y5YWYtYTE4NC00NDk3LWIxNTAtMjc5NjhiMzBlNGIyIiwidCI6ImQ2MzMwOTY2LWY4NWItNGY0MS04NTFkLWE4OGZjOTNlOGM4YiJ9'
            },
            {'nome': 'Campanha Gerentes - Wella',
             'slug': 'Wella_Gerentes',
             'icone': 'dashboard2.png',
             'embed': 'https://app.powerbi.com/view?r=eyJrIjoiNDQ0MzhlMGQtYTQxMS00YWVjLTkxNTUtOGQ4ZjJiZDVmYTJjIiwidCI6ImQ2MzMwOTY2LWY4NWItNGY0MS04NTFkLWE4OGZjOTNlOGM4YiJ9'
            },
            {'nome': 'Campanha Gerentes - Loreal',
             'slug': 'Loreal_Gerentes',
             'icone': 'dashboard1.png',
             'embed': 'https://app.powerbi.com/view?r=eyJrIjoiYzMwYTMzZWUtNmUzNy00ZTRmLWEzNDEtNDZmNzRhYTVlOGYwIiwidCI6ImQ2MzMwOTY2LWY4NWItNGY0MS04NTFkLWE4OGZjOTNlOGM4YiJ9'
            }

        ]
    },
        'gribeirao': {
        'nome': 'Gerência Ribeirão',
        'senha': 'PwbiRib@1813',
        'dashboards': [
            {'nome': 'Campanha Wella Assistentes',
             'slug': 'Wella_Assistentes',
             'icone': 'dashboard1.png',
             'embed': 'https://app.powerbi.com/view?r=eyJrIjoiM2QwZjFhYjEtYjg1NC00ZGFhLTgzYjEtNGU4Y2Q5YmZiOGE3IiwidCI6ImQ2MzMwOTY2LWY4NWItNGY0MS04NTFkLWE4OGZjOTNlOGM4YiJ9'
            },
            {'nome': 'Campanha Wella Rede',
             'slug': 'Wella_Rede',
             'icone': 'dashboard4.png',
             'embed': 'https://app.powerbi.com/view?r=eyJrIjoiZWIzMGMxMDQtYWI4ZS00NTAwLTlhNmItNjY3OWI0MjAxNzFlIiwidCI6ImQ2MzMwOTY2LWY4NWItNGY0MS04NTFkLWE4OGZjOTNlOGM4YiJ9'
            },
            {'nome': 'Campanha Loreal Coloração',
             'slug': 'Loreal_Coloracao',
             'icone': 'dashboard3.png',
             'embed': 'https://app.powerbi.com/view?r=eyJrIjoiNWZjYTdiZjAtN2FmZC00N2Q1LWJkMGMtNWY1NjdjMGYzYjYzIiwidCI6ImQ2MzMwOTY2LWY4NWItNGY0MS04NTFkLWE4OGZjOTNlOGM4YiJ9'
            },
            {'nome': 'Campanha Loreal Rede',
             'slug': 'Loreal_Rede',
             'icone': 'dashboard4.png',
             'embed': 'https://app.powerbi.com/view?r=eyJrIjoiMjQ0M2Y5YWYtYTE4NC00NDk3LWIxNTAtMjc5NjhiMzBlNGIyIiwidCI6ImQ2MzMwOTY2LWY4NWItNGY0MS04NTFkLWE4OGZjOTNlOGM4YiJ9'
            },
            {'nome': 'Campanha Gerentes - Wella',
             'slug': 'Wella_Gerentes',
             'icone': 'dashboard2.png',
             'embed': 'https://app.powerbi.com/view?r=eyJrIjoiNDBlOWYyYjMtNWM4NS00OGM5LThmOTEtYTNkYjQ5NWEyMWEyIiwidCI6ImQ2MzMwOTY2LWY4NWItNGY0MS04NTFkLWE4OGZjOTNlOGM4YiJ9'
            },
            {'nome': 'Campanha Gerentes - Loreal',
             'slug': 'Loreal_Gerentes',
             'icone': 'dashboard1.png',
             'embed': 'https://app.powerbi.com/view?r=eyJrIjoiMmUxOTMyNzYtZjFkZS00NDEzLTlhM2QtMmY5ZTJlN2RmMjBhIiwidCI6ImQ2MzMwOTY2LWY4NWItNGY0MS04NTFkLWE4OGZjOTNlOGM4YiJ9'
            }

        ]
    },
        'hnavarini': {
        'nome': 'Herbert Navarini',
        'senha': 'PiwbW@1813',
        'dashboards': [
            {'nome': 'Vendas - Julho',
             'slug': 'Vendas_Julho',
             'icone': 'dashboard3.png',
             'embed': 'https://app.powerbi.com/view?r=eyJrIjoiOGQ5OGM5ZjItOTdmOC00Mjc0LWE0YmMtMzUzYmE0Mzg3ODZlIiwidCI6ImQ2MzMwOTY2LWY4NWItNGY0MS04NTFkLWE4OGZjOTNlOGM4YiJ9'
            },
            {'nome': 'Vendas - Agosto',
             'slug': 'Vendas_Agosto',
             'icone': 'dashboard2.png',
             'embed': 'https://app.powerbi.com/view?r=eyJrIjoiNWE4YTVhNDMtZWE3NC00MGVhLTkzODQtM2YxM2FhNWU2MDE0IiwidCI6ImQ2MzMwOTY2LWY4NWItNGY0MS04NTFkLWE4OGZjOTNlOGM4YiJ9'
            },
            {'nome': 'Campanha Wella Assistentes',
             'slug': 'Wella_Assistentes',
             'icone': 'dashboard1.png',
             'embed': 'https://app.powerbi.com/view?r=eyJrIjoiM2QwZjFhYjEtYjg1NC00ZGFhLTgzYjEtNGU4Y2Q5YmZiOGE3IiwidCI6ImQ2MzMwOTY2LWY4NWItNGY0MS04NTFkLWE4OGZjOTNlOGM4YiJ9'
            },
            {'nome': 'Campanha Wella Rede',
             'slug': 'Wella_Rede',
             'icone': 'dashboard4.png',
             'embed': 'https://app.powerbi.com/view?r=eyJrIjoiZWIzMGMxMDQtYWI4ZS00NTAwLTlhNmItNjY3OWI0MjAxNzFlIiwidCI6ImQ2MzMwOTY2LWY4NWItNGY0MS04NTFkLWE4OGZjOTNlOGM4YiJ9'
            },
            {'nome': 'Campanha Loreal Coloração',
             'slug': 'Loreal_Coloracao',
             'icone': 'dashboard3.png',
             'embed': 'https://app.powerbi.com/view?r=eyJrIjoiNWZjYTdiZjAtN2FmZC00N2Q1LWJkMGMtNWY1NjdjMGYzYjYzIiwidCI6ImQ2MzMwOTY2LWY4NWItNGY0MS04NTFkLWE4OGZjOTNlOGM4YiJ9'
            },
            {'nome': 'Campanha Loreal Rede',
             'slug': 'Loreal_Rede',
             'icone': 'dashboard4.png',
             'embed': 'https://app.powerbi.com/view?r=eyJrIjoiMjQ0M2Y5YWYtYTE4NC00NDk3LWIxNTAtMjc5NjhiMzBlNGIyIiwidCI6ImQ2MzMwOTY2LWY4NWItNGY0MS04NTFkLWE4OGZjOTNlOGM4YiJ9'
            },
            {'nome': 'Campanha Gerentes - Wella',
             'slug': 'Wella_Gerentes',
             'icone': 'dashboard2.png',
             'embed': 'https://app.powerbi.com/view?r=eyJrIjoiYjVkMDVhYWMtNTc4Zi00NmM5LWJhYWItODg4ZWMxOGE4ZGM0IiwidCI6ImQ2MzMwOTY2LWY4NWItNGY0MS04NTFkLWE4OGZjOTNlOGM4YiJ9'
            },
            {'nome': 'Campanha Gerentes - Loreal',
             'slug': 'Loreal_Gerentes',
             'icone': 'dashboard1.png',
             'embed': 'https://app.powerbi.com/view?r=eyJrIjoiYjU0YmE1YjctYWE5ZC00ZjdmLWJjYTAtOThmZjYwZmVlMTgyIiwidCI6ImQ2MzMwOTY2LWY4NWItNGY0MS04NTFkLWE4OGZjOTNlOGM4YiJ9'
            }

        ]
    },


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
