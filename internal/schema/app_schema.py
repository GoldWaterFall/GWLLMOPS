#!/usr/bin/env-python
# -*- coding: utf-8 -*-
"""
@Time 2025-03-07 1:12
@Author ShiqiDing
@File app_schema.py
"""
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class CompletionReq(FlaskForm):
    query = StringField('query',
                        validators=[DataRequired(message="用户提问是必填的"),
                                    Length(max=2000, message="用户提问最大长度是2000")
                                    ]
                        )
