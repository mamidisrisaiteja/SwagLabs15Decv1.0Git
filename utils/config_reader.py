import yaml
class ConfigError(Exception):
    pass
class ConfigReader:
    def __init__(self,path="config.yml"):
        self.path=path
    def load_config(self):
        try:
            with open(self.path,"r") as f:
                return yaml.safe_load(f) or {}
        except FileNotFoundError:
            raise ConfigError(f"Config file not found {self.path}")
        except yaml.YAMLERROR as e:
            raise ConfigError(f"Incorrect yaml:{e}")

