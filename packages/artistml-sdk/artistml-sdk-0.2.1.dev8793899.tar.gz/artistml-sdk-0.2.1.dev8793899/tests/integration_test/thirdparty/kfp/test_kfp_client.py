import re

import requests
from kfp import Client
from kfp import compiler
from kfp import dsl

from artistml_sdk.lib import config

kfp_host = config.test.get_val(
    "kfp",
    "host",
)
kfp_port = config.test.get_val(
    "kfp",
    "port",
)


@dsl.component
def addition_component(num1: int, num2: int) -> int:
    return num1 + num2


@dsl.pipeline(name='addition-pipeline')
def my_pipeline(a: int, b: int, c: int = 10):
    add_task_1 = addition_component(num1=a, num2=b)
    add_task_2 = addition_component(num1=add_task_1.output, num2=c)


cmplr = compiler.Compiler()

CLUSTER_IP = "kubeflow.platform.artistml.com"


def get_authservice_session_when_multiuser() -> str:
    response = requests.get(f"https://{CLUSTER_IP}")
    response_text = response.text
    # print(response_text)
    # //Extract the request token REQ_VALUE as done in step
    req_token = re.search('state=(.+)">', response_text).group(1)
    creds = {'login': 'user@example.com', 'password': '12341234'}
    response = requests.post(
        f"https://{CLUSTER_IP}/dex/auth/local/login?back=&state={req_token}",
        data=creds,
        headers={'Content-Type': 'application/x-www-form-urlencoded'},
    )
    # // Cookie was set in the last redirection, hence we need to fetch that from response.history
    cookie = "authservice_session=" + response.history[2].cookies.get(
        'authservice_session')
    return cookie


def test_create_experiment():

    client = Client(
        host="https://kubeflow.platform.artistml.com/pipeline",
        # namespace="kubeflow-user-example-com",
        # cookies=get_authservice_session_when_multiuser(),
    )
    print(client.list_experiments(
        # namespace="kubeflow-user-example-com",
    ))
    print(
        client.create_experiment(name="sylvan-test",
                                 # namespace="kubeflow-user-example-com",
                                 ))
