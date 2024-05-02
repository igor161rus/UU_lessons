from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB

import os

os.environ["PATH"] += os.pathsep + r"D:\Python\Projects\UU\lessons\practice_03\.venv\Lib\site-packages\graphviz"

with Diagram("Web Service", show=False):
    ELB("lb") >> EC2("web") >> RDS("userdb")
