import os

if os.getenv('DETA_RUNTIME'):
    from deta_runtime.deta_main import app
else:
    from local_runtime.local_main import app