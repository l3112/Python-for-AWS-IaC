#!/usr/bin/env python
#This code is from 
#https://learn.hashicorp.com/tutorials/terraform/cdktf-build-python?in=terraform/cdktf
# but I have things to say about it as
# a semi-new Python user
from constructs import Construct
from cdktf import App, TerraformStack, TerraformOutput
from imports.aws import AwsProvider, ec2


class MyStack(TerraformStack):
  def __init__(self, scope: Construct, ns: str):
    super().__init__(scope, ns)

    AwsProvider(self, "Aws", region="us-west-1")

    helloInstance = ec2.Instance(self, "hello",
      ami="ami-01456a894f71116f2",
      instance_type="t2.micro",
      tags={"Name": "Pyth-Dem"}
    )

    TerraformOutput(self, "hello_public_ip",
      value=helloInstance.public_ip
    )

app = App()
MyStack(app, "hello-terraform")

app.synth()
