import tempfile
from typing import Callable
from typing import Final

from kfp import compiler
from kfp import components

from ..apis.common.v1.types_pb2 import CommonFilter
from ..apis.common.v1.types_pb2 import CommonOption
from ..apis.muses.v1.component_pb2 import Component
from ..apis.muses.v1.component_pb2 import ComponentOptionFilter
from ..apis.muses.v1.component_service_pb2 import CreateComponentRequest
from ..apis.muses.v1.component_service_pb2 import CreateComponentResponse
from ..apis.muses.v1.component_service_pb2 import DeleteComponentRequest
from ..apis.muses.v1.component_service_pb2 import DeleteComponentResponse
from ..apis.muses.v1.component_service_pb2 import DeleteComponentsRequest
from ..apis.muses.v1.component_service_pb2 import DeleteComponentsResponse
from ..apis.muses.v1.component_service_pb2 import GetComponentRequest
from ..apis.muses.v1.component_service_pb2 import GetComponentResponse
from ..apis.muses.v1.component_service_pb2 import ListComponentsRequest
from ..apis.muses.v1.component_service_pb2 import ListComponentsResponse
from ..apis.muses.v1.component_service_pb2 import UpdateComponentRequest
from ..apis.muses.v1.component_service_pb2 import UpdateComponentResponse
from ..apis.muses.v1.flow_service_pb2 import ComponentParameter
from ..apis.muses.v1.flow_service_pb2 import CreateFlowRequest
from ..apis.muses.v1.flow_service_pb2 import CreateFlowResponse
from ..apis.muses.v1.flow_service_pb2 import DeleteFlowRequest
from ..apis.muses.v1.flow_service_pb2 import DeleteFlowResponse
from ..apis.muses.v1.flow_service_pb2 import DeleteFlowsRequest
from ..apis.muses.v1.flow_service_pb2 import DeleteFlowsResponse
from ..apis.muses.v1.flow_service_pb2 import Flow
from ..apis.muses.v1.flow_service_pb2 import FlowOptionFilter
from ..apis.muses.v1.flow_service_pb2 import GetFlowRequest
from ..apis.muses.v1.flow_service_pb2 import GetFlowResponse
from ..apis.muses.v1.flow_service_pb2 import ListFlowsRequest
from ..apis.muses.v1.flow_service_pb2 import ListFlowsResponse
from ..apis.muses.v1.flow_service_pb2 import Parameter
from ..apis.muses.v1.flow_service_pb2 import UpdateFlowRequest
from ..apis.muses.v1.flow_service_pb2 import UpdateFlowResponse
from ..apis.muses.v1.method_pb2 import Method
from ..apis.muses.v1.method_pb2 import MethodOptionFilter
from ..apis.muses.v1.method_service_pb2 import CreateMethodRequest
from ..apis.muses.v1.method_service_pb2 import CreateMethodResponse
from ..apis.muses.v1.method_service_pb2 import DeleteMethodRequest
from ..apis.muses.v1.method_service_pb2 import DeleteMethodResponse
from ..apis.muses.v1.method_service_pb2 import ListMethodsRequest
from ..apis.muses.v1.method_service_pb2 import ListMethodsResponse
from ..apis.muses.v1.method_service_pb2 import UpdateMethodRequest
from ..apis.muses.v1.method_service_pb2 import UpdateMethodResponse
from ..apis.thirdparty.kfpapi.pipeline_spec_pb2 import ComponentSpec
from ..apis.thirdparty.kfpapi.pipeline_spec_pb2 import PipelineDeploymentConfig
from ..apis.thirdparty.kfpapi.pipeline_spec_pb2 import PipelineSpec
from ..gateway import muses_client
from ..gateway import try_request_grpc
from ..lib import convert_message
from ..lib import read_message

_cmplr: Final[compiler.Compiler] = compiler.Compiler()


