Sifflet CLI
==========

This package provides a command line interface (CLI) to [Sifflet](https://www.siffletdata.com/)  application.

# Getting Started
## Installation

Sifflet CLI is compatible with Python version 3.7 or greater

```shell
pip install sifflet

sifflet --version
```

## Configuration

Before using the Sifflet CLI, you need to set your tenant and credentials. 
You can do it in several ways:
- Sifflet command line `sifflet configure` (which will persists configuration in a file)
- Or with environment variables  

You will need in both cases the following information:  
`<your_tenant_name>`: if you access to Sifflet with "https://abcdef.siffletdata.com", then your tenant would be `abcdef`  
`<your_sifflet_access_token>`: you can find more information on how to generate it [here](https://docs.siffletdata.com/docs/generate-an-api-token)


#### Sifflet configure
You can input the tenant and credentials directly with the `sifflet configure` command
```shell
> sifflet configure
Your tenant name [None]: <your_tenant_name>
Your API access token [None]: <your_sifflet_access_token>
```
The use of `sifflet configure` will persist the configuration in a file located at `~/.sifflet/config.ini` 
(or in `%UserProfile%\.sifflet/config.ini` on Windows).

#### Environment variables
To use environment variables, you can do the following:

```shell
> export SIFFLET_TENANT=<your_tenant_name>
> export SIFFLET_TOKEN=<your_sifflet_access_token> 
```


You can check that setup is done correctly with `sifflet status`.

```shell
> sifflet status

Sifflet version = x.x.x
Tenant = my_tenant
Tenant is up and reachable
Token expiration date = 2024-01-01 00:00:00
Token is valid with scope API
Status = OK
```

If you encounter any error at this step, please check your tenant and token configurations.

## Documentation
The documentation with the available commands can be found [here](https://docs.siffletdata.com/docs/cli-command-line-interface).

## Help
The `--help` option is available for any command, for instance `sifflet --help` or `sifflet rules list --help`.

## Examples

### Trigger a specific rule 
- First, find your rule id with `sifflet rules list`. You can filter with `--name` to narrow your search.

```shell
# Display rules
sifflet rules list
sifflet rules list --name <search_criteria>
```

- Then you can trigger one of several rules with `sifflet rules run`

```shell
# Run one or many rules
sifflet rules run --id <rule_id>
sifflet rules run --id <rule_id_1> --id <rule_id_2> --id <rule_id_3>
```

- Finally, retrieve the run status of a rule with `sifflet rules run_history`

```shell
# Display rule runs history for a given rule id
sifflet rules run_history --id <rule_id>
```

### Send dbt artifacts
If you have already added the datasource to Sifflet, you can then send the dbt artifacts for syncing the data.

```shell
# send the dbt artifacts
sifflet ingest dbt --project-name <project_name> --target <target> --input-folder <dbt_artifacts_directory>
```

## Contact

For any queries, you can reach us at `contact@siffletdata.com`