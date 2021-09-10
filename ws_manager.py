from uuid import uuid4


class WsManager:
    def __init__(self):
        self.web_sockets = []
        self.requests = {}
        for i in range(3):
            self.web_sockets.append({
                "ws_id": f"ws-{uuid4().hex}",
                "target_type": "telegram",
                "tags": ['ok']
            })

        for i in range(3):
            self.web_sockets.append({
                "ws_id": f"ws-{uuid4().hex}",
                "target_type": "telegram",
                "tags": ['error']
            })

    def send_task_by_tag(self, tag, task):
        ws_contain_tag = []
        for ws in self.web_sockets:
            if tag in ws['tags']:
                ws_contain_tag.append(ws['ws_id'])

        res = []
        for ws_id in ws_contain_tag:
            req_id = f"req-{uuid4().hex}"
            if tag == 'ok':
                self.requests[req_id] = True
            else:
                self.requests[req_id] = False

            res.append({
                "ws_id": ws_id,
                "request_id": req_id
            })
        return res





