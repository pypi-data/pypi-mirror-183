from dataclasses import dataclass, field, asdict
import requests
from datetime import datetime
import click
import sys
from typing import Dict
import uuid
from stochasticx.constants.urls import CloudRoutes, get_cloud_url
from stochasticx.utils.auth_utils import AuthUtils
from stochasticx.models.models import OptimizedModel, Models
from stochasticx.utils.logging import configure_logger
from stochasticx.utils.parse_utils import parse_date
from stochasticx.utils.stat_controller import (
    StatController,
    LocalDeploymentJobInformation,
)
from stochasticx.utils.preferences import Preferences


logger = configure_logger(__name__)


class LocalDeploymentsClient:
    @staticmethod
    def get_deployments(fmt="table"):
        preferences = Preferences.load()
        response = requests.get(f"{preferences.local_deployment_url}/models")
        response.raise_for_status()

        models = response.json()
        model_results = []

        for model in models:
            model_results.append(
                LocalDeployment(
                    id=model.get("id"),
                    model_name=model.get("model_name"),
                    type=model.get("type"),
                    cuda=model.get("cuda"),
                    task_type=model.get("task_type"),
                    user_params=model.get("user_params"),
                )
            )

        if fmt == "table":
            columns = []
            values = []

            if len(model_results) > 0:
                columns, _ = model_results[0].to_table()

            for model in model_results:
                _, vals = model.to_table()
                values.append(vals)

            return columns, values
        else:
            return model_results

    @staticmethod
    def get_deployment_by_id(id):
        deployments = LocalDeploymentsClient.get_deployments(fmt=None)

        for deployment in deployments:
            if deployment.id == id:
                return deployment

        return None

    @staticmethod
    def delete_deployment(model_type, model_name):
        preferences = Preferences.load()
        response = requests.delete(
            "{}/model/{}/{}".format(
                preferences.local_deployment_url, model_type, model_name
            )
        )
        response.raise_for_status()


@dataclass
class LocalDeployment:
    model_name: str
    type: str
    cuda: bool
    task_type: str
    user_params: Dict
    id: str = None

    def to_table(self):
        columns = [
            "Model ID",
            "Model name",
            "Model type",
            "CUDA",
            "Task type",
            "User params",
        ]

        values = [
            str(self.id),
            self.model_name,
            self.type,
            str(self.cuda),
            self.task_type,
            str(self.user_params),
        ]

        return columns, values


@dataclass
class LocalSequenceClassificationDeployment(LocalDeployment):
    task_type: str = "sequence_classification"
    user_params: Dict = field(
        default_factory=lambda: {"max_batch_size": 8, "max_seq_length": 128}
    )

    def start_deployment(self):
        preferences = Preferences.load()
        response = requests.post(
            f"{preferences.local_deployment_url}/model", json=asdict(self)
        )

        response.raise_for_status()

        StatController.add_information(
            LocalDeploymentJobInformation(
                deployment_type=self.task_type,
                model_name=self.model_name,
                type=self.type,
                params=self.user_params,
                job_result=response.json(),
            )
        )


@dataclass
class LocalQuestionAnsweringDeployment(LocalDeployment):
    task_type: str = "question_answering"
    user_params: Dict = field(
        default_factory=lambda: {
            "max_batch_size": 8,
            "max_seq_length": 256,
            "stride": 30,
        }
    )

    def start_deployment(self):
        preferences = Preferences.load()
        response = requests.post(
            f"{preferences.local_deployment_url}/model", json=asdict(self)
        )

        response.raise_for_status()

        StatController.add_information(
            LocalDeploymentJobInformation(
                deployment_type=self.task_type,
                model_name=self.model_name,
                type=self.type,
                params=self.user_params,
                job_result=response.json(),
            )
        )


@dataclass
class LocalTokenClassificationDeployment(LocalDeployment):
    task_type: str = "token_classification"
    user_params: Dict = field(
        default_factory=lambda: {"max_seq_length": 256, "label_all_tokens": False}
    )

    def start_deployment(self):
        preferences = Preferences.load()
        response = requests.post(
            f"{preferences.local_deployment_url}", json=asdict(self)
        )

        response.raise_for_status()

        StatController.add_information(
            LocalDeploymentJobInformation(
                deployment_type=self.task_type,
                model_name=self.model_name,
                type=self.type,
                params=self.user_params,
                job_result=response.json(),
            )
        )


