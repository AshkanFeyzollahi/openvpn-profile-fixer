"""ovpn_pfix

The module that fixes unsupported OpenVPN profiles."""
import re
from io import TextIOWrapper

import click

with open("./supported-options.txt", "r") as f:
    SUPPORTED_OPTIONS = [line[:-1] for line in f.readlines()]

@click.command()
@click.option("--input", "-I", type=click.File(), help="The OpenVPN profile that user want to fix.")
@click.option("--output", "-O", type=click.File('w'), help="Output filename.")
def _ovpn_pfix(input: TextIOWrapper, output: TextIOWrapper) -> None:
    """Fixes unsupported OpenVPN profiles."""

    content_of_new_profile: str = ""

    input: str = input.read()

    for line in input.splitlines():
        if line.split()[0] not in SUPPORTED_OPTIONS:
            continue
        content_of_new_profile += line + '\n'

    if content_of_new_profile[-1] == '\n':
        content_of_new_profile = content_of_new_profile[:-1]

    certificates_regex = re.compile(r"((?:<ca>).*(?:</ca>)|(?:<cert>).*(?:</cert>))", re.DOTALL)
    keys_regex = re.compile(r"(?:<key>).*(?:</key>)", re.DOTALL)

    for certificate in certificates_regex.findall(input):
        content_of_new_profile += '\n' + certificate

    for key in keys_regex.findall(input):
        content_of_new_profile += '\n' + key

    output.write(content_of_new_profile)

if __name__ == "__main__":
    _ovpn_pfix()
