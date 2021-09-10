from uuid import uuid4
from ws_manager import WsManager


class TaskService:

    def __init__(self):
        self.storage = {}
        self.ws_manager = WsManager()

    def add_task_by_tag(self, task_data, tag):
        task_id = f"task-{uuid4().hex}"

        workers = self.ws_manager.send_task_by_tag(tag, task_data)

        res_task = {
            "task_id": task_id,
            "data": task_data,
            "workers": workers
        }
        self.storage[task_id] = res_task
        return res_task





