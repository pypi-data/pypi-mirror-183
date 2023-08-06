from fintekkers.devops.aws_account_setup import get_ecr_client
from fintekkers.devops.aws_account_setup import REPOSITORY_NAME, SERVICE_NAME
import base64, os 

import docker
from docker import DockerClient

DOCKER_FILE = os.environ['FINTEKKERS_DOCKER_FILEE'] if 'FINTEKKERS_DOCKER_FILE' in os.environ else "Dockerfile"
print("DOCKER_FILE: {}".format(DOCKER_FILE))

DOCKER_IMAGE_VERSION = os.environ['FINTEKKERS_DOCKER_IMAGE_VERSION'] if 'FINTEKKERS_DOCKER_IMAGE_VERSION' in os.environ else "0"
print("DOCKER_IMAGE_VERSION: {}".format(DOCKER_IMAGE_VERSION))

def get_image_tag_name():
    return SERVICE_NAME

def get_image_tag_name_with_version():
    return "{}:{}".format(get_image_tag_name(), "latest")

def docker_login() -> tuple:
    docker_client = docker.from_env()
    ecr_credentials = (get_ecr_client().get_authorization_token()['authorizationData'][0])

    ecr_username = 'AWS'

    ecr_password = (
        base64.b64decode(ecr_credentials['authorizationToken'])
        .replace(b'AWS:', b'')
        .decode('utf-8'))

    ecr_url = ecr_credentials['proxyEndpoint']

    print("Logging in to {}. {} / {}".format(ecr_url, ecr_username, ecr_password))
    docker_client.login(username=ecr_username, password=ecr_password, registry=ecr_url)
    #Equivalent of aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 754996918532.dkr.ecr.us-east-1.amazonaws.com

    return docker_client, ecr_url

def build_and_tag_image(docker_client:DockerClient, image_tag_name:str, version:str, ecr_url:str):
    #If you're building on Mac M chips, or on Windows, you'll need this platform arg.
    #equivalent of " --platform linux/amd64" param when running docker build on command line
    print("Building image: {}".format(image_tag_name))
    image, build_log = docker_client.images.build(path='.', tag=image_tag_name, \
        rm=True, dockerfile=DOCKER_FILE, platform="linux/amd64")
    print(list(build_log)[:-5])

    ecr_repo_name = '{}/{}'.format(ecr_url.replace('https://', ''), REPOSITORY_NAME)
    print("Tagging image with {}, version {}".format(ecr_repo_name, version))
    image.tag(ecr_repo_name, tag=version)
    return ecr_repo_name
    
def push_image(docker_client:DockerClient, ecr_repo_name:str):
    print("Pushing image: {}".format(ecr_repo_name))

    push_log = docker_client.images.push(ecr_repo_name, tag=DOCKER_IMAGE_VERSION)
    #Equivalent of docker push 754996918532.dkr.ecr.us-east-1.amazonaws.com/fintekkers-dummy-service:latest
    print(push_log)

def build_and_push_docker_image():
    image_tag_name = get_image_tag_name_with_version()

    versions_for_this_build = ["latest", DOCKER_IMAGE_VERSION]

    for version in versions_for_this_build:
        docker_client, ecr_url = docker_login()
        ecr_repo_name = build_and_tag_image(docker_client, image_tag_name, version, ecr_url)
        print("Pushing image to {}".format(ecr_repo_name))
        push_image(docker_client, ecr_repo_name)

if __name__ == "__main__":
    build_and_push_docker_image()