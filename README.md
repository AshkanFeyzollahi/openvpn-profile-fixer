# OpenVPN Profile Fixer

The Python3 module that fixes unsupported OpenVPN profiles. *What does
OpenVPN Profile Fixer actually do?* Well, it removes unsupported options
from `.ovpn` files and it specially made for `option_error: sorry, unsupported
options present in configuration: UNKNOWN/UNSUPPORTED OPTIONS`

For more details about `UNKNOWN/UNSUPPORTED OPTIONS`, look at https://support.openvpn.com/hc/article_attachments/17545051570587

## Requirements

Python >= 3.7

## How to use?

1. To start using ovpn_pfix just open terminal/cmd and clone this repository
    by entering this command in terminal/cmd:

    ```bash
    git clone AshkanFeyzollahi/ovpn_pfix
    ```

2. Go to where you cloned repository files to and open terminal/cmd.

3. Install requirements and dependencies by entering one of below commands in
    terminal/cmd:

    * Windows

        ```bash
        python -m pip install -r requirements.txt
        ```

    * Linux/MacOS

        ```bash
        python3 -m pip install -r requirements.txt
        ```

    After installing requirements and dependencies, you're ready to go and start
    using ovpn_pfix.

4. Open terminal/cmd in same directory and run one of following commands to start
    using ovpn_pfix.

    * Windows

        ```bash
        python ovpn_pfix.py --help
        ```

    * Linux/MacOS

        ```bash
        python3 ovpn_pfix.py --help
        ```

### Usage

```plain
Usage: ovpn_pfix.py [OPTIONS]

  Fixes unsupported OpenVPN profiles.

Options:
  -I, --input FILENAME   The OpenVPN profile that user want to fix.
  -O, --output FILENAME  Output filename.
  --help                 Show this message and exit.
```

## Issues

If you had problem while running `ovpn_pfix.py`, feel free to open
an issue.
