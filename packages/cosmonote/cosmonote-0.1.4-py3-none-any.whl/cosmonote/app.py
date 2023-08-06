import click
from clickmod import ClickModApp
from clickmod_auth import build_token
from rich.table import Table
from rich.markdown import Markdown
from rich.panel import Panel
from rich import box
from rich.columns import Columns

from .notes import parse_note
from .utils import format_time, format_uuid, parse_uuid


app = ClickModApp("cosmonote", domain="https://cosmonote.dev")


@app.main.group()
def notes():
    pass


@notes.command("create")
@click.option("--email", envvar="COSMONOTE_EMAIL")
def create_note(email):
    token = build_token(email)

    note = click.edit("Title goes here\n\nNote body goes here.\n")
    if not note:
        app.console.print("Nothing saved, note will be ignored.")
        return
    title, content = parse_note(note)

    links = []
    while True:
        terms = click.prompt("Link search terms", type=str, default="")
        if not terms:
            break
        data = {"terms": terms}
        r = app.api_request("search", "get", params=data, headers={"Authorization": f"Bearer {token}"})
        search_notes = r.json()['data']
        table = Table.grid(expand=True)
        table.add_column("", justify="left", style="green", no_wrap=True)
        table.add_column("Title", justify="left", no_wrap=True)
        table.add_column("Updated at", justify="left", style="cyan", no_wrap=True)
        for ii, note in enumerate(search_notes):
            table.add_row(f"{ii}.", note['title'], format_time(note['updated_at']))
        app.console.print(table)
        try:
            link_num = click.prompt("Add link", type=int)
        except click.Abort:
            app.console.print('')
            continue
        try:
            kind = click.prompt("Kind", type=click.Choice(['NA', 'SB', 'SP']), show_choices=True)
        except click.Abort:
            app.console.print('')
            continue
        links.append({
            'to_note': search_notes[link_num]['uuid'],
            'kind': kind,
        })

    data = {
        "title": title,
        "content": content,
        "links": links,
    }
    r = app.api_request("notes", "post", data, headers={"Authorization": f"Bearer {token}"})


@notes.command("update")
@click.option("--email", envvar="COSMONOTE_EMAIL")
@click.argument("uuid")
def update_note(email, uuid):
    token = build_token(email)
    r = app.api_request(f"notes/{parse_uuid(uuid)}", "get", headers={"Authorization": f"Bearer {token}"})
    note = r.json()['data']

    note_body = note['title']
    if note['content']:
        note_body += f"\n\n{note['content']}"
    note_body = click.edit(note_body)
    if not note_body:
        app.console.print("Nothing saved, aborted.")
        return
    title, content = parse_note(note_body)

    data = {
        "title": title,
        "content": content,
    }
    r = app.api_request(f"notes/{parse_uuid(uuid)}", "patch", data, headers={"Authorization": f"Bearer {token}"})


@notes.command("list")
@click.option("--email", envvar="COSMONOTE_EMAIL")
def list_notes(email):
    token = build_token(email)
    r = app.api_request("notes", "get", headers={"Authorization": f"Bearer {token}"})
    table = Table(show_edge=False, box=box.SIMPLE)
    table.add_column("Title", justify="right", style="cyan")
    table.add_column("Updated at", justify="left", no_wrap=True)
    table.add_column("UUID", justify="left", style="dim")
    table.add_column("# Links", justify="right", style="red")
    for note in r.json()['data']:
        table.add_row(
            note['title'],
            format_time(note['updated_at']),
            format_uuid(note['uuid']),
            f"{note['link_count']}" if note['link_count'] else "",
        )
    app.console.print(table)


@notes.command("search")
@click.option("--email", envvar="COSMONOTE_EMAIL")
@click.argument("terms")
def search_notes(email, terms):
    token = build_token(email)
    data = {"terms": terms, "limit": 100}
    r = app.api_request("search", "get", params=data, headers={"Authorization": f"Bearer {token}"})
    table = Table(show_edge=False, box=box.SIMPLE)
    table.add_column("Title", justify="right", style="cyan")
    table.add_column("Updated at", justify="left", no_wrap=True)
    table.add_column("UUID", justify="left", style="dim")
    for note in r.json()['data']:
        table.add_row(note['title'], format_time(note['updated_at']), format_uuid(note['uuid']))
    app.console.print(table)


@notes.command("get")
@click.option("--email", envvar="COSMONOTE_EMAIL")
@click.argument("uuid")
def get_note(email, uuid):
    token = build_token(email)
    r = app.api_request(f"notes/{parse_uuid(uuid)}", "get", headers={"Authorization": f"Bearer {token}"})
    note = r.json()['data']

    columns = []

    details = Markdown(f"# {note['title']}\n\n{note['content']}")
    details = Panel(details, title=f"Note: [dim]{format_uuid(note['uuid'])}", expand=True)

    table = Table.grid()
    table.add_column("", max_width=80)
    table.add_row(details)
    columns.append(table)

    if note['links']:
        links = Table(show_edge=False, expand=True, box=box.SIMPLE)
        links.add_column("To note", style="cyan")
        links.add_column("Kind")
        links.add_column("Note UUID", style="dim")
        links.add_column("Link UUID", style="dim")
        for l in note['links']:
            links.add_row(l['to_note']['title'], l['kind'], format_uuid(l['to_note']['uuid']), format_uuid(l['uuid']))
        links = Panel(links, title="Links", expand=True)

        table = Table.grid()
        table.add_column("", max_width=120)
        table.add_row(links)
        columns.append(table)

    app.console.print(Columns(columns))


@app.main.group()
def links():
    pass


@links.command("create")
@click.option("--email", envvar="COSMONOTE_EMAIL")
@click.option("--from-note", "-f", required=True)
@click.option("--to-note", "-t", required=True)
@click.option("--kind", "-k", type=click.Choice(['NA', 'SP', 'SB']), required=True)
def create_link(email, from_note, to_note, kind):
    token = build_token(email)
    data = {
        'from_note': str(parse_uuid(from_note)),
        'to_note': str(parse_uuid(to_note)),
        'kind': kind,
    }
    r = app.api_request("links", "post", data=data, headers={"Authorization": f"Bearer {token}"})


@links.command("update")
@click.option("--email", envvar="COSMONOTE_EMAIL")
@click.argument("uuid")
@click.option("--kind", "-k", type=click.Choice(['NA', 'SP', 'SB']), required=True)
def update_link(email, uuid, kind):
    token = build_token(email)
    data = {'kind': kind}
    r = app.api_request(f"links/{parse_uuid(uuid)}", "patch", data=data, headers={"Authorization": f"Bearer {token}"})


@links.command("delete")
@click.option("--email", envvar="COSMONOTE_EMAIL")
@click.argument("uuid")
def delete_link(email, uuid):
    token = build_token(email)
    r = app.api_request(f"links/{parse_uuid(uuid)}", "delete", headers={"Authorization": f"Bearer {token}"})
