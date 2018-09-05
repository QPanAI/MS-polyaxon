# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

from polyaxon_schemas.code_reference import CodeReferenceConfig

from polyaxon_client.api.base import BaseApiHandler
from polyaxon_client.exceptions import PolyaxonException
from polyaxon_client.schemas import (
    ExperimentConfig,
    ExperimentJobConfig,
    ExperimentMetricConfig,
    ExperimentStatusConfig
)


class ExperimentApi(BaseApiHandler):
    """
    Api handler to get experiments from the server.
    """
    ENDPOINT = "/"

    def list_experiments(self, page=1):
        """This gets all experiments visible to the user from the server."""
        try:
            response = self.transport.get(self._get_http_url('/experiments'),
                                          params=self.get_page(page=page))
            return self.prepare_list_results(response.json(), page, ExperimentConfig)
        except PolyaxonException as e:
            self.transport.handle_exception(e=e, log_message='Error while retrieving experiments.')
            return []

    def get_experiment(self, username, project_name, experiment_id):
        request_url = self._build_url(self._get_http_url(),
                                      username,
                                      project_name,
                                      'experiments',
                                      experiment_id)
        try:
            response = self.transport.get(request_url)
            return self.prepare_results(response_json=response.json(), config=ExperimentConfig)
        except PolyaxonException as e:
            self.transport.handle_exception(e=e, log_message='Error while retrieving experiment.')
            return None

    def update_experiment(self,
                          username,
                          project_name,
                          experiment_id,
                          patch_dict,
                          background=False):
        request_url = self._build_url(self._get_http_url(),
                                      username,
                                      project_name,
                                      'experiments',
                                      experiment_id)

        if background:
            self.transport.async_patch(request_url, json_data=patch_dict)
            return None

        try:
            response = self.transport.patch(request_url, json_data=patch_dict)
            return self.prepare_results(response_json=response.json(), config=ExperimentConfig)
        except PolyaxonException as e:
            self.transport.handle_exception(e=e, log_message='Error while updating experiment.')
            return None

    def delete_experiment(self, username, project_name, experiment_id, background=False):
        request_url = self._build_url(self._get_http_url(),
                                      username,
                                      project_name,
                                      'experiments',
                                      experiment_id)

        if background:
            self.transport.async_delete(request_url)
            return None

        try:
            return self.transport.delete(request_url)
        except PolyaxonException as e:
            self.transport.handle_exception(e=e, log_message='Error while deleting experiment.')
            return None

    def get_statuses(self, username, project_name, experiment_id, page=1):
        request_url = self._build_url(self._get_http_url(),
                                      username,
                                      project_name,
                                      'experiments',
                                      experiment_id,
                                      'statuses')
        try:
            response = self.transport.get(request_url, params=self.get_page(page=page))
            return self.prepare_list_results(response.json(), page, ExperimentStatusConfig)
        except PolyaxonException as e:
            self.transport.handle_exception(
                e=e, log_message='Error while retrieving experiment statuses.')
            return None

    def create_status(self,
                      username,
                      project_name,
                      experiment_id,
                      status,
                      message=None,
                      background=False):
        request_url = self._build_url(self._get_http_url(),
                                      username,
                                      project_name,
                                      'experiments',
                                      experiment_id,
                                      'statuses')

        json_data = {'status': status}
        if message:
            json_data['message'] = message
        if background:
            self.transport.async_post(request_url, json_data=json_data)
            return None

        try:
            response = self.transport.post(request_url, json_data=json_data)
            return self.prepare_results(response_json=response.json(),
                                        config=ExperimentStatusConfig)
        except PolyaxonException as e:
            self.transport.handle_exception(
                e=e, log_message='Error while creating experiment status.')
            return None

    def get_code_reference(self,
                           username,
                           project_name,
                           experiment_id):
        request_url = self._build_url(self._get_http_url(),
                                      username,
                                      project_name,
                                      'experiments',
                                      experiment_id,
                                      'coderef')
        try:
            response = self.transport.get(request_url)
            return self.prepare_results(response.json(), CodeReferenceConfig)
        except PolyaxonException as e:
            self.transport.handle_exception(
                e=e, log_message='Error while retrieving experiment code reference.')
            return None

    def create_code_reference(self,
                              username,
                              project_name,
                              experiment_id,
                              coderef,
                              background=False):
        request_url = self._build_url(self._get_http_url(),
                                      username,
                                      project_name,
                                      'experiments',
                                      experiment_id,
                                      'coderef')
        if background:
            self.transport.async_post(request_url, json_data=coderef)
            return None

        try:
            response = self.transport.post(request_url, json_data=coderef)
            return self.prepare_results(response_json=response.json(),
                                        config=CodeReferenceConfig)
        except PolyaxonException as e:
            self.transport.handle_exception(
                e=e, log_message='Error while creating experiment coderef.')
            return None

    def get_metrics(self, username, project_name, experiment_id, page=1):
        request_url = self._build_url(self._get_http_url(),
                                      username,
                                      project_name,
                                      'experiments',
                                      experiment_id,
                                      'metrics')
        try:
            response = self.transport.get(request_url, params=self.get_page(page=page))
            return self.prepare_list_results(response.json(), page, ExperimentMetricConfig)
        except PolyaxonException as e:
            self.transport.handle_exception(
                e=e, log_message='Error while retrieving experiment metric.')
            return None

    def create_metric(self, username, project_name, experiment_id, values, background=False):
        request_url = self._build_url(self._get_http_url(),
                                      username,
                                      project_name,
                                      'experiments',
                                      experiment_id,
                                      'metrics')

        if background:
            self.transport.async_post(request_url, json_data={'values': values})
            return None

        try:
            response = self.transport.post(request_url, json_data={'values': values})
            return self.prepare_results(response_json=response.json(),
                                        config=ExperimentMetricConfig)
        except PolyaxonException as e:
            self.transport.handle_exception(
                e=e, log_message='Error while retrieving experiment status.')
            return None

    def list_jobs(self, username, project_name, experiment_id, page=1):
        """Fetch list of jobs related to this experiment."""
        request_url = self._build_url(self._get_http_url(),
                                      username,
                                      project_name,
                                      'experiments',
                                      experiment_id,
                                      'jobs')

        try:
            response = self.transport.get(request_url, params=self.get_page(page=page))
            return self.prepare_list_results(response.json(), page, ExperimentJobConfig)
        except PolyaxonException as e:
            self.transport.handle_exception(e=e, log_message='Error while retrieving jobs.')
            return []

    def restart(self,
                username,
                project_name,
                experiment_id,
                config=None,
                update_code=None,
                background=False):
        """Restart an experiment."""
        request_url = self._build_url(self._get_http_url(),
                                      username,
                                      project_name,
                                      'experiments',
                                      experiment_id,
                                      'restart')

        data = {}
        if config:
            data['config'] = config
        if update_code:
            data['update_code'] = update_code

        if background:
            self.transport.async_post(request_url, json_data=data)
            return None

        try:
            response = self.transport.post(request_url, json_data=data)
            return self.prepare_results(response_json=response.json(), config=ExperimentConfig)
        except PolyaxonException as e:
            self.transport.handle_exception(
                e=e, log_message='Error while restarting the experiment.')
            return None

    def resume(self,
               username,
               project_name,
               experiment_id,
               config=None,
               update_code=None,
               background=False):
        """Restart an experiment."""
        request_url = self._build_url(self._get_http_url(),
                                      username,
                                      project_name,
                                      'experiments',
                                      experiment_id,
                                      'resume')

        data = {}
        if config:
            data['config'] = config
        if update_code:
            data['update_code'] = update_code

        if background:
            self.transport.async_post(request_url, json_data=data)
            return None

        try:
            response = self.transport.post(request_url, json_data=data)
            return self.prepare_results(response_json=response.json(), config=ExperimentConfig)
        except PolyaxonException as e:
            self.transport.handle_exception(e=e, log_message='Error while resuming the experiment.')
            return None

    def copy(self,
             username,
             project_name,
             experiment_id,
             config=None,
             update_code=None,
             background=False):
        """Restart an experiment."""
        request_url = self._build_url(self._get_http_url(),
                                      username,
                                      project_name,
                                      'experiments',
                                      experiment_id,
                                      'copy')

        data = {}
        if config:
            data['config'] = config
        if update_code:
            data['update_code'] = update_code

        if background:
            self.transport.async_post(request_url, json_data=data)
            return None

        try:
            response = self.transport.post(request_url, json_data=data)
            return self.prepare_results(response_json=response.json(), config=ExperimentConfig)
        except PolyaxonException as e:
            self.transport.handle_exception(e=e, log_message='Error while copying the experiment.')
            return None

    def stop(self, username, project_name, experiment_id, background=False):
        request_url = self._build_url(self._get_http_url(),
                                      username,
                                      project_name,
                                      'experiments',
                                      experiment_id,
                                      'stop')

        if background:
            self.transport.async_post(request_url)
            return None

        try:
            return self.transport.post(request_url)
        except PolyaxonException as e:
            self.transport.handle_exception(e=e, log_message='Error while stopping experiment.')
            return None

    def resources(self, username, project_name, experiment_id, message_handler=None):
        """Streams experiments resources using websockets.

        message_handler: handles the messages received from server.
            e.g. def f(x): print(x)
        """
        request_url = self._build_url(self._get_ws_url(),
                                      username,
                                      project_name,
                                      'experiments',
                                      experiment_id,
                                      'resources')
        self.transport.socket(request_url, message_handler=message_handler)

    # pylint:disable=inconsistent-return-statements
    def logs(self, username, project_name, experiment_id, stream=True, message_handler=None):
        """Streams experiments logs using websockets.

        message_handler: handles the messages received from server.
            e.g. def f(x): print(x)
        """
        if not stream:
            request_url = self._build_url(self._get_http_url(),
                                          username,
                                          project_name,
                                          'experiments',
                                          experiment_id,
                                          'logs')

            try:
                return self.transport.get(request_url)
            except PolyaxonException as e:
                self.transport.handle_exception(e=e, log_message='Error while retrieving jobs.')
                return []

        request_url = self._build_url(self._get_ws_url(),
                                      username,
                                      project_name,
                                      'experiments',
                                      experiment_id,
                                      'logs')
        self.transport.socket(request_url, message_handler=message_handler)

    def start_tensorboard(self,
                          username,
                          project_name,
                          experiment_id,
                          job_config=None,
                          background=False):
        request_url = self._build_url(self._get_http_url(),
                                      username,
                                      project_name,
                                      'experiments',
                                      experiment_id,
                                      'tensorboard',
                                      'start')

        job_config = {'config': job_config} if job_config else {}

        if background:
            self.transport.async_post(request_url, json_data=job_config)
            return None

        try:
            return self.transport.post(request_url, json_data=job_config)
        except PolyaxonException as e:
            self.transport.handle_exception(e=e, log_message='Error while starting tensorboard.')
            return None

    def stop_tensorboard(self, username, project_name, experiment_id, background=False):
        request_url = self._build_url(self._get_http_url(),
                                      username,
                                      project_name,
                                      'experiments',
                                      experiment_id,
                                      'tensorboard',
                                      'stop')

        if background:
            self.transport.async_post(request_url)
            return None

        try:
            return self.transport.post(request_url)
        except PolyaxonException as e:
            self.transport.handle_exception(e=e, log_message='Error while stopping tensorboard.')
            return None

    def bookmark(self, username, project_name, experiment_id, background=False):
        request_url = self._build_url(self._get_http_url(),
                                      username,
                                      project_name,
                                      'experiments',
                                      experiment_id,
                                      'bookmark')

        if background:
            self.transport.async_post(request_url)
            return None

        try:
            return self.transport.post(request_url)
        except PolyaxonException as e:
            self.transport.handle_exception(e=e, log_message='Error while bookmarking experiment.')
            return None

    def unbookmark(self, username, project_name, experiment_id, background=False):
        request_url = self._build_url(self._get_http_url(),
                                      username,
                                      project_name,
                                      'experiments',
                                      experiment_id,
                                      'unbookmark')

        if background:
            self.transport.async_delete(request_url)
            return None

        try:
            return self.transport.delete(request_url)
        except PolyaxonException as e:
            self.transport.handle_exception(
                e=e, log_message='Error while unbookmarking experiment.')
            return None

    def download_outputs(self, username, project_name, experiment_id):
        """Downloads outputs for this experiment to the current dir."""
        request_url = self._build_url(self._get_http_url(),
                                      username,
                                      project_name,
                                      'experiments',
                                      experiment_id,
                                      'outputs')

        try:
            response = self.transport.download(
                request_url,
                '{}.{}.{}.tar.gz'.format(username, project_name, experiment_id))
            return response
        except PolyaxonException as e:
            self.transport.handle_exception(
                e=e, log_message='Error while downloading experiment outputs.')
            return None
