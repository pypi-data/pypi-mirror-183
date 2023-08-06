from __future__ import annotations
from typing import List, Optional, Any

from continual.rpc.management.v1 import management_pb2
from continual.rpc.management.v1 import types
from continual.python.sdk.resource import Resource
from continual.python.sdk.manager import Manager
from continual.python.sdk.iterators import Pager


class MetricsManager(Manager):
    """Manages metric resources."""

    name_pattern: str = "projects/{project}/environments/{environment}/models/{model}/model_versions/{version}/metrics/{metric}"

    def create(
        self,
        key: str,
        value: Any,
        direction: str,
        group_name: str = "",
        description: str = "",
        step: int = 0,
    ) -> Metric:
        """Create a Metric.

        Arguments:
            key: identifier for the metric (e.g. "accuracy")
            value: value of the metric
            direction: direction of the metric (e.g. "HIGHER")
            group_name: name of the group to which this metric belongs (e.g. "train")
            description: description of the metric
            step: step at which the metric was logged, allows metrics to be grouped into a sequence

        Returns:
            A new metric.

        Examples:
            >>> ... # Assume client, project, and environment are defined.
            >>> env = project.environments.get("my_environment")
            >>> run = env.runs.create("my_run")
            >>> model = run.models.create(display_name="my_model", description="Customer churn model")
            >>> model_version = model.model_versions.create()
            >>> model_version.metrics.create(key="accuracy", value=0.9, direction="HIGHER", group_name="train")
            <Metric object {'name': 'projects/test_project_1/environments/test_env/models/test_model/versions/cegl9qq5lsrkc0osu0ug/metrics/cegl9u25lsrkc0osu100',
            'key': 'accuracy', 'run_name': 'projects/test_project_1/environments/test_env/runs/test_run', 'value': 0.9, 'create_time': '2022-12-20T06:23:52.671047Z',
            'update_time': '2022-12-20T06:23:52.671047Z', 'group_name': 'train', 'description': '', 'direction': 'HIGHER', 'step': '0'}>
        """
        req = management_pb2.CreateMetricRequest(
            parent=self.parent,
            metric=Metric(
                key=key,
                value=float(value) if isinstance(value, int) else value,
                direction=direction,
                group_name=group_name,
                description=description,
                step=step,
                run_name=self.run_name,
            ).to_proto(),
        )

        resp = self.client._management.CreateMetric(req)
        return Metric.from_proto(resp, client=self.client)

    def get(
        self, name: str = "", key: str = "", group_name: str = "", step: int = 0
    ) -> Metric:
        """Get metric.

        Arguments:
            name: Metric name or id.
            key: Metric key.
            group_name: Metric group name.
            step: Metric step for sequences.

        Returns
            A Metric.

        Examples:
            >>> ... # Assume client, project, and environment are defined.
            >>> env = project.environments.get("my_environment")
            >>> run = env.runs.create("my_run")
            >>> model = run.models.create(display_name="my_model", description="Customer churn model")
            >>> model_version = model.model_versions.create()
            >>> metric_keys = ['accuracy', 'precision', 'recall']
            >>> metrics = [model_version.metrics.create(key=key, value=0.9, direction="HIGHER", group_name="train") for key in metric_keys]
            >>> model_version.metrics.get(name=metrics[1].name).key                     # get by name
            'precision'
            >>> model_version.metrics.get(key="accuracy", group_name="train").key       # get by key and group_name
            'accuracy'
        """

        req = management_pb2.GetMetricRequest(
            parent=self.parent,
            name=name,
            key=key,
            group_name=group_name,
            step=step,
        )
        metric = self.client._management.GetMetric(req)
        return Metric.from_proto(metric, client=self.client)

    def list(
        self,
        page_size: Optional[int] = None,
        order_by: str = None,
        latest: bool = True,
    ) -> List[Metric]:
        """List metrics.

        Arguments:
            page_size: Number of items to return.
            order_by: A string field name used to order list.
            latest: If true, the results are sorted in descending order, else ascending.

        Returns:
            A list of metrics.

        Examples:
            >>> ... # Assume client, project, and environment are defined.
            >>> env = project.environments.get("my_environment")
            >>> run = env.runs.create("my_run")
            >>> model = run.models.create(display_name="my_model", description="Customer churn model")
            >>> model_version = model.model_versions.create()
            >>> metric_keys = ['accuracy', 'precision', 'recall']
            >>> metrics = [model_version.metrics.create(key=key, value=0.9, direction="HIGHER", group_name="train") for key in metric_keys]
            >>> [m.key for m in model_version.metrics.list(page_size=3)]
            ['recall', 'precision', 'accuracy']
            >>> [m.key for m in model_version.metrics.list(page_size=3, order_by="key", latest=False)]
            ['accuracy', 'precision', 'recall']
        """
        req = management_pb2.ListMetricsRequest(
            parent=self.parent,
            page_size=page_size,
            order_by=order_by,
            latest=latest,
        )
        resp = self.client._management.ListMetrics(req)
        return [Metric.from_proto(x, client=self.client) for x in resp.metrics]

    def list_all(self) -> Pager[Metric]:
        """List all metrics.

        Pages through all metrics using an iterator.

        Returns:
            A iterator of all metrics.

        Examples:
            >>> ... # Assume client, project, and environment are defined.
            >>> env = project.environments.get("my_environment")
            >>> run = env.runs.create("my_run")
            >>> model = run.models.create(display_name="my_model", description="Customer churn model")
            >>> model_version = model.model_versions.create()
            >>> metric_keys = ['accuracy', 'precision', 'recall']
            >>> metrics = [model_version.metrics.create(key=key, value=0.9, direction="HIGHER", group_name="train") for key in metric_keys]
            >>> [m.key for m in model_version.metrics.list_all()]
            ['accuracy', 'precision', 'recall']
        """

        def next_page(next_page_token):
            req = management_pb2.ListMetricsRequest(
                parent=self.parent, page_token=next_page_token
            )
            resp = self.client._management.ListMetrics(req)
            return (
                [Metric.from_proto(x, client=self.client) for x in resp.metrics],
                resp.next_page_token,
            )

        return Pager(next_page)

    # def delete(self, id: str) -> None:
    #     """Delete a metric.

    #     Arguments:
    #         id: Metric name or id.

    #     Examples:
    #         >>> ... # Assume client, project, and environment are defined.
    #         >>> env = project.environments.get("my_environment")
    #         >>> run = env.runs.create("my_run")
    #         >>> model = run.models.create(display_name="my_model", description="Customer churn model")
    #         >>> model_version = model.model_versions.create()
    #         >>> metric_keys = ['accuracy', 'precision', 'recall']
    #         >>> metrics = [model_version.metrics.create(key=key, value=0.9, direction="HIGHER", group_name="train") for key in metric_keys]
    #         >>> len(list(model_version.metrics.list_all()))
    #         3
    #         >>> model_version.metrics.delete(id=metrics[0].id)
    #     """

    #     req = management_pb2.DeleteMetricRequest(name=self.name(id))
    #     self.client._management.DeleteMetric(req)


class Metric(Resource, types.Metric):
    """Metric resource."""

    name_pattern: str = "projects/{project}/environments/{environment}/models/{model}/model_versions/{version}/metrics/{metric}"
    _manager: MetricsManager
    """Metrics manager."""

    def _init(self):
        self._manager = MetricsManager(parent=self.parent, client=self.client)
