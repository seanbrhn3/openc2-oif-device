from flask import Flask, request
from .utils import decode_msg, encode_msg, FrozenDict, MessageQueue, safe_cast
from .actuator import Actuator  # contains basic actuator methods and actuator data

app = Flask(__name__)

"""
    Windows:
           powershell -netsh add delete firwall rules, kill process with executable name
           return netstat -A (Everything open)
           block port or range of ports, block out going packets

        ACL
    Rules:
        Debian/Ubuntu
        CentOS
        Windows
        Redhat rule
    """
rules = {
    "Windows"
}

@app.route("/", methods=['GET', 'POST'])
def index():
    return "something"
