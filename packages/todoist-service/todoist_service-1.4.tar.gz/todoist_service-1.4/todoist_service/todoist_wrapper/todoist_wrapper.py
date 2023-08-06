from todoist_api_python.models import Label, Task, Project


class TodoistWrapper:

    def get_all_labels(self) -> [Label]:
        raise NotImplementedError()

    def get_tasks(self, filt) -> [Task]:
        raise NotImplementedError

    def get_all_tasks(self) -> [Task]:
        raise NotImplementedError()

    def get_task_by_id(self, item_id) -> Task:
        raise NotImplementedError()

    def add_label(self, name) -> Label:
        raise NotImplementedError()

    def get_label(self, label_id) -> Label:
        raise NotImplementedError()

    def add_project(self, name) -> Project:
        raise NotImplementedError()

    def get_project(self, project_id) -> Project:
        raise NotImplementedError()

    def get_all_projects(self) -> [Project]:
        raise NotImplementedError()

    def get_user_id(self) -> str:
        raise NotImplementedError()

    def get_user_name(self) -> str:
        raise NotImplementedError()

    def update_task(self, task_id: str, **kwargs) -> bool:
        raise NotImplementedError()
