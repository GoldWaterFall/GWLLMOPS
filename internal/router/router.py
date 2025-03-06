#!/usr/bin/env-python
# -*- coding: utf-8 -*-
"""
@Time 2025-03-06 5:38
@Author ShiqiDing
@File router.py
"""
from dataclasses import dataclass

from flask import Flask, Blueprint
from injector import inject

from internal.handler import AppHandler


@inject
@dataclass
class Router:
    '''路由'''
    app_handler: AppHandler

    def register_router(self, app: Flask):
        '''注册路由'''
        # 1.创建一个蓝图
        bp = Blueprint("llmops", __name__, url_prefix="")

        # 2.将url与对应控制器做绑定
        bp.add_url_rule("/ping", methods=["GET", "POST", "DELETE"], view_func=self.app_handler.ping)
        bp.add_url_rule("/app/completion", methods=["POST"], view_func=self.app_handler.completion)
        # 3.在应用上去注册蓝图
        app.register_blueprint(bp)
