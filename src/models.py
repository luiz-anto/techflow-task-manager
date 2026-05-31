
class Task:

    def __init__(self, id, title, priority="Media",
                 status="A Fazer", deadline=None):
        # id: identificador único da tarefa
        self.id = id
        # title: descrição da tarefa
        self.title = title
        # priority: Alta, Media ou Baixa
        self.priority = priority
        # status: A Fazer, Em Progresso ou Concluido
        self.status = status
        # deadline: prazo de entrega (adicionado na v1.1)
        self.deadline = deadline

    def __repr__(self):
        return (f"Task(id={self.id}, title='{self.title}', "
                f"priority='{self.priority}', "
                f"status='{self.status}', "
                f"deadline='{self.deadline}')")
