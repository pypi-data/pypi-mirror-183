'''
# Description:

This repo packages together a suite of utilities for AWS Lambda functions running on the Node.js runtime, to ease adopting best practices such as tracing, structured logging, custom metrics.'
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
