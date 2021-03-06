# -*- coding: utf-8 -*-
# Copyright: (c) 2018, Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.cli.arguments import option_helpers as opt_help


def test_version():
    ver = opt_help.version('ansible-cli-test')
    assert 'ansible-cli-test' in ver
    assert 'python version' in ver
