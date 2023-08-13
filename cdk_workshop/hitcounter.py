from constructs import Construct
from aws_cdk import aws_lambda as _lambda
from aws_cdk import aws_dynamodb as ddb

class HitCounter(Construct):

    @property
    def handler(self):
        return self._handler
    

    def __init__(self, scope: Construct, id: str,
                 downstream: _lambda.IFunction, **kwargs):
        super().__init__(scope, id, **kwargs)

        table = ddb.Table(
            self, 'Hits',
            partition_key = {'name': 'path', 'type': ddb.AttributeType.STRING}
        )

        self._handler = _lambda.Function(
            self, 'HitCountHandler',
            runtime = _lambda.Runtime.PYTHON_3_7,
            handler='hitcount.handler',
            environment={'DOWNSTREAM_FUNCTION_NAME': downstream.fuction_name,
                         'HITS_TABLE_NAME': table.table_name}
        )