@dataclass
class LocalTranslationDeployment(LocalDeployment):
    task_type: str = "translation"
    user_params: Dict = field(
        default_factory=lambda: {
            "max_source_length": 256,
            "max_target_length": 256,
            "src_lang": "en",
            "tgt_lang": "es",
            "pad_to_max_length": False,
            "num_beams": 4,
            "ignore_pad_token_for_loss": True,
            "source_prefix": "",
            "forced_bos_token": None,
        }
    )

    def start_deployment(self):
        preferences = Preferences.load()
        response = requests.post(
            f"{preferences.local_deployment_url}/model", json=asdict(self)
        )

        response.raise_for_status()

        StatController.add_information(
            LocalDeploymentJobInformation(
                deployment_type=self.task_type,
                model_name=self.model_name,
                type=self.type,
                params=self.user_params,
                job_result=response.json(),
            )
        )


@dataclass
class LocalSummarizationDeployment(LocalDeployment):
    task_type: str = "summarization"
    user_params: Dict = field(
        default_factory=lambda: {
            "max_source_length": 256,
            "max_target_length": 64,
            "lang": "en",
            "pad_to_max_length": False,
            "num_beams": 4,
            "ignore_pad_token_for_loss": True,
            "source_prefix": "",
            "forced_bos_token": None,
        }
    )

    def start_deployment(self):
        preferences = Preferences.load()
        response = requests.post(
            f"{preferences.local_deployment_url}/model", json=asdict(self)
        )

        response.raise_for_status()

        StatController.add_information(
            LocalDeploymentJobInformation(
                deployment_type=self.task_type,
                model_name=self.model_name,
                type=self.type,
                params=self.user_params,
                job_result=response.json(),
            )
        )


@dataclass
class LocalTextGenerationDeployment(LocalDeployment):
    task_type: str = "text_generation"
    user_params: Dict = field(default_factory=lambda: {"block_size": 256})

    def start_deployment(self):
        preferences = Preferences.load()
        response = requests.post(
            f"{preferences.local_deployment_url}/model", json=asdict(self)
        )

        response.raise_for_status()

        StatController.add_information(
            LocalDeploymentJobInformation(
                deployment_type=self.task_type,
                model_name=self.model_name,
                type=self.type,
                params=self.user_params,
                job_result=response.json(),
            )
        )


class InferenceTaskType:
    def __init__(self):
        pass

    def return_parameters(self):
        raise NotImplementedError()


class SequenceClassificationInfTask(InferenceTaskType):
    def __init__(self, max_batch_size=8, max_seq_length=128):
        self.max_batch_size = max_batch_size
        self.max_seq_length = max_seq_length

    def return_parameters(self):
        return {
            "max_batch_size": self.max_batch_size,
            "max_seq_length": self.max_seq_length,
        }


class QuestionAnsweringInfTask(InferenceTaskType):
    def __init__(self, max_batch_size=8, max_seq_length=128):
        self.max_batch_size = max_batch_size
        self.max_seq_length = max_seq_length

    def return_parameters(self):
        return {
            "max_batch_size": self.max_batch_size,
            "max_seq_length": self.max_seq_length,
        }


class SummarizationInfTask(InferenceTaskType):
    def __init__(
        self, max_batch_size=8, max_source_length=128, source_prefix="", lang="en"
    ):
        self.max_batch_size = max_batch_size
        self.max_source_length = max_source_length
        self.source_prefix = source_prefix
        self.lang = lang

    def return_parameters(self):
        return {
            "max_batch_size": self.max_batch_size,
            "max_source_length": self.max_source_length,
            "source_prefix": self.source_prefix,
            "lang": self.lang,
        }


class TranslationInfTask(InferenceTaskType):
    def __init__(
        self,
        max_batch_size=8,
        max_source_length=128,
        source_prefix="",
        src_lang="en",
        tgt_lang="de",
    ):
        self.max_batch_size = max_batch_size
        self.max_source_length = max_source_length
        self.source_prefix = source_prefix
        self.src_lang = src_lang
        self.tgt_lang = tgt_lang

    def return_parameters(self):
        return {
            "max_batch_size": self.max_batch_size,
            "max_source_length": self.max_source_length,
            "source_prefix": self.source_prefix,
            "src_lang": self.src_lang,
            "tgt_lang": self.tgt_lang,
        }


