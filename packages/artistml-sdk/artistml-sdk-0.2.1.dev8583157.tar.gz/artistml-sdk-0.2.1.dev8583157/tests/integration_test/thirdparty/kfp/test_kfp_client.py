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


def test_create_experiment():
    client = Client(
        host="https://kubeflow.platform.artistml.com/pipeline",
        namespace="kubeflow-user-example-com",
    )
    client.list_experiments(namespace="kubeflow-user-example-com", )
