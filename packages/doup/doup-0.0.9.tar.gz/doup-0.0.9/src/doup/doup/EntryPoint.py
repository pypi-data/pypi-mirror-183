import argparse
import os

from doup import DockerVersionGrepper
from doup import DockerVersionUpdater

def getArgs():
    currentPath = os.getcwd()
    parser = argparse.ArgumentParser(description='find docker images recursivly in the current working directory')
    parser.add_argument('-p', '--path', type=str,
                        default=currentPath,
                        help='search in a different path for docker versions')
    parser.add_argument('-d', '--dry-run', action='store_true',
                        help='run in dry run mode and dont change files')

    parser.add_argument('-g', '--group', type=str,
                        help='update only specific group members')

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

