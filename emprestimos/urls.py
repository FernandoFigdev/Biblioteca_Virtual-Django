from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmprestimoViewSet, RelatorioEmprestimosView

router = DefaultRouter()
router.register(r'', EmprestimoViewSet)

urlpatterns = [
    path('relatorio-emprestimos/', RelatorioEmprestimosView.as_view(), name='relatorio-emprestimos'),
    path('<int:pk>/aprovar/', EmprestimoViewSet.as_view({'post': 'aprovar'}), name='aprovar-emprestimo'),
    path('<int:pk>/concluir/', EmprestimoViewSet.as_view({'post': 'concluir'}), name='concluir-emprestimo'),
    path('', include(router.urls)),
]
