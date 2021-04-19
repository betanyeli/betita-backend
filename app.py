#!/usr/bin/env python3

from aws_cdk import core

from beta.src.beta_stack import BetaStack

app = core.App()
BetaStack(app, "AppSyncGraphQLDynamoDBExample")

app.synth()
