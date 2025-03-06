#!/usr/bin/env-python
# -*- coding: utf-8 -*-
"""
@Time 2025-03-06 5:36
@Author ShiqiDing
@File app_handler.py
"""
import os

from flask import request
from openai import OpenAI

from internal.exception import FailExpection
from internal.schema.app_schema import CompletionReq
from pkg.response import success_json, validate_error_json


class AppHandler:
    '''应用控制器'''

    def ping(self):
        raise FailExpection("数据未找到")

    def completion(self):
        '''聊天接口'''
        # 1.提取从接口中获得的输入，POST
        req = CompletionReq()
        if not req.validate():
            return validate_error_json(req.errors)

        query = request.json.get("query")
        # 2.构建openai客户端并发起请求
        client = OpenAI(
            # api_key=os.environ.get("OPENAI_API_KEY"),
            base_url=os.getenv("OPENAI_API_BASE")
        )
        # 3.得到请求响应，并将openai的响应结果给前端
        completion = client.chat.completions.create(model="qwen-plus-latest",
                                                    messages=[
                                                        {"role": "system",
                                                         "content": "你是聊天机器人，请根据用户的输入回复对应信息"},
                                                        {"role": "user", "content": query}
                                                    ])
        content = completion.choices[0].message.content

        return success_json({"content": content})
