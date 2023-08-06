from termcolor import colored

def getVersion(versionString: str):
    return versionString.split(':')[1].strip()

def getNamespace(versionString: str):
    namespaceAndRepo = versionString.split(':')[0].split('/')
    namespace = ''

    if len(namespaceAndRepo) == 2:
        namespace = namespaceAndRepo[0]
    else:
        namespace = 'library'

    return namespace.strip()

def getRepository(versionString: str):
    namespaceAndRepo = versionString.split(':')[0].split('/')
    repo = ''

    if len(namespaceAndRepo) == 2:
        repo = namespaceAndRepo[1]
    else:
        repo = namespaceAndRepo[0]

    return repo.strip()

# ----------------------------------------------------------------------------

class DockerImage:
    versionString = ''
    filename = ''
    channel = ''
    group = ''

    namespace = ''
    repository = ''
    version = ''

    def __init__(self, versionString: str, channel: str, group: str, filename: str):
        self.versionString = versionString.strip()
        self.filename = filename
        self.channel = channel
        self.group = group

        self.namespace = getNamespace(versionString)
        self.version = getVersion(versionString)
        self.repository = getRepository(versionString)

    def show(self):
        print('versionString: ' + self.versionString)
        print('channel: ' + self.channel)
        print('group: ' + self.group)
        print('filename: ' + self.filename)
        print('namespace: ' + self.namespace)
        print('repository: ' + self.repository)
        print('version: ' + self.version)
        print('--------------------------------------------------------------')

    def getVersionString(self, newVersion: str):
        versionString = ''

        if self.namespace == 'library':
            versionString = self.repository + ':' + newVersion
        else:
            versionString = self.namespace + '/' + self.repository + ':' + newVersion

        return versionString


    def update(self, nextVersion: str, dry_run: bool):
        print('--------------------------------------------------------------')

        if nextVersion == self.version:
            print(self.namespace + '/' + self.repository + ': ' + \
                colored(self.version, 'green'))

        else:
            print(self.namespace + '/' + self.repository + ': ' + \
                colored(self.version, 'red') + ' -> ' + \
                colored(nextVersion, 'green'))

            if not dry_run:
                file = open(self.filename, 'rt')
                data = file.read()
                data = data.replace(self.versionString, self.getVersionString(nextVersion))
                file.close()

                file = open(self.filename, 'wt')
                file.write(data)
                file.close()

