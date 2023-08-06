from os import chmod
from .python_util import *
from .devops_build import DevopsBuild
from .credential import gopass_field_from_path, gopass_password_from_path

def add_c4k_mixin_config(config,
                         c4k_module_name,
                         c4k_config_dict,
                         c4k_auth_dict):
    
    config.update({'C4kMixin': {'Config': c4k_config_dict,
                                'Auth': c4k_auth_dict,
                                'Name': c4k_module_name}})
    return config


class C4kMixin(DevopsBuild):

    def __init__(self, project, config):
        super().__init__(project, config)
        self.c4k_mixin_config = config['C4kMixin']['Config']
        self.c4k_mixin_auth = config['C4kMixin']['Auth']
        self.c4k_module_name = config['C4kMixin']['Name']

    def __generate_clojure_map(self, template_dict):
        clojure_map_str = '{'
        for key, value in template_dict.items():
            if type(value) is dict:
                clojure_map_str += f':{key} {self.__generate_clojure_map(value)}\n' 
            else:
                clojure_map_str += f':{key} "{value}"\n'
        clojure_map_str += '}'
        return clojure_map_str

    def write_c4k_config(self):
        fqdn = self.get('fqdn')
        self.c4k_mixin_config.update({'fqdn':fqdn})
        self.c4k_mixin_config.update({'mon-config': {
            'cluster-name': f':{self.c4k_module_name}',
            'cluster-stage': f':{self.stage}',
            'grafana-cloud-url': 'https://prometheus-prod-01-eu-west-0.grafana.net/api/prom/push'}})
        with open(self.build_path() + '/out_config.edn', 'w') as output_file:
            output_file.write(self.__generate_clojure_map(self.c4k_mixin_config))
    
    def write_c4k_auth(self):
        self.c4k_mixin_auth.update({'mon-auth': {
            'grafana-cloud-user': gopass_field_from_path('server/meissa/grafana-cloud', 'grafana-cloud-user'),
            'grafana-cloud-password': gopass_password_from_path('server/meissa/grafana-cloud')
        }})
        with open(self.build_path() + '/out_auth.edn', 'w') as output_file:
            output_file.write(self.__generate_clojure_map(self.c4k_mixin_auth))
        chmod(self.build_path() + '/out_auth.edn', 0o600)

    def c4k_apply(self):
        cmd = f'c4k-{self.c4k_module_name}-standalone.jar {self.build_path()}/out_config.edn {self.build_path()}/out_auth.edn > {self.build_path()}/out_{self.c4k_module_name}.yaml'
        output = execute(cmd, True)
        print(output)
        return output
