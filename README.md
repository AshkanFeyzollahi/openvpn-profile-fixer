# OpenVPN Profile Fixer: A Python3 Module to Modify Unsupported OpenVPN Profiles

https://github.com/AshkanFeyzollahi/openvpn-profile-fixer/assets/136630721/adb4e000-b297-43e0-a482-89fbe505854e

This is a Python3 script designed to modify unsupported options within .ovpn files. If you encounter the error "unknown/unsupported options" when trying to use an OpenVPN profile, this tool can help. For further information on these unsupported options, please refer to this [article](https://support.openvpn.com/hc/article_attachments/17545051570587).

## Prerequisites

To get started with openvpn-profile-fixer, ensure you have the following installed:

- Python version 3.7 or higher
- PIP, the latest version
- Git, the latest version

## Instructions

Begin by opening your terminal or command prompt and clone this repository using the following command:

```bash
git clone https://github.com/AshkanFeyzollahi/openvpn-profile-fixer.git
```

Navigate to the location where you cloned the repository and launch your terminal or command prompt there.

Next, install the required packages and dependencies by executing either of the following commands based on your operating system:

- **Windows**:

    ```bash
    python -m pip install -r requirements.txt
    ```

- **Linux**/**macOS**:

    ```bash
    python3 -m pip install -r requirements.txt
    ```

Once you've successfully installed the necessary packages and dependencies, you are now prepared to utilize openvpn-profile-fixer.

In the same directory as before, execute the following command in your terminal or command prompt to begin using the script:

- **Windows**:

    ```bash
    python ovpn_pfix.py --help
    ```

- **Linux**/**macOS**:

    ```bash
    python3 ovpn_pfix.py --help
    ```

## Usage

You can apply the modifications to your OpenVPN profile file using the provided script with the following command line arguments:

```bash
Usage: ovpn_pfix.py [OPTIONS]

  This script modifies unsupported options within OpenVPN profiles.

Options:
  -I, --input FILENAME       Specify the input .ovpn file name.
  -O, --output FILENAME      Define the output filename.
  --help                     Show this message and exit.
```

Now, simply replace FILENAME with the name of your input.ovpn file and provide the desired output filename if needed. Run the script accordingly:

- **Windows**:

    ```bash
    python ovpn_pfix.py -I input.ovpn -O output.ovpn
    ```

- **Linux**/**macOS**:

    ```bash
    python3 ovpn_pfix.py -I input.ovpn -O output.ovpn
    ```

## Collaborate & Report Updates

As OpenVPN updates its configurations and introduces new unsupported options, it becomes essential to keep our script current and effective. Users who come across newly identified unsupported options during their OpenVPN sessions are encouraged to contribute by reporting such cases. By submitting an issue ticket, you enable us to collaboratively enhance the capabilities of the openvpn-profile-fixer script.

Here's how to proceed:

- Identify the specific unsupported option causing issues after an OpenVPN update.
- Create a new issue ticket on [our project issues page](https://github.com/AshkanFeyzollahi/openvpn-profile-fixer/issues).
- Provide detailed steps to reproduce the issue along with the relevant OpenVPN logs and the affected .ovpn file.
- Allow our community of maintainers and contributors to discuss potential solutions and implement improvements into the script.

By working together, we can continually refine the openvpn-profile-fixer script and ensure compatibility with the evolving landscape of OpenVPN configurations. Let's continue enhancing the utility and accessibility of OpenVPN for all users!

## Issues

In case you experience any problems while utilizing ovpn_pfix.py, we encourage you to report the issue through creating an issue ticket on our GitHub page. We will be glad to assist you and work towards resolving any encountered difficulties. Thank you!
