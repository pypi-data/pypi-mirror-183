import inspect
import json
import rich
from invoke import task
from git import Repo

if not hasattr(inspect, "getargspec"):
    inspect.getargspec = inspect.getfullargspec


def changed_models():

    from pathlib import Path

    repo = Repo()
    hcommit = repo.head.commit

    changed_models = []

    for diff in hcommit.diff("main"):
        if ".sql" in diff.a_path and "models" in diff.a_path:
            p = Path(diff.a_path)
            changed_models.append(p.stem)

    return changed_models


@task
def model_diff(c):

    from rich.columns import Columns
    from rich import print

    diff_column = Columns(changed_models())

    print(diff_column)


@task
def important_models(c, top=10):

    import networkx as nx
    from rich.console import Console
    from rich.table import Table

    G = nx.DiGraph()

    with c.cd("dbt/adw"):
        cmd = f"dbt ls --resource-type=model --output=json"
        result = c.run(cmd, hide=True, warn=True)

    out = list(result.stdout.split("\n"))

    for stringout in out:
        if stringout == "":
            continue
        parsed_json = json.loads(stringout)
        G.add_node(parsed_json["name"])

    for stringout in out:
        if stringout == "":
            continue
        parsed_json = json.loads(stringout)
        deps_on = list(
            map(lambda i: i.split(".").pop(), parsed_json["depends_on"]["nodes"])
        )
        edge_list = [(parsed_json["name"], i) for i in deps_on]
        G.add_edges_from(edge_list)

    node_importance = sorted(G.in_degree, key=lambda x: x[1], reverse=True)

    table = Table(
        title="Model Importance",
        caption="Models which more models depend on are considered more important.",
    )

    table.add_column("Model Name", style="magenta")
    table.add_column("Dependances", justify="right", style="green")

    for model_name, num_of_deps in node_importance[0:top]:

        table.add_row(model_name, str(num_of_deps))

    console = Console()
    console.print(table)


@task
def visualise(c, model="products"):

    import networkx as nx

    G = nx.DiGraph()

    model_list = changed_models()

    parent = model

    with c.cd("dbt/adw"):
        cmd = f"dbt ls --resource-type=model --select {parent}+ --output=json"
        result = c.run(cmd, hide=True, warn=True)

    out = list(result.stdout.split("\n"))

    for stringout in out:
        if stringout == "":
            continue
        parsed_json = json.loads(stringout)
        if parsed_json["name"] == parent:
            G.add_node(parsed_json["name"], color="red")
        else:
            G.add_node(parsed_json["name"])

    for stringout in out:
        if stringout == "":
            continue
        parsed_json = json.loads(stringout)
        deps_on = list(
            map(lambda i: i.split(".").pop(), parsed_json["depends_on"]["nodes"])
        )
        edge_list = [(parsed_json["name"], i) for i in deps_on]
        G.add_edges_from(edge_list)

    from pyvis.network import Network

    net = Network(notebook=True)

    net.show_buttons()

    net.from_nx(G)

    net.toggle_physics(False)

    net.show("example.html")


@task
def list_deps(c, model="referrals"):

    from rich.columns import Columns
    from rich import print

    parent = model

    with c.cd("dbt/adw"):
        cmd = f"dbt ls --resource-type=model --select {parent}+ --output=json"
        result = c.run(cmd, hide=True, warn=True)

    out = list(result.stdout.split("\n"))

    generated = set([parent])
    to_clone = set()

    for stringout in out:
        if stringout == "":
            continue
        parsed_json = json.loads(stringout)
        deps_on = set(
            map(lambda i: i.split(".").pop(), parsed_json["depends_on"]["nodes"])
        )

        model_name = parsed_json["name"]

        if model_name == parent:
            new_clones = deps_on - generated
            to_clone.update(new_clones)

        if parent in deps_on:
            # This model will have to be regenerated since it relies on the
            # parent (changed) model.
            generated.add(model_name)

            # Get the new parents which will have to be cloned,
            # which is all the dependancies minus the ones we are
            # going to generate.
            new_clones = deps_on - generated
            to_clone.update(new_clones)

    models = {}
    with c.cd("dbt/adw"):
        models_str = " ".join(to_clone)
        cmd = f"dbt ls --resource-type=model --select {models_str} --output=json"
        result = c.run(cmd, hide=True, warn=True)
        out = list(result.stdout.split("\n"))
        for stringout in out:
            if stringout == "":
                continue
            parsed_json = json.loads(stringout)
            material_type = parsed_json["config"]["materialized"]
            model_name = parsed_json["name"]
            models[model_name] = material_type

    

    print(models)
