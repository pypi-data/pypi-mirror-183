# Copyright 2021 Georges Racinet <georges.racinet@octobus.net>
#
# This software may be used and distributed according to the terms of the
# GNU General Public License version 2 or any later version.
#
# SPDX-License-Identifier: GPL-3.0-or-later


class PaasError(RuntimeError):
    """Used for errors encountered on PAAS."""
    def __init__(self, executor, action, code,
                 transport_code=None,  # used when different from code
                 action_details=None,
                 error_details=None):
        self.executor = executor
        self.action = action
        self.action_details = action_details
        self.transport_code = transport_code
        self.code = code
        self.error_details = error_details
        self.args = (executor, action, code)


class PaasProvisioningError(PaasError):
    """Used for errors encountered while provisioning on PAAS."""


class PaasResourceError(PaasError):
    """Errors encountered on an already provisioned PAAS resource."""

    def __init__(self, resource_id, *args, **kwargs):
        super(PaasResourceError, self).__init__(*args, **kwargs)
        self.resource_id = resource_id
        self.args = (resource_id, ) + self.args


class GitLabError(RuntimeError):
    """Used for errors encountered in interactions with GitLab."""

    def __init__(self, url, status_code, params, message):
        self.url = url
        self.status_code = status_code
        self.params = params
        self.message = message
        self.args = (url, status_code, params, message)


class GitLabUnavailableError(GitLabError):
    """Used when API is not reachable.

    This condition is often considered to be non permanent.
    """

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('params', None)
        kwargs.setdefault('status_code', None)
        super(GitLabUnavailableError, self).__init__(*args, **kwargs)


class GitLabUnexpectedError(GitLabError):
    """Used for HTTP status code that represent hard errors.
    """
