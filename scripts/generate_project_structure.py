import os
import sys

def create_directory(path):
    os.makedirs(path, exist_ok=True)

def generate_project_structure(base_path):
    # Create main project directory
    create_directory(base_path)

    # src directory
    src_path = os.path.join(base_path, 'src')
    create_directory(src_path)
    
    # Application layer
    app_path = os.path.join(src_path, 'application')
    create_directory(app_path)
    create_directory(os.path.join(app_path, 'interfaces'))
    create_directory(os.path.join(app_path, 'services'))
    create_directory(os.path.join(app_path, 'use_cases'))

    # Domain layer
    domain_path = os.path.join(src_path, 'domain')
    create_directory(domain_path)
    create_directory(os.path.join(domain_path, 'entities'))
    create_directory(os.path.join(domain_path, 'value_objects'))
    create_directory(os.path.join(domain_path, 'events'))

    # Infrastructure layer
    infra_path = os.path.join(src_path, 'infrastructure')
    create_directory(infra_path)
    create_directory(os.path.join(infra_path, 'database'))
    create_directory(os.path.join(infra_path, 'repositories'))
    create_directory(os.path.join(infra_path, 'messaging'))
    create_directory(os.path.join(infra_path, 'cache'))

    # Presentation layer
    pres_path = os.path.join(src_path, 'presentation')
    create_directory(pres_path)
    api_path = os.path.join(pres_path, 'api')
    create_directory(api_path)
    create_directory(os.path.join(api_path, 'routes'))
    create_directory(os.path.join(api_path, 'schemas'))
    create_directory(os.path.join(pres_path, 'grpc'))
    create_directory(os.path.join(pres_path, 'graphql'))

    # Core
    create_directory(os.path.join(src_path, 'core'))

    # Common
    create_directory(os.path.join(src_path, 'common'))

    # Tests directory
    tests_path = os.path.join(base_path, 'tests')
    create_directory(tests_path)
    create_directory(os.path.join(tests_path, 'unit'))
    create_directory(os.path.join(tests_path, 'integration'))
    create_directory(os.path.join(tests_path, 'e2e'))

    # Docs directory
    # docs_path = os.path.join(base_path, 'docs')
    # create_directory(docs_path)
    # create_directory(os.path.join(docs_path, 'adr'))

    # Scripts directory
    create_directory(os.path.join(base_path, 'scripts'))

    # Kubernetes directory
    create_directory(os.path.join(base_path, 'k8s'))

    # CI directory
    create_directory(os.path.join(base_path, 'ci'))

    print(f"Project structure created at: {base_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python generate_project_structure.py <project_name>")
        sys.exit(1)
    
    project_name = sys.argv[1]
    project_path = os.path.join(os.getcwd(), project_name)
    generate_project_structure(project_path)