'''
# Azure DevOps Git Repository Archiver

[![npm version](https://badge.fury.io/js/azure-devops-repository-archiver.svg)](https://badge.fury.io/js/azure-devops-repository-archiver)
![Release](https://github.com/stefanfreitag/azure_s3_repository_archiver/workflows/release/badge.svg)

Allows to backup regularly git repositories hosted in Azure DevOps to an S3 Bucket.

## Planned Features

* Logging to CloudWatch

  * Encryption using customer-managed KMS key
* Notifications to SNS about uploaded objects
* S3 bucket encryption and versioning
* Lifecycle configuration for the archived repositories. Will move in S3 to

  * Infrequent Access after 30 days
  * Glacier after 60 days
  * Deep Archive 90 days
  * Expiry after 180 days
* Tagging of created AWS resources

## Prerequisites

The connection to the Azure DevOps organization requires a [personal access
token](https://learn.microsoft.com/en-us/azure/devops/organizations/accounts/use-personal-access-tokens-to-authenticate).
The PAT needs to have "Code read" permission and stored in a SecretsManager secret

```shell
aws secretsmanager create-secret --name rwest_archiver_rwest_platform --description "RWEST Archiver for RWEST-Platform organization" --secret-string "{\"pat\":\"<your_pat>\"}"
```

## Links

* [projen](https://github.com/projen/projen)
* [cdk](https://github.com/aws/aws-cdk)
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from typeguard import check_type

from ._jsii import *

import constructs as _constructs_77d1e7e8


class Archiver(
    _constructs_77d1e7e8.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="azure-devops-repository-archiver.Archiver",
):
    '''
    :stability: experimental
    '''

    def __init__(self, scope: _constructs_77d1e7e8.Construct, id: builtins.str) -> None:
        '''
        :param scope: -
        :param id: -

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__59b1d445ea6a4ea2b344c5e83eb14b7e5d57e243d55dbad607605e1e2e63c1b5)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = ArchiverProperties()

        jsii.create(self.__class__, self, [scope, id, props])

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "ArchiverProperties":
        '''
        :stability: experimental
        '''
        return typing.cast("ArchiverProperties", jsii.get(self, "props"))

    @props.setter
    def props(self, value: "ArchiverProperties") -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb1dff6681014d6e509e01d6b12c3974e4810c8d1a67b368174954a280d668f6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "props", value)


@jsii.data_type(
    jsii_type="azure-devops-repository-archiver.ArchiverProperties",
    jsii_struct_bases=[],
    name_mapping={},
)
class ArchiverProperties:
    def __init__(self) -> None:
        '''
        :stability: experimental
        '''
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ArchiverProperties(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "Archiver",
    "ArchiverProperties",
]

publication.publish()

def _typecheckingstub__59b1d445ea6a4ea2b344c5e83eb14b7e5d57e243d55dbad607605e1e2e63c1b5(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb1dff6681014d6e509e01d6b12c3974e4810c8d1a67b368174954a280d668f6(
    value: ArchiverProperties,
) -> None:
    """Type checking stubs"""
    pass
