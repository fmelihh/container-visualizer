import click
import docker
from cmd.cli import app


@click.command()
@click.option('--container-id', default=None, help="lists the memory usage of only the container with the given ID.")
@click.option('--unit', default="gigabyte", help="Output unit for computation. Gigabyte and byte are among the "
                                                 "available commands")
def memory_usage(container_id, unit):
    if container_id is None:
        click.echo("container id cannot be empty")

    client = docker.from_env()
    selected_container = client.containers.get(container_id)
    stats = selected_container.stats(stream=False)

    usage = stats['memory_stats']['usage']
    limit = stats['memory_stats']['limit']

    if unit == "gigabyte":
        usage = round(usage / (1024**3), 2)
        limit = round(limit / (1024**3), 2)

    click.echo(f"Memory usage for container {selected_container.id}: {usage}/{limit} {unit}")


app.add_command(memory_usage)
