import docker
from flask import Flask
from conf import IMAGE_NAME, APP_PORT, PG_HOST, SECRET_KEY, DEBUG, PG_USER, PG_PASSWORD, PG_DB_NAME, PG_PORT

app = Flask(__name__)


@app.route('/deploy', methods=['GET'])
def deploy_app():
    client = docker.from_env()
    client.containers.run(
        image=IMAGE_NAME,
        auto_remove=True,
        remove=True,
        ports={APP_PORT: APP_PORT},

        environment=[f"PG_HOST={PG_HOST}",
                     f"SECRET_KEY={SECRET_KEY}",
                     f"DEBUG={DEBUG}",
                     f"PG_USER={PG_USER}",
                     f"PG_PASSWORD={PG_PASSWORD}",
                     f"PG_DB_NAME={PG_DB_NAME}",
                     f"PG_PORT={PG_PORT}"
                     ], detach=True, links={f'{PG_HOST}': f'{PG_HOST}'})
    return 'UPLOADED'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8889)
