import requests
import json
import re

from doup import DockerImage
from doup import Utility

# ----------------------------------------------------------------------------
# https://github.com/docker/hub-feedback/issues/1253
class DockerVersionUpdater:

    dry_run = False

    def __init__(self, dry_run: bool):
        self.dry_run = dry_run

    def updateDockerVersion(self, dockerImage: DockerImage.DockerImage):
        digest = self.getChannelDigest(dockerImage, 'amd64')
        tags = self.getTagsToDigest(dockerImage, digest)
        nextVersion = self.getLatestVersion(dockerImage, tags)

        dockerImage.update(nextVersion, self.dry_run)

    def getChannelDigest(self, dockerImage: DockerImage.DockerImage, architecture: str):
        url = "https://hub.docker.com/v2/repositories/" + \
            dockerImage.namespace + "/" + \
            dockerImage.repository + "/tags/" + \
            dockerImage.channel

        response = requests.get(url)
        bar = json.loads(response.text)
        images = bar['images']

        digest = ''
        for image in images:
            if image['architecture'] == architecture:
                digest = image['digest']

        return digest

    def getTagsToDigest(self, dockerImage: DockerImage.DockerImage, digest: str):
        url = "https://hub.docker.com/v2/repositories/" + \
            dockerImage.namespace + "/" + \
            dockerImage.repository + "/tags/?page_size=1000"

        response = json.loads(requests.get(url).text)
        tags = []
        for result in response['results']:
            for image in result['images']:
                try:
                    if image['digest'] == digest:
                        tags.append(result['name'])
                except:
                    version = dockerImage.repository + ':'  + result['name']
                    print('WARNING: image ' + version + ' has no key <digest>')
        return tags

    def getLatestVersion(self, dockerImage, tags: list):
        tagsToRemove = []
        for tag in tags:
            if not Utility.stringContainsNumbers(tag):
                tagsToRemove.append(tag)

        for tag in tagsToRemove:
            tags.remove(tag)

        latestVersion = Utility.longestString(tags)
        return latestVersion

