#给app取别名为 'index'
from flask import Blueprint

index_blu=Blueprint('index',__name__,template_folder='templates',static_folder='static')
from .views import *