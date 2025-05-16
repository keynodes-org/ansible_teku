# ansible_teku

Ansible role for deploying Teku Ethereum consensus layer node
Currently, the role supports only beacon node deployment.

## Auto-generated

- [Defaults](#default-vars)
  - [data_storage_mode](#data_storage_mode)
  - [teku_beacon_node_config](#teku_beacon_node_config)
  - [teku_binary_download_url](#teku_binary_download_url)
  - [teku_binary_path](#teku_binary_path)
  - [teku_checkpoint_sync_url](#teku_checkpoint_sync_url)
  - [teku_config_file_path](#teku_config_file_path)
  - [teku_dir_base](#teku_dir_base)
  - [teku_dir_beacon](#teku_dir_beacon)
  - [teku_dir_binary](#teku_dir_binary)
  - [teku_dir_config](#teku_dir_config)
  - [teku_dir_data](#teku_dir_data)
  - [teku_dir_install](#teku_dir_install)
  - [teku_dir_lib](#teku_dir_lib)
  - [teku_dir_log](#teku_dir_log)
  - [teku_dir_validator](#teku_dir_validator)
  - [teku_download_url](#teku_download_url)
  - [teku_ee_endpoint](#teku_ee_endpoint)
  - [teku_group](#teku_group)
  - [teku_install_java](#teku_install_java)
  - [teku_java_apt_package_name](#teku_java_apt_package_name)
  - [teku_java_install](#teku_java_install)
  - [teku_java_memory_size](#teku_java_memory_size)
  - [teku_jwt_secret_path](#teku_jwt_secret_path)
  - [teku_log_level](#teku_log_level)
  - [teku_metrics_enabled](#teku_metrics_enabled)
  - [teku_network](#teku_network)
  - [teku_reinstall](#teku_reinstall)
  - [teku_rest_api_port](#teku_rest_api_port)
  - [teku_systemd_env_options](#teku_systemd_env_options)
  - [teku_systemd_service_name](#teku_systemd_service_name)
  - [teku_systemd_service_path](#teku_systemd_service_path)
  - [teku_user](#teku_user)
  - [teku_version](#teku_version)
- [Tags](#tags)

- [Dependencies](#dependencies)

---

## Defaults

### data_storage_mode

Sets the strategy for handling historical chain: ARCHIVE, PRUNE, MINIMAL, NOT_SET

#### Defaults

```YAML
data_storage_mode: PRUNE
```

### teku_beacon_node_config

Teku config file options Each key name is the corresponding command line option name without the leading dashes (--).

#### Defaults

```YAML
teku_beacon_node_config:
  - name: data-path
    value: '{{ teku_dir_data }}'
  - name: data-beacon-path
    value: '{{ teku_dir_beacon }}'
  - name: data-validator-path
    value: '{{ teku_dir_validator }}'
  - name: data-storage-mode
    value: '{{ data_storage_mode }}'
  - name: checkpoint-sync-url
    value: '{{ teku_checkpoint_sync_url }}'
  - name: network
    value: '{{ teku_network }}'
  - name: log-file
    value: '{{ teku_dir_log }}/teku.log'
  - name: log-destination
    value: FILE
  - name: logging
    value: '{{ teku_log_level }}'
  - name: ee-endpoint
    value: '{{ teku_ee_endpoint }}'
  - name: ee-jwt-secret-file
    value: '{{ teku_jwt_secret_path }}'
  - name: rest-api-port
    value: '{{ teku_rest_api_port }}'
  - name: metrics-enabled
    value: '{{ teku_metrics_enabled }}'
```

### teku_binary_download_url

#### Defaults

```YAML
teku_binary_download_url: https://artifacts.consensys.net/public/teku/raw/names/teku.tar.gz/versions/{{
  teku_version }}/teku-{{ teku_version }}.tar.gz
```

### teku_binary_path

Path where the Teku binary exists.

#### Defaults

```YAML
teku_binary_path: '{{ teku_dir_binary }}/teku'
```

### teku_checkpoint_sync_url

Teku snap sync url.

#### Defaults

```YAML
teku_checkpoint_sync_url: https://sepolia.beaconstate.info
```

### teku_config_file_path

Path to the Teku YAML configuration file used by the service.

#### Defaults

```YAML
teku_config_file_path: '{{ teku_dir_config }}/config.yaml'
```

### teku_dir_base

Base directory for Teku installation and data.

#### Defaults

```YAML
teku_dir_base: /opt/teku
```

### teku_dir_beacon

Directory for Teku beacon data.

#### Defaults

```YAML
teku_dir_beacon: '{{ teku_dir_data }}/beacon'
```

### teku_dir_binary

Directory to install Teku binary

#### Defaults

```YAML
teku_dir_binary: /usr/local/bin
```

### teku_dir_config

Directory for Teku configuration files.

#### Defaults

```YAML
teku_dir_config: '{{ teku_dir_base }}/config'
```

### teku_dir_data

Directory for Teku data storage.

#### Defaults

```YAML
teku_dir_data: '{{ teku_dir_base }}/data'
```

### teku_dir_install

Directory where Teku tarball is downloaded and extracted.

### teku_dir_lib

#### Defaults

```YAML
teku_dir_lib: '{{ teku_dir_base }}/lib'
```

### teku_dir_log

Directory for Teku log files.

#### Defaults

```YAML
teku_dir_log: '{{ teku_dir_base }}/logs'
```

### teku_dir_validator

Directory for Teku validator data .

#### Defaults

```YAML
teku_dir_validator: '{{ teku_dir_data }}/validator'
```

### teku_download_url

Full URL to download the Teku binary. Default is constructed from teku_version and teku_download_url_base.

### teku_ee_endpoint

Teku execution layer client url.

#### Defaults

```YAML
teku_ee_endpoint: https://ethereum-sepolia-rpc.publicnode.com
```

### teku_group

Group for the Teku service.

#### Defaults

```YAML
teku_group: teku
```

### teku_install_java

Whether to install Java (OpenJDK).

### teku_java_apt_package_name

Name of the Java package to install.

#### Defaults

```YAML
teku_java_apt_package_name: openjdk-21-jre-headless
```

### teku_java_install

#### Defaults

```YAML
teku_java_install: true
```

### teku_java_memory_size

Teku RAM usage limit, default 6 gigabyte(6g).

#### Defaults

```YAML
teku_java_memory_size: 6g
```

### teku_jwt_secret_path

JWT file path.

#### Defaults

```YAML
teku_jwt_secret_path: '{{ teku_dir_config }}/jwt.hex'
```

### teku_log_level

Teku log level - OFF, FATAL, ERROR, WARN, INFO, DEBUG, TRACE, ALL

#### Defaults

```YAML
teku_log_level: DEBUG
```

### teku_metrics_enabled

Enable prometheus metrics.

#### Defaults

```YAML
teku_metrics_enabled: true
```

### teku_network

Teku network name(mainnet, sepolia, hoodi etc).

#### Defaults

```YAML
teku_network: sepolia
```

### teku_reinstall

Flag for Teku reinstall.

#### Defaults

```YAML
teku_reinstall: false
```

### teku_rest_api_port

Resti api port.

#### Defaults

```YAML
teku_rest_api_port: 8551
```

### teku_systemd_env_options

Teku systemd environment options.

#### Defaults

```YAML
teku_systemd_env_options:
  - JAVA_OPTS=-Xmx{{ teku_java_memory_size }}
```

### teku_systemd_service_name

Name of the Teku systemd service.

#### Defaults

```YAML
teku_systemd_service_name: teku
```

### teku_systemd_service_path

Path for the Teku systemd service file.

#### Defaults

```YAML
teku_systemd_service_path: /etc/systemd/system/{{ teku_systemd_service_name }}.service
```

### teku_user

Username for the Teku service.

#### Defaults

```YAML
teku_user: teku
```

### teku_version

Version of Teku to install.

#### Defaults

```YAML
teku_version: 25.4.1
```

## Tags

**_teku-config_**

**_teku-install_**

**_teku-prepare_**

## Dependencies

None.
