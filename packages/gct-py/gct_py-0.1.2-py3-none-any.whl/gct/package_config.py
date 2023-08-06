import platform
import subprocess

GRAPHVIZ_INSTRUCTIONS_LINK = "https://github.com/QasimWani/gct/#graphical-code-tracer-gct-is-the-worlds-first-static-code-visualization-tool"


def _install_pip_package(package: str):
    try:
        __import__(package)
    except ImportError:
        subprocess.check_call(["pip", "install", package])


def _is_graphviz_installed():
    """Function that checks if graphviz is installed and if so, is dot version >= 6.0.1"""
    try:
        output = subprocess.Popen(
            ["dot", "-V"], stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        data = output.stderr.read()

        version = (
            data.decode("utf-8").split("graphviz version ")[1].split(" ")[0].strip()
        )
        assert version >= "6.0.1", version
        return True

    except AssertionError as e:
        message = f"Found graphviz version {e}. Dot version >= 6.0.1 is required. See instructions for graphviz: {GRAPHVIZ_INSTRUCTIONS_LINK}"
        print(message)
    except subprocess.CalledProcessError:
        print(
            "Graphviz not installed. See instructions for graphviz:",
            GRAPHVIZ_INSTRUCTIONS_LINK,
        )
    except Exception as e:
        print("Unknown error while checking for graphviz version:", e)
    return False


def _install_graphviz():
    # Check for correct version of graphviz, if installed.
    if _is_graphviz_installed():
        return

    system = platform.system()
    try:
        if system == "Windows":
            subprocess.check_call(["choco", "install", "-y", "graphviz"])
        elif system == "Darwin":  # macOS
            subprocess.check_call(["brew", "install", "graphviz"])
        else:  # assume Linux or other Unix-like system
            subprocess.check_call(["apt-get", "install", "-y", "graphviz"])
    except:
        print(
            "Failed to install graphviz. See instructions for graphviz:",
            GRAPHVIZ_INSTRUCTIONS_LINK,
        )


# Install python packages and graphviz dist. if they don't exist.
def installer():
    PACKAGES = ["argparse", "graphviz", "networkx", "platform"]
    for package in PACKAGES:
        _install_pip_package(package)

    _install_graphviz()
