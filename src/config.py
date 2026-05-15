import yaml
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_DIR = BASE_DIR / "config"


def load_config(config_name="config.yaml"):
    """
    Load a YAML configuration file.

    Parameters
    ----------
    config_name : str
        Name of the config file inside config/ directory.

    Returns
    -------
    dict
        Parsed configuration dictionary.
    """

    config_path = CONFIG_DIR / config_name

    with open(config_path, "r") as file:
        config = yaml.safe_load(file)

    return config


def save_config(config, config_name="config.yaml"):
    """
    Save a configuration dictionary to a YAML file.

    Parameters
    ----------
    config : dict
        Configuration dictionary to save.

    config_name : str
        Name of the config file inside config/ directory.
    """

    config_path = CONFIG_DIR / config_name

    with open(config_path, "w") as file:
        yaml.dump(config, file, sort_keys=False)


def update_config(key_path, value, config_name="config.yaml"):
    """
    Update a specific configuration value.

    Parameters
    ----------
    key_path : str
        Configuration of the key using dot notation.

    value : any
        New value to assign.

    config_name : str
        Name of the config file.
    """

    config = load_config(config_name)

    keys = key_path.split(".")
    temp = config

    for key in keys[:-1]:
        if key not in temp or not isinstance(temp[key], dict):
            temp[key] = {}
        temp = temp[key]

    temp[keys[-1]] = value

    save_config(config, config_name)

    print(f"Updated [{key_path}] -> {value}")