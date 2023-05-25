# --*-- coding:utf-8 --*--
from flask import jsonify

from novel.api_1_0 import api
from novel.utils.response_code import RET


@api.route('/novel/tasks')
def get_tasks():
    """
    获取用户的任务列表
    :return: 任务详情
    """
    return jsonify(re_code=RET.OK, msg='查询成功')


@api.route('/novel/tasks', methods=['POST'])
def add_tasks():
    """
    新增一个任务
    :return: 返回响应结果
    """
    return jsonify(re_code=RET.OK, msg='查询成功')


@api.route('/novel/tasks/<int:task_id>', methods=['DELETE'])
def delete_tasks(task_id):
    """
    删除一个任务
    :return: 返回响应结果
    """
    return jsonify(re_code=RET.OK, msg='查询成功')


@api.route('/novel/tasks/<int:task_id>', methods=['PUT'])
def update_tasks(task_id):
    """
    修改一个任务
    :return: 返回响应结果
    """
    return jsonify(re_code=RET.OK, msg='查询成功')

# 子任务相关API

@api.route('/novel/subtasks')
def get_subtasks():
    """
    获取用户的任务列表
    :return: 任务详情
    """
    return jsonify(re_code=RET.OK, msg='查询成功')


@api.route('/novel/subtasks', methods=['POST'])
def add_subtasks():
    """
    新增一个任务
    :return: 返回响应结果
    """
    return jsonify(re_code=RET.OK, msg='查询成功')


@api.route('/novel/subtasks/<int:task_id>', methods=['DELETE'])
def delete_subtasks(task_id):
    """
    删除一个任务
    :return: 返回响应结果
    """
    return jsonify(re_code=RET.OK, msg='查询成功')


@api.route('/novel/subtasks/<int:task_id>', methods=['PUT'])
def update_subtasks(task_id):
    """
    修改一个任务
    :return: 返回响应结果
    """
    return jsonify(re_code=RET.OK, msg='查询成功')
