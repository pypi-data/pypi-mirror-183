import json


class DashboardFactory:
    def __init__(self, time_range: str = '-P3H'):
        self.widget_template = {'start': time_range, 'widgets': []}

    def get_dashboard_body(self):
        return json.dumps(self.widget_template)

    def _add_metric_widget(self, x: int, y: int, instance_id: str, label: str, namespace: str, metric: str, width: int = 24, height: int = 6):
        widget = {
            "type": "metric",
            "x": x,
            "y": y,
            "width": width,
            "height": height,
            "properties": {
                "region": "ap-southeast-1",
                "view": "timeSeries",
                "stacked": False,
                "metrics": [[namespace, metric, "InstanceId", instance_id]],
                "title": label}
        }
        return widget

    def add_cpu_widget(self, x: int, y: int, instance_id: str, label: str, width: int = 24, height: int = 6, cw_namespace: str = "AWS/EC2"):
        widget = self._add_metric_widget(
            x, y, instance_id, label, cw_namespace, "CPUUtilization", width, height)
        self.widget_template['widgets'].append(widget)

    def add_mem_widget(self, x: int, y: int, instance_id: str, label: str, width: int = 24, height: int = 6, cw_namespace: str = 'CWAgent'):
        widget = self._add_metric_widget(
            x, y, instance_id, label, cw_namespace, "Memory % Committed Bytes In Use", width, height)
        self.widget_template['widgets'].append(widget)

    def add_disk_space_widget(self, x: int, y: int, instance_id: str, label: str, width: int = 24, height: int = 6, cw_namespace: str = 'CWAgent'):
        widget = self._add_metric_widget(
            x, y, instance_id, label, cw_namespace, "LogicalDisk % Free Space", width, height)
        self.widget_template['widgets'].append(widget)
