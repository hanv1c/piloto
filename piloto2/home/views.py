from django.shortcuts import render

LISTA_ALUNOS = [
    {"nome": "João Silva", "matricula": "202301", "curso": "Técnico em Informática", "turma": "208",'data_de_nascimento':'99/99/9999'},
    {"nome": "Maria Oliveira", "matricula": "202302", "curso": "Técnico em Informática", "turma": "208",'data_de_nascimento':'24/03/2008'},
    {"nome": "Carlos Souza", "matricula": "202303", "curso": "Técnico em Informática", "turma": "208",'data_de_nascimento':'00/00/0000'},
]


def index(request):
    return render(request, 'index.html')
def sobre(request):
    return render(request, 'sobre.html')
def contato(resquest):
    return render(resquest, 'contato.html')
def ajuda(resquest):
    return render(resquest, 'ajuda.html')
def local(request):
    return render(request, 'local.html')
def exibirItem(request,id):
    return render(request,'exibir_item.html',{'id':id})
def perfil(request,usuario):
    return render(request,'perfil.html',{'usuario':usuario})
def diadasemana(request,dia):
    dias = ["Domingo","Segunda-Feira","Terça-Feira","Quarta-Feira","Quinta-Feira","Sexta-Feira","Sábado"]
    if dia < 1 or dia > 7:
        mensagem = "Digite um valor válido"
    else:
        mensagem = dias[dia-1]
    return render(request,'diaDaSemana.html',{'msg':mensagem})
def dados(request):
    contexto = {
        'nome':'dandhyluhan',
        'idade':17,
        'cidade':'Teresina'
    }
    return render(request,'dados.html',contexto)
def form(request):
    if request.method == "POST": 
        nome = request.POST.get("nome")
        idade = request.POST.get("idade")
        cidade = request.POST.get("cidade")
        data_de_nascimento = request.POST.get("data_de_nascimento")
        context = {
            'nome': nome,
            'idade': idade,
            'cidade': cidade,
            'data_de_nascimento': data_de_nascimento,
        }
        return render(request,'dados.html',context)
    else:
        return render(request,'form.html')
def listarAlunos(request):
    context = {
        'lista': LISTA_ALUNOS,
    }
    return render(request, 'listar_alunos.html', context)
