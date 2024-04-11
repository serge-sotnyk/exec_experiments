_code = """
from inner_package import version

def get_version():
    return version()
    
"""

if __name__ == "__main__":
    namespace = {}
    exec(_code, namespace, namespace)
    print(namespace['get_version']())
