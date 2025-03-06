#!/usr/bin/env-python
# -*- coding: utf-8 -*-
"""
@Time 2025-03-07 2:11
@Author ShiqiDing
@File expection.py
"""
from dataclasses import field
from typing import Any

from pkg.response import HttpCode


class CustomExpection(Exception):
    '''基础自定义异常信息'''
    code: HttpCode = HttpCode.FAIL
    message: str = ""
    data: Any = field(default_factory=dict)

    def __init__(self, message: str = None, data: Any = None):
        super().__init__(message)
        self.message = message
        self.data = data


class FailExpection(CustomExpection):
    '''通用失败异常'''
    pass


class NotFoundExpection(CustomExpection):
    ''''未找到数据异常'''
    code = HttpCode.NOT_FOUND


class UnauthorizedExpection(CustomExpection):
    '''未授权异常'''
    code = HttpCode.UNAUTHORIZED


class ForbiddenExpection(CustomExpection):
    '''无权限异常'''
    code = HttpCode.FORBIDDEN


class ValidationExpection(CustomExpection):
    '''数据权限异常'''
    code = HttpCode.VALIDATE_ERROR
