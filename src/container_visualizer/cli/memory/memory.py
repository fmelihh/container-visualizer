import time
import plotext as plt
import json
import click
import docker
import pendulum
from src.container_visualizer.cli.cli import app
from ...plots import line_chart


@click.command()
@click.option('--container-id', required=True, default=None, help="lists the memory usage of only the container with "
                                                                  "the given ID.")
@click.option('--unit', default="gigabyte", help="Output unit for computation. Gigabyte and byte are among the "
                                                 "available commands")
def memory_usage(container_id, unit):
    if container_id is None:
        click.echo("container id cannot be empty")

    client = docker.from_env()
    selected_container = client.containers.get(container_id)

    x_axis_lower_limit = pendulum.now()
    for idx, stat in enumerate(selected_container.stats(stream=True)):
        stat = json.loads(stat)
        usage = stat['memory_stats']['usage']
        limit = stat['memory_stats']['limit']

        if unit == "gigabyte":
            usage = round(usage / (1024**3), 2)
            limit = round(limit / (1024**3), 2)

        line_chart(
            title="Memory Usage",
            x_axis=[pendulum.now().format("HH:mm:ss")],
            y_axis=[usage],
            date_form=["H:M:S", "H:M:S"],
            x_axis_lower_limit=x_axis_lower_limit.format("HH:mm:ss"),
            x_axis_upper_limit=x_axis_lower_limit.add(seconds=10 * (idx + 1)).format("HH:mm:ss"),
            y_axis_lower_limit=0,
            y_axis_upper_limit=limit
        )


app.add_command(memory_usage)
