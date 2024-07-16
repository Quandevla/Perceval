# MIT License
#
# Copyright (c) 2022 Quandela
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# As a special exception, the copyright holders of exqalibur library give you
# permission to combine exqalibur with code included in the standard release of
# Perceval under the MIT license (or modified versions of such code). You may
# copy and distribute such a combined system following the terms of the MIT
# license for both exqalibur and Perceval. This exception for the usage of
# exqalibur is limited to the python bindings used by Perceval.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
"""module test rpc handler"""

from _mock_rpc_handler import get_rpc_handler


def test_build_endpoint(requests_mock):
    """test build endpoint function"""
    rpc = get_rpc_handler(requests_mock, url='https://example.org')
    wanted = 'https://example.org/end'
    assert rpc.build_endpoint('/end') == wanted
    wanted = 'https://example.org/end/id'
    assert rpc.build_endpoint('/end', 'id') == wanted
    wanted = 'https://example.org/end/path/id'
    assert rpc.build_endpoint('/end', 'path', 'id') == wanted


def test_rpc_handler(requests_mock):
    """test rpc handler calls"""
    rpc = get_rpc_handler(requests_mock, url='https://example.org')
    resp_details = rpc.fetch_platform_details()
    assert 'name' in resp_details
    id_job = rpc.create_job({})
    assert isinstance(id_job, str)
    resp_status = rpc.get_job_status(id_job)
    assert resp_status['msg'] == 'ok'
    rpc.cancel_job(id_job)
    resp_result = rpc.get_job_results(id_job)
    assert 'results' in resp_result