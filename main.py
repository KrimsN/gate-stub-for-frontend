from fastapi import FastAPI
from starlette.config import Config

from schemes import (
    AddTaskByTagBodyScheme,
    AddTaskByWsIdsBodyScheme,
    AddTaskByUsernameScheme
)
from task_service import TaskService


REQUESTS = {
    'send_personal_message': {
        "ws_id": "ws-42f1629b09a1480181e4b612167115d9",
        "data": {
            "message_id": 1285,
            "date": 1631256188,
            "text": "msg",
            "entities": [],
            "outgoing": True
        }
    },
    'account_info': {
        "ws_id": "ws-42f1629b09a1480181e4b612167115d9",
        "data": {
            "id": 967403852,
            "is_self": True,
            "is_contact": False,
            "is_mutual_contact": False,
            "is_deleted": False,
            "is_bot": False,
            "is_verified": False,
            "is_restricted": False,
            "is_scam": False,
            "is_fake": False,
            "is_support": False,
            "first_name": "Viktor Nic",
            "status": "offline",
            "last_online_date": 1631256488,
            "username": "vicnuku",
            "dc_id": 2
        }
      }
}


app = FastAPI()

task_service = TaskService()


@app.post('/addTaskByTag')
def add_task_by_tag(body: AddTaskByTagBodyScheme):
    res = task_service.add_task_by_tag(body.dict(exclude={"tag"}), tag=body.tag)
    return res


@app.post('/addTaskByWsIds')
def add_task_by_ws_ids(body: AddTaskByWsIdsBodyScheme):
    pass


@app.post('/addTaskByUsername')
def add_task_by_username(body: AddTaskByUsernameScheme):
    pass


@app.get('/getTaskInfo')
def get_task_info(task_id: str):
    res = []
    task = task_service.storage[task_id]
    for worker in task['workers']:
        req_id = worker['request_id']
        req_res = task_service.ws_manager.requests[req_id]
        if req_res:
            method = task['data']['method']
            r = REQUESTS[method]
            r['ws_id'] = worker['ws_id']
            res.append(r)
        else:
            res.append({
                'ws_id': worker['ws_id'],
                'data': 'waiting result'
            })

    return res
