import argparse
import os

from doup import DockerVersionGrepper
from doup import DockerVersionUpdater

def getArgs():
    currentPath = os.getcwd()
    parser = argparse.ArgumentParser(description='Find docker images in project files recursivly')
    parser.add_argument('-p', '--path', type=str,
                        default=currentPath,
                        help='find docker images in a specific path')
    parser.add_argument('-d', '--dry-run', action='store_true',
                        help='print the dockerimage versions but dont change any files')

    parser.add_argument('-g', '--group', type=str,
                        help='update only docker images from a specific group')

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