class MusesClient:

    @property
    def _stub(self):
        """
        The function returns the client object
        :return: The client object
        """
        return muses_client

    @try_request_grpc
    def create_component(
        self,
        component: Component,
    ) -> CreateComponentResponse:
        request: CreateComponentRequest = CreateComponentRequest(
            component=component, )
        return self._stub.component.CreateComponent(request)

    def create_component_from_file(
        self,
        yaml_path: str,
    ) -> CreateComponentResponse:
        component: Component = read_message(yaml_path, Component)
        return self.create_component(component=component)

    def create_component_from_function(
        self,
        func: Callable,
    ) -> CreateComponentResponse:
        _, filepath = tempfile.mkstemp(suffix=".yaml")
        _cmplr.compile(
            func,
            package_path=filepath,
        )
        return self.create_component_from_kfp_file(yaml_path=filepath)

    @try_request_grpc
    def create_component_from_kfp_file(
        self,
        yaml_path: str,
    ) -> CreateComponentResponse:
        component_spec = components.load_component_from_file(
            yaml_path).component_spec
        name = component_spec.name
        pipe_spec: PipelineSpec = read_message(yaml_path, PipelineSpec)
        component = pipe_spec.components[
            pipe_spec.root.dag.tasks[name].component_ref.name]
        exec_spec: PipelineDeploymentConfig.ExecutorSpec = convert_message(
            pipe_spec.deployment_spec["executors"][component.executor_label],
            PipelineDeploymentConfig.ExecutorSpec,
        )
        request: CreateComponentRequest = CreateComponentRequest(
            component=Component(
                name=name,
                component=component,
                executor_spec=exec_spec,
            ), )
        return self._stub.component.CreateComponent(request)

    @try_request_grpc
    def get_component(
        self,
        id: int,
    ) -> GetComponentResponse:
        return self._stub.component.GetComponent(GetComponentRequest(id=id), )

    @try_request_grpc
    def update_component(
        self,
        component: Component,
    ) -> UpdateComponentResponse:
        return self._stub.component.UpdateComponent(
            UpdateComponentRequest(component=component), )

    @try_request_grpc
    def delete_component(
        self,
        id: int,
    ) -> DeleteComponentResponse:
        return self._stub.component.DeleteComponent(
            DeleteComponentRequest(id=id), )

    @try_request_grpc
    def list_components(
        self,
        common_option: CommonOption = None,
        common_filter: CommonFilter = None,
        option_filter: ComponentOptionFilter = None,
    ) -> ListComponentsResponse:
        return self._stub.component.ListComponents(
            ListComponentsRequest(
                common_option=common_option,
                common_filter=common_filter,
                option_filter=option_filter,
            ), )

    @try_request_grpc
    def delete_components(
        self,
        common_filter: CommonFilter = None,
        option_filter: ComponentOptionFilter = None,
    ) -> DeleteComponentsResponse:
        return self._stub.component.DeleteComponents(
            DeleteComponentsRequest(
                common_filter=common_filter,
                option_filter=option_filter,
            ), )

    @try_request_grpc
    def create_method(
        self,
        m: Method,
    ) -> CreateMethodResponse:
        return self._stub.method.CreateMethod(CreateMethodRequest(
            method=m, ), )

    def create_method_from_file(
        self,
        yaml_path: str,
    ) -> CreateMethodResponse:
        m: Method = read_message(yaml_path, Method)
        return self.create_method(m)

    @try_request_grpc
    def update_method(
        self,
        m: Method,
    ) -> UpdateMethodResponse:
        return self._stub.method.UpdateMethod(UpdateMethodRequest(method=m), )

    @try_request_grpc
    def delete_method(
        self,
        id: int,
    ) -> DeleteMethodResponse:
        return self._stub.method.DeleteMethod(DeleteMethodRequest(id=id), )

    @try_request_grpc
    def list_methods(
        self,
        common_option: CommonOption = None,
        common_filter: CommonFilter = None,
        option_filter: MethodOptionFilter = None,
    ) -> ListMethodsResponse:
        return self._stub.method.ListMethods(
            ListMethodsRequest(
                common_option=common_option,
                common_filter=common_filter,
                option_filter=option_filter,
            ), )

    @try_request_grpc
    def create_flow(
        self,
        flow: Flow,
    ) -> CreateFlowResponse:
        request: CreateFlowRequest = CreateFlowRequest(flow=flow, )
        return self._stub.flow.CreateFlow(request)

    def create_flow_from_file(
        self,
        yaml_path: str,
    ) -> CreateFlowResponse:
        flow: Flow = read_message(yaml_path, Flow)
        return self.create_flow(flow=flow)

    def create_flow_from_function(
        self,
        func: Callable,
    ) -> CreateFlowResponse:
        _, filepath = tempfile.mkstemp(suffix=".yaml")
        _cmplr.compile(
            func,
            package_path=filepath,
        )
        return self.create_flow_from_kfp_file(yaml_path=filepath)

    @try_request_grpc
    def create_flow_from_kfp_file(
        self,
        yaml_path: str,
    ) -> CreateFlowResponse:
        pipe_spec: PipelineSpec = read_message(yaml_path, PipelineSpec)
        deploy_config: PipelineDeploymentConfig = convert_message(
            pipe_spec.deployment_spec,
            PipelineDeploymentConfig,
        )
        comps = []
        parameters = []
        for comp_name, comp in pipe_spec.root.dag.tasks.items():
            for param_name, param in comp.inputs.parameters.items():
                if param.component_input_parameter:
                    # 直接从flow传递的参数
                    parameters.append(
                        Parameter(
                            parameter=ComponentParameter(
                                node_id=comp_name,
                                param_name=param_name,
                            ),
                            parameter_spec=pipe_spec.root.input_definitions.
                            parameters[param.component_input_parameter],
                        ), )
                    continue
                if param.task_output_parameter:
                    parameters.append(
                        Parameter(
                            parameter=ComponentParameter(
                                node_id=comp_name,
                                param_name=param_name,
                            ),
                            parent_parameter=ComponentParameter(
                                node_id=param.task_output_parameter.
                                producer_task,
                                param_name=param.task_output_parameter.
                                output_parameter_key,
                            ),
                        ), )

            component_spec: ComponentSpec = pipe_spec.components[
                comp.component_ref.name]
            executor_spec: PipelineDeploymentConfig.ExecutorSpec = deploy_config.executors[
                component_spec.executor_label]
            comps.append(
                self.create_component(
                    Component(name=comp_name,
                              component=component_spec,
                              executor_spec=executor_spec,
                              node_id=comp_name)).details)

        request: CreateFlowRequest = CreateFlowRequest(flow=Flow(
            name=pipe_spec.pipeline_info.name,
            parameters=parameters,
            components={c.node_id: c
                        for c in comps},
        ), )
        return self._stub.flow.CreateFlow(request)

    @try_request_grpc
    def get_flow(
        self,
        id: int,
    ) -> GetFlowResponse:
        return self._stub.flow.GetFlow(GetFlowRequest(id=id), )

    @try_request_grpc
    def update_flow(
        self,
        flow: Flow,
    ) -> UpdateFlowResponse:
        return self._stub.flow.UpdateFlow(UpdateFlowRequest(flow=flow), )

    @try_request_grpc
    def delete_flow(
        self,
        id: int,
    ) -> DeleteFlowResponse:
        return self._stub.flow.DeleteFlow(DeleteFlowRequest(id=id), )

    @try_request_grpc
    def list_flows(
        self,
        common_option: CommonOption = None,
        common_filter: CommonFilter = None,
        option_filter: FlowOptionFilter = None,
    ) -> ListFlowsResponse:
        return self._stub.flow.ListFlows(
            ListFlowsRequest(
                common_option=common_option,
                common_filter=common_filter,
                option_filter=option_filter,
            ), )

    @try_request_grpc
    def delete_flows(
        self,
        common_filter: CommonFilter = None,
        option_filter: FlowOptionFilter = None,
    ) -> DeleteFlowsResponse:
        return self._stub.flow.DeleteFlows(
            DeleteFlowsRequest(
                common_filter=common_filter,
                option_filter=option_filter,
            ), )
