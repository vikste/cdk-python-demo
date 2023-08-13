from constructs import Construct
from aws_cdk import Stack
from aws_cdk import aws_lambda as _lambda
from aws_cdk import aws_apigateway as apigw

class CdkWorkshopStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs):
        super().__init__(scope, construct_id, **kwargs)

        # defines an AWS Lambda resource
        my_lambda = _lambda.Function(
            self, "HelloHandler",
            runtime = _lambda.Runtime.PYTHON_3_7,
            code = _lambda.Code.from_asset('lambda'),
            handler = 'hello.handler',
        )

        apigw.LambdaRestApi(self, "Endpoint", handler=my_lambda)