class TokenClassificationInfTask(InferenceTaskType):
    def __init__(self, max_batch_size=8, max_seq_length=128):
        self.max_batch_size = max_batch_size
        self.max_seq_length = max_seq_length

    def return_parameters(self):
        return {
            "max_batch_size": self.max_batch_size,
            "max_seq_length": self.max_seq_length,
        }


class InstanceTypes:
    g4dn_xlarge = "g4dn.xlarge"
    c5_2xlarge = "c5.2xlarge"
    c5_12xlarge = "c5.12xlarge"


class Instance:
    def __init__(
        self,
        id,
        name,
        cost_per_hour,
        cost_per_month,
        spot_cost,
        storage,
        vcpus,
        memory,
        network,
    ):
        self.id = id
        self.name = name
        self.cost_per_hour = cost_per_hour
        self.cost_per_month = cost_per_month
        self.spot_cost = spot_cost
        self.storage = storage
        self.vcpus = vcpus
        self.memory = memory
        self.network = network

    def to_table(self):
        columns = [
            "Id",
            "Name",
            "Cost/hour",
            "Cost/month",
            "Spot cost",
            "Storage",
            "vCPUs",
            "Memory",
            "Network",
        ]

        values = [
            self.id,
            self.name,
            self.cost_per_hour,
            self.cost_per_month,
            self.spot_cost,
            self.storage,
            self.vcpus,
            self.memory,
            self.network,
        ]

        return columns, values

    def __str__(self):
        return "ID: {} ; Name: {} ; Cost/hour: {} ; Cost/month: {} ; Spot cost: {} ; Storage: {} ; vCPUs: {} ; Memory: {} ; Network: {}".format(
            self.id,
            self.name,
            self.cost_per_hour,
            self.cost_per_month,
            self.spot_cost,
            self.storage,
            self.vcpus,
            self.memory,
            self.network,
        )


class Deployment:
    def __init__(self):
        pass

    def populate_data(
        self,
        id,
        task_type,
        created_at,
        instance,
        optimized_model,
        status,
        parameters,
        start,
        end,
        endpoint=None,
        api_key=None,
    ):
        self.id = id
        self.task_type = task_type
        self.created_at = created_at
        self.instance = instance
        self.optimized_model = optimized_model
        self.status = status
        self.parameters = parameters

        self.start = None
        if start is not None:
            self.start = datetime.utcfromtimestamp(int(start)).strftime(
                "%Y-%m-%d %H:%M:%S"
            )

        self.end = None
        if end is not None:
            self.end = datetime.utcfromtimestamp(int(end)).strftime("%Y-%m-%d %H:%M:%S")

        self.endpoint = endpoint
        self.api_key = api_key

    def get_endpoint(self):
        self.sync()
        return self.endpoint

    def get_api_key(self):
        self.sync()
        return self.api_key

    def sync(self):
        synced_deployment = Deployments.get_deployment(self.id)
        self.task_type = synced_deployment.task_type
        self.created_at = synced_deployment.created_at
        self.instance = synced_deployment.instance
        self.optimized_model = synced_deployment.optimized_model
        self.parameters = synced_deployment.parameters
        self.endpoint = synced_deployment.endpoint
        self.api_key = synced_deployment.api_key
        self.start = synced_deployment.start
        self.end = synced_deployment.end
        self.status = synced_deployment.status

    def get_status(self):
        self.sync()
        return self.status

    def get_instance(self):
        self.sync()
        return self.instance

    def get_optimized_model(self):
        self.sync()
        return self.optimized_model

    def get_task_type(self):
        self.sync()
        return self.task_type

    def get_id(self):
        return self.id

    def start_inference(
        self, model, task_type, instance_type=InstanceTypes.g4dn_xlarge
    ):
        auth_header = AuthUtils.get_auth_headers()
        r = requests.post(
            get_cloud_url(CloudRoutes.DEPLOYMENT_URL),
            headers=auth_header,
            json={
                "modelId": model.id,
                "instanceType": instance_type,
                "userParams": task_type.return_parameters(),
            },
        )
        r.raise_for_status()
        self.id = r.json().get("data").get("id")

    def delete(self):
        if self.get_status() == "running":
            url = get_cloud_url(CloudRoutes.DEPLOYMENT_URL.formatting(self.id))

            auth_header = AuthUtils.get_auth_headers()
            r = requests.delete(url, headers=auth_header)
            r.raise_for_status()
        else:
            logger.warning("You cannot delete a deployment until it is running")

    def to_table(self):
        columns = ["Id", "Created at", "Status", "Parameters", "Start", "End"]

        values = [
            self.id,
            parse_date(self.created_at),
            self.status,
            str(self.parameters),
            self.start,
            self.end,
        ]

        return columns, values

    def __str__(self):
        return "ID: {} ; Created at: {} ; Status: {}; Parameters: {} ; Start: {} ; End: {}".format(
            self.id,
            parse_date(self.created_at),
            self.status,
            self.parameters,
            self.start,
            self.end,
        )


