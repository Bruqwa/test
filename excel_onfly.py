import os
import uvicorn
from services.rest_api.main import factory

app = factory()

if __name__ == '__main__':
    log_config = os.getenv("LOG_CONFIG", 'etc/logging.conf')
    uvicorn.run(
        'excel_onfly:app', host='0.0.0.0', port=8010, reload=True, debug=True, log_config=log_config
    )
