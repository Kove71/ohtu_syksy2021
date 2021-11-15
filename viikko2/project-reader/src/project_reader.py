from urllib import request
import toml

from project import Project


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        #print(content)

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        toml_parse = toml.loads(content)
        project_data = toml_parse["tool"]["poetry"]
        name = project_data["name"]
        description = project_data["description"]
        dependencies = project_data["dependencies"]
        dev_dependencies = toml_parse["tool"]["poetry"]["dev-dependencies"]
        return Project(name, description, dependencies, dev_dependencies)
