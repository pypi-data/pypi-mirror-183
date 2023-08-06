from invoke import Program, Collection
from dbtest import tasks

program = Program(version="0.1.0", namespace=Collection.from_module(tasks))
