# 📋 TechFlow Task Manager

Sistema de gerenciamento de tarefas desenvolvido para startup de logística,
baseado em metodologias ágeis (Kanban + Scrum híbrido).

## 🎯 Objetivo

Permitir que equipes acompanhem o fluxo de trabalho em tempo real,
priorizem tarefas críticas e monitorem o desempenho.

## 📦 Escopo inicial

- CRUD completo de tarefas (criar, listar, atualizar, deletar)
- Priorização: Alta / Média / Baixa
- Status: A Fazer / Em Progresso / Concluído
- Interface via terminal (CLI)

## 🔄 Metodologia ágil

Abordagem híbrida **Kanban + Scrum**:
- Quadro Kanban no GitHub Projects para visualizar o fluxo
- Sprints semanais para entregas incrementais
- Revisão contínua do backlog

## 🚀 Como executar

```bash
pip install pytest
python src/app.py
pytest tests/ -v
```

## 🔄 Mudança de escopo — v1.1

**Data:** 28/05/2025
**Motivo:** O cliente de logística solicitou campo de prazo (deadline)
em cada tarefa para controle de tempo nas entregas.
**Impacto:** Campo `deadline` adicionado ao modelo Task. Card
"Adicionar campo deadline" criado no Kanban.
