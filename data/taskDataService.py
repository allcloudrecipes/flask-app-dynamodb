from __future__ import print_function
from models.task import Task
import boto3


class TaskDataService:
    def __init__(self):
        self.dynamodb = boto3.resource('dynamodb', region_name='us-east-2')
        self.table = self.dynamodb.Table('TASKS')

    def create(self, task_id, task_name):
        self.table.put_item(
            Item={
                'TaskId': task_id,
                'TaskName': task_name
            }
        )

    def delete(self, task_id):
        self.table.delete_item(
            Item={
                'TaskId': task_id
            }
        )

    def list(self):
        tasks = []
        response = self.table.scan()
        for item in response['Items']:
            tasks.append(Task(item))
        return tasks
