from fastapi import FastAPI
from starlette.config import Config


CONFIG = {}


def setup_config():
    global CONFIG
    config = Config('.env')
    CONFIG['var_11'] = config('VAR11')
    CONFIG['var_22'] = config('VAR22')


setup_config()

app = FastAPI()


@app.get('/')
async def env_vars():
    return {
        'var_11': CONFIG.get('var_11'),
        'var_22': CONFIG.get('var_22'),
    }
