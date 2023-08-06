from todoist_api_python.api import TodoistAPI

from todoist_service.todoist_wrapper.todoist_wrapper import TodoistWrapper


class TodoistAPIWrapper(TodoistWrapper):
    def get_user_id(self):
        t = self.api.quick_add_task("remove this")
        user_id = t.task.creator_id
        return user_id

    def get_user_name(self):
        return "Unknown"

    def __init__(self, token):
        self.api = TodoistAPI(token=token)

    def get_all_labels(self):
        return self.api.get_labels()

    def get_tasks(self, filt):
        return self.api.get_tasks(filt=filt)

    def get_all_tasks(self):
        return self.api.get_tasks()

    def get_task_by_id(self, item_id):
        return self.api.get_task(item_id)

    def update_task(self, task_id: str, **kwargs):
        return self.api.update_task(task_id, **kwargs)

    def add_label(self, name):
        return self.api.add_label(name)

    def get_label(self, label_id):
        return self.api.get_label(label_id)

    def add_project(self, name):
        return self.api.add_project(name)

    def get_project(self, project_id):
        return self.api.get_project(project_id)

    def get_all_projects(self):
        return self.api.get_projects()
