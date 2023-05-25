# --*-- coding:utf-8 --*--
from flask import jsonify, g, current_app, request

from novel import db
from novel.api_1_0 import api
from novel.models.novel_models import NovelTask
from novel.utils.common import login_required
from novel.utils.response_code import RET


@api.route('/novel/tasks')
@login_required
def get_tasks():
    """
    获取用户的任务列表
    :return: 任务详情
    """
    novelTasks = None
    try:
        novelTasks = NovelTask.query.filter(NovelTask.user_id == g.user_id).all()
    except Exception as e:
        current_app.logger.debug(e)
    if not novelTasks:
        return jsonify(re_code=RET.NODATA, msg='无任务信息')
    novelTasks = [novelTask.to_dict() for novelTask in novelTasks]
    return jsonify(re_code=RET.OK, msg='查询任务成功', data={'novelTasks': novelTasks})


@api.route('/novel/tasks', methods=['POST'])
@login_required
def add_tasks():
    """
    新增一个任务
    :return: 返回响应结果
    """
    # 1.前端获取房屋信息并校验数据
    json_dict = request.json
    story = json_dict.get('story')
    category = json_dict.get('category')
    story_name = json_dict.get('story_name')
    user_id = g.user_id
    if not all(
            [story, category, story_name, user_id]):
        return jsonify(re_code=RET.PARAMERR, msg='参数不完整')

    # 2.保存数据到数据库
    novelTask = NovelTask()
    novelTask.user_id = user_id
    novelTask.category = category
    novelTask.story_name = story_name
    novelTask.user_id = user_id

    try:
        db.session.add(novelTask)
        db.session.commit()
    except Exception as e:
        current_app.logger.debug(e)
        db.session.rollback()
        return jsonify(re_code=RET.DBERR, msg='新增任务失败')
    # 3.返回响应house_id
    return jsonify(re_code=RET.OK, msg='新增任务成功', data={'task': novelTask.id})


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
