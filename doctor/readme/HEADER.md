Teku
=========

Teku is an open source Ethereum consensus client written in Java. Teku contains a full beacon node implementation and a validator client for participating in proof of stake consensus.

Currently, the role supports only validator client deployment.

**Tests:**
* Ubuntu 24.04 (noble)

How to run molecule tests
----------------------

```shell
python3 -m venv venv
pip install -r requirements.txt
source venv/bin/activate
make init
make test
```

Make
----

`make init` - Prepare environment
`make test` - Run molecule tests (`molecule -v test`)
`make docs` - Auto-generate `README` (`ansible-doctor`)

Role install
--------------

You can install role by using `ansible-galaxy`:

```shell
ansible-galaxy role install git+git@github.com:keynodes-org/ansible_teku.git
```

For particular version of this role:
```shell
ansible-galaxy role install git+git@github.com:keynodes-org/ansible_teku.git,main
```

Update to latest version:
```shell
ansible-galaxy role install git+git@github.com:keynodes-org/ansible_teku.git --upgrade
```

Example of using in `requirements.yml`:
```yaml
---
roles:
  - name: teku
    src: git+git@github.com:keynodes-org/ansible_teku.git
    version: main
```

How to use in playbook:
-------------------------

```yaml
- hosts: ansible_hostname
  roles:
    - role: ansible_teku
```

Variables
===============
