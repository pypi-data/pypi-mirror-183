import argparse
import os

from doup import DockerVersionGrepper
from doup import DockerVersionUpdater

def getArgs():
    currentPath = os.getcwd()
    parser = argparse.ArgumentParser(description='doup is a tool to find and update Docker-Image-Strings in project files.')
    parser.add_argument('-p', '--path', type=str,
                        default=currentPath,
                        help='search for Docker-Image-Strings in a specific path')
    parser.add_argument('-d', '--dry-run', action='store_true',
                        help='print the Docker-Image-Strings but dont update any files')

    parser.add_argument('-g', '--group', type=str,
                        help='ignore all Docker-Image-Strings which are not part of the following group')

    args = parser.parse_args()

    return args

# -----------------------------------------------------------------------------

def main():
    args = getArgs()

    dockerVersionUpdater = DockerVersionUpdater.DockerVersionUpdater(args.dry_run)
    dockerVersionGrepper = DockerVersionGrepper.DockerVersionGrepper(args.path, args.group)

    dockerImages = dockerVersionGrepper.getDockerImagesInPath()
    for dockerImage in dockerImages:
        dockerVersionUpdater.updateDockerVersion(dockerImage)