class Instances:
    @staticmethod
    def get_instance_types(fmt=None):
        instances = []

        auth_header = AuthUtils.get_auth_headers()
        r = requests.get(get_cloud_url(CloudRoutes.INSTANCES_URL), headers=auth_header)
        r.raise_for_status()

        data = r.json()

        if data.get("ec2Instances") is not None:
            for instance_data in data["ec2Instances"]:
                instance = Instance(
                    id=instance_data["id"],
                    name=instance_data["instanceType"],
                    cost_per_hour=instance_data["hourlyCost"],
                    memory=instance_data["memory"],
                    cost_per_month=instance_data["monthlyCost"],
                    network=instance_data["network"],
                    spot_cost=instance_data["spotCost"],
                    storage=instance_data["storage"],
                    vcpus=instance_data["vcpus"],
                )

                instances.append(instance)

            if fmt == "table":
                columns = []
                values = []

                if len(instances) > 0:
                    columns, _ = instances[0].to_table()

                for instance in instances:
                    _, vals = instance.to_table()
                    values.append(vals)

                return columns, values

        return instances

    @staticmethod
    def get_instance_type_by_name(name):
        instances = Instances.get_instance_types()

        for instance in instances:
            if instance.name == name:
                return instance


class DeploymentUtils:
    @staticmethod
    def create_deployment(deployment_data):
        optimized_model_id = deployment_data["model"]["id"]
        optimized_model = Models.get_optimized_model(optimized_model_id)

        instance_data = deployment_data.get("instance")

        instance = None
        if instance_data is not None:
            instance = Instance(
                id=instance_data["id"],
                name=instance_data["instanceType"],
                cost_per_hour=instance_data["hourlyCost"],
                memory=instance_data["memory"],
                cost_per_month=instance_data["monthlyCost"],
                network=instance_data["network"],
                spot_cost=instance_data["spotCost"],
                storage=instance_data["storage"],
                vcpus=instance_data["vcpus"],
            )

        start = None
        end = None
        if deployment_data.get("utilization") is not None:
            start = deployment_data["utilization"].get("start")
            end = deployment_data["utilization"].get("end")

        endpoint = None
        api_key = None
        resources = deployment_data.get("resources")
        if resources is not None:
            endpoint = INFERENCE_URL + resources.get("route")[2:]
            api_key = resources.get("apiKey")

        deployment = Deployment()
        deployment.populate_data(
            id=deployment_data["id"],
            task_type=deployment_data["job"]["taskType"],
            created_at=deployment_data["createdAt"],
            instance=instance,
            optimized_model=optimized_model,
            status=deployment_data["status"],
            parameters=deployment_data["userParams"],
            start=start,
            end=end,
            endpoint=endpoint,
            api_key=api_key,
        )

        return deployment


class StableDiffusionDeployment:
    def __init__(self, id, status, model_name, api_key=None, client_url=None):
        self.id = id
        self.status = status
        self.model_name = model_name
        self.api_key = api_key
        self.client_url = client_url

    def __str__(self):
        return (
            "ID: {} ; Status: {} ; Model name: {} ; API key: {} ; Endpoint: {}".format(
                self.id, self.status, self.model_name, self.api_key, self.client_url
            )
        )


