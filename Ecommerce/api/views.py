from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Product
from .serializers import ProductSerializer

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Listar': "/listar-produtos/",
        'Detalhes': "/detalhes-produto/<str:pk>/",
        'Criar': "/adicionar-produto/",
        'Atualizar': "/editar-produto/<str:pk>",
        'Deletar': "/excluir-produto/<str:pk>"
    }

    return Response(api_urls)

@api_view(['GET'])
def listarProdutos(request):
    produtos = Product.objects.all()
    serializer = ProductSerializer(produtos, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def detalhesProduto(request, pk):
    produtos = Product.objects.get(id=pk)
    serializer = ProductSerializer(produtos, many=False)

    return Response(serializer.data)


@api_view(['POST'])
def adicionarProduto(request):
    serializer = ProductSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def editarProduto(request, pk):
    produto = Product.objects.get(id=pk)
    serializer = ProductSerializer(instance=produto, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def excluirProduto(request, pk):
    produto = Product.objects.get(id=pk)
    produto.delete()


    return Response('Produto excluído com sucesso')