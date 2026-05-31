import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import pytest
import app
from app import create_task, list_tasks, update_task, delete_task, tasks


@pytest.fixture(autouse=True)
def reset():
    """Limpa tarefas e reseta ID antes de cada teste."""
    tasks.clear()
    app.next_id = 1
    yield
    tasks.clear()


def test_criar_tarefa_simples():
    """Deve criar tarefa com título válido."""
    t = create_task("Minha tarefa")
    assert t.title == "Minha tarefa"
    assert t.id == 1
    assert t.priority == "Media"
    assert t.status == "A Fazer"

def test_criar_tarefa_prioridade_alta():
    """Deve criar tarefa com prioridade Alta."""
    t = create_task("Urgente", priority="Alta")
    assert t.priority == "Alta"

def test_criar_tarefa_com_deadline():
    """Deve criar tarefa com prazo (mudança de escopo v1.1)."""
    t = create_task("Entrega", deadline="30/05/2025")
    assert t.deadline == "30/05/2025"

def test_titulo_vazio_levanta_erro():
    """Deve lançar ValueError para título vazio."""
    with pytest.raises(ValueError):
        create_task("")

def test_ids_sequenciais():
    """IDs devem ser únicos e sequenciais."""
    t1 = create_task("T1")
    t2 = create_task("T2")
    assert t1.id == 1
    assert t2.id == 2

def test_listar_tarefas_vazia():
    """Lista deve começar vazia."""
    assert list_tasks() == []

def test_listar_retorna_todas():
    """Deve retornar todas as tarefas criadas."""
    create_task("A"); create_task("B")
    assert len(list_tasks()) == 2

def test_atualizar_status():
    """Deve atualizar o status da tarefa."""
    create_task("Tarefa")
    t = update_task(1, status="Em Progresso")
    assert t.status == "Em Progresso"

def test_atualizar_inexistente_retorna_none():
    """Deve retornar None para ID que não existe."""
    assert update_task(999, status="Concluido") is None

def test_deletar_tarefa():
    """Deve remover a tarefa e retornar True."""
    create_task("Deletar")
    assert delete_task(1) is True
    assert len(list_tasks()) == 0

def test_deletar_inexistente_retorna_false():
    """Deve retornar False para ID inexistente."""
    assert delete_task(999) is False