class StableDiffusionDeployments:
    @staticmethod
    def get_deployments():
        deployments = []

        auth_header = AuthUtils.get_auth_headers()
        r = requests.get(
            get_cloud_url(CloudRoutes.STABLE_DIFFUSION_URL), headers=auth_header
        )
        r.raise_for_status()

        data = r.json()
        deploying = False

        if data["data"] is not None:
            for deployment_data in data["data"]:

                api_key = None
                client_url = None
                if deployment_data.get("resources") is not None:
                    api_key = deployment_data.get("resources").get("apiKey")
                    client_url = deployment_data.get("clientUrl")
                else:
                    deploying = True

                deployment = StableDiffusionDeployment(
                    id=deployment_data.get("id"),
                    status=deployment_data.get("status"),
                    model_name=deployment_data.get("modelName"),
                    client_url=client_url,
                    api_key=api_key,
                )
                deployments.append(deployment)

        if deploying:
            click.secho(
                "[+] There are models that are still deploying. It can take some minutes...\n",
                bold=True,
                fg="yellow",
            )

        return deployments

    @staticmethod
    def get_deployment(id):
        url = get_cloud_url(CloudRoutes.STABLE_DIFFUSION_URL.formating(id))

        auth_header = AuthUtils.get_auth_headers()
        r = requests.get(url, headers=auth_header)

        try:
            r.raise_for_status()
        except:
            click.secho("[+] The ID is not correct\n", bold=True, fg="yellow")
            sys.exit()

        data = r.json()
        deployment_data = data["deployedModel"]
        if deployment_data is not None:
            if deployment_data.get("resources") is not None:
                api_key = deployment_data.get("resources").get("apiKey")
                client_url = deployment_data.get("clientUrl")

                deployment = StableDiffusionDeployment(
                    id=deployment_data.get("_id"),
                    status=deployment_data.get("status"),
                    model_name=deployment_data.get("modelName"),
                    client_url=client_url,
                    api_key=api_key,
                )
            else:
                deployment = StableDiffusionDeployment(
                    id=deployment_data.get("_id"),
                    status=deployment_data.get("status"),
                    model_name=deployment_data.get("modelName"),
                )

                click.secho(
                    "[+] The model is still deploying. It can take some minutes...",
                    bold=True,
                    color="yellow",
                )

            return deployment

        return None

    @staticmethod
    def deploy():
        auth_header = AuthUtils.get_auth_headers()
        r = requests.post(
            get_cloud_url(CloudRoutes.STABLE_DIFFUSION_URL),
            headers=auth_header,
            json={"name": "Stable-Diffusion-{}".format(uuid.uuid4())},
        )
        r.raise_for_status()

    @staticmethod
    def delete(id):
        url = get_cloud_url(CloudRoutes.STABLE_DIFFUSION_URL.formating(id))
        auth_header = AuthUtils.get_auth_headers()
        r = requests.delete(url, headers=auth_header)
        r.raise_for_status()


class Deployments:
    @staticmethod
    def get_deployments(fmt=None):
        deployments = []

        auth_header = AuthUtils.get_auth_headers()
        r = requests.get(get_cloud_url(CloudRoutes.DEPLOYMENT_URL), headers=auth_header)
        r.raise_for_status()

        data = r.json()

        if data["data"] is not None:
            for deployment_data in data["data"]:
                deployment = DeploymentUtils.create_deployment(deployment_data)
                deployments.append(deployment)

            if fmt == "table":
                columns = []
                values = []

                if len(deployments) > 0:
                    columns, _ = deployments[0].to_table()

                for deployment in deployments:
                    _, vals = deployment.to_table()
                    values.append(vals)

                return columns, values

        return deployments

    @staticmethod
    def get_deployment(id):
        url = get_cloud_url(CloudRoutes.DEPLOYMENT_URL.formatting(id))

        auth_header = AuthUtils.get_auth_headers()
        r = requests.get(url, headers=auth_header)
        r.raise_for_status()

        data = r.json()
        deployment_data = data["deployedModel"]
        if deployment_data is not None:
            deployment = DeploymentUtils.create_deployment(deployment_data)
            return deployment

        return None
