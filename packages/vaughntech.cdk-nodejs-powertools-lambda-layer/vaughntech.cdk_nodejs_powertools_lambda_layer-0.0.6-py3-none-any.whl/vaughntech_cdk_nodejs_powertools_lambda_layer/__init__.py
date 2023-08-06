'''
# Description

This repo packages together a suite of utilities for AWS Lambda functions running on the Node.js runtime, to ease adopting best practices such as tracing, structured logging, custom metrics.'

# CDK Backup Plan

![Build](https://github.com/aws-samples/cdk-backup-plan/workflows/build/badge.svg)
![Release](https://github.com/aws-samples/cdk-backup-plan/workflows/release/badge.svg)

Provides an easy to use reusable CDK construct to create [Backup Plans](https://docs.aws.amazon.com/aws-backup/latest/devguide/about-backup-plans.html) using [AWS Backups](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html). It allows to indicate how frequently and what resources to backup.

> **NOTE:** More details on all the available arguments can be found [here](API.md)

## Install

NPM install:

```sh
npm install cdk-backup-plan
```

PyPi install:

```sh
pip install cdk-backup-plan
```

## Usage

```python
// ...
import { Runtime, Tracing } from 'aws-cdk-lib/aws-lambda';
import { NodejsFunction } from 'aws-cdk-lib/aws-lambda-nodejs';
import { ToolsLayer } from 'vaughntech-nodejs-powertools-lambdalayer';

// ...
const hello_world_lambda =  new NodejsFunction(this, 'helloworldLambda', {
    description: `Hello World Lambda`,
    label: 'HelloFnc',
    runtime: Runtime.NODEJS_16_X,
    memorySize = 128,
    timeout: Duration.seconds(10),
    logRetention = 30,
    tracing: Tracing.ACTIVE,
    entry: path.join(__dirname, '../../src/lambda/hello/index.ts'),
    functionProps: {
    timeout: 5,
    layers: [
        toolsLayer,
    ]
});
// ...
```

Python usage:

```python
# ...
from cdk_backup_plan import Backup

# ...
vpc = ec2.Vpc(self, "TestVPC")
engine = rds.DatabaseInstanceEngine.postgres(
    version=rds.PostgresEngineVersion.VER_12_3,
)
db = rds.DatabaseInstance(self, "TestInstance",
    engine=engine,
    vpc=vpc,
    credentials=rds.Credentials.from_generated_secret("postgres"),
)
Backup(self, "TestBk",
    backup_plan_name="TestPkPlan",
    backup_rate_hour=3,
    backup_completion_window=Duration.hours(2),
    resources=[bk.BackupResource.from_rds_database_instance(db)],
)
# ...
```

> **NOTE:** [Tagging](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_backup.BackupResource.html#static-fromwbrtagkey-value-operation) and/or [ARN](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_backup.BackupResource.html#static-fromwbrarnarn) can be used to reference resources not directly available in the [static methods section](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_backup.BackupResource.html#methods).
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

import aws_cdk.aws_lambda as _aws_cdk_aws_lambda_ceddda9d
import constructs as _constructs_77d1e7e8


@jsii.interface(
    jsii_type="vaughntech-nodejs-powertools-lambdalayer.IExampleConstructProps"
)
class IExampleConstructProps(typing_extensions.Protocol):
    @builtins.property
    @jsii.member(jsii_name="layerVersionName")
    def layer_version_name(self) -> builtins.str:
        ...

    @layer_version_name.setter
    def layer_version_name(self, value: builtins.str) -> None:
        ...


class _IExampleConstructPropsProxy:
    __jsii_type__: typing.ClassVar[str] = "vaughntech-nodejs-powertools-lambdalayer.IExampleConstructProps"

    @builtins.property
    @jsii.member(jsii_name="layerVersionName")
    def layer_version_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "layerVersionName"))

    @layer_version_name.setter
    def layer_version_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__088af38a28aa2c9dec5a20feb9ad69edb9fc6d570956ae1d434456f86fc0d79b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "layerVersionName", value)

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IExampleConstructProps).__jsii_proxy_class__ = lambda : _IExampleConstructPropsProxy


class ToolsLayer(
    _constructs_77d1e7e8.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="vaughntech-nodejs-powertools-lambdalayer.ToolsLayer",
):
    '''Create a Lambda layer with the PowerTools and other required modules.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        props: typing.Optional[IExampleConstructProps] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b57d6a82c5ec533f684923f36c124ea48f9bab4d60ba9c19a3142c3b3e8856b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        jsii.create(self.__class__, self, [scope, id, props])

    @builtins.property
    @jsii.member(jsii_name="layerVersion")
    def layer_version(self) -> _aws_cdk_aws_lambda_ceddda9d.LayerVersion:
        '''Lambda Layer.'''
        return typing.cast(_aws_cdk_aws_lambda_ceddda9d.LayerVersion, jsii.get(self, "layerVersion"))

    @layer_version.setter
    def layer_version(self, value: _aws_cdk_aws_lambda_ceddda9d.LayerVersion) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__87778e603b0a38c04b3a6eb6c16f71e251411c7b9b471cb48ed355ed5ef3cda9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "layerVersion", value)


__all__ = [
    "IExampleConstructProps",
    "ToolsLayer",
]

publication.publish()

def _typecheckingstub__088af38a28aa2c9dec5a20feb9ad69edb9fc6d570956ae1d434456f86fc0d79b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b57d6a82c5ec533f684923f36c124ea48f9bab4d60ba9c19a3142c3b3e8856b(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    props: typing.Optional[IExampleConstructProps] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87778e603b0a38c04b3a6eb6c16f71e251411c7b9b471cb48ed355ed5ef3cda9(
    value: _aws_cdk_aws_lambda_ceddda9d.LayerVersion,
) -> None:
    """Type checking stubs"""
    pass
