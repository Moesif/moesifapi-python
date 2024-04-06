from datetime import datetime
from ..exceptions.api_exception import *
import json
from .regex_config_helper import RegexConfigHelper
import logging

logger = logging.getLogger(__name__)

# Application Configuration
class AppConfig:
    def __init__(self):
        self.regex_config_helper = RegexConfigHelper()
        return

    def get_config(self, api_client, debug):
        """Get Config"""
        try:
            config_api_response = api_client.get_app_config()
            return config_api_response
        except APIException as inst:
            if 401 <= inst.response_code <= 403:
                logger.warning("Unauthorized access getting application configuration. Please check your Appplication Id.")
            if debug:
                logger.info(f"Error getting application configuration, with status code: {str(inst.response_code)}")

    def parse_configuration(self, config, debug):
        """Parse configuration object and return Etag, sample rate and last updated time"""
        try:
            return config.headers.get("X-Moesif-Config-ETag"), json.loads(config.raw_body).get('sample_rate', 100), datetime.utcnow()
        except:
            if debug:
                logger.info('Error while parsing the configuration object, setting the sample rate to default')
            return None, 100, datetime.utcnow()

    def get_sampling_percentage(self, event_data, config, user_id, company_id):
        """Get sampling percentage"""

        if config is not None:
            try:
                config_body = json.loads(config.raw_body)

                user_sample_rate = config_body.get('user_sample_rate', None)

                company_sample_rate = config_body.get('company_sample_rate', None)

                regex_config = config_body.get('regex_config', None)

                if regex_config:
                    config_mapping = self.regex_config_helper.prepare_config_mapping(event_data)
                    regex_sample_rate = self.regex_config_helper.fetch_sample_rate_on_regex_match(regex_config, config_mapping)
                    if regex_sample_rate is not None:
                        return regex_sample_rate

                if user_id and user_sample_rate and user_id in user_sample_rate:
                    return user_sample_rate[user_id]

                if company_id and company_sample_rate and company_id in company_sample_rate:
                    return company_sample_rate[company_id]

                return config_body.get('sample_rate', 100)

            except Exception as e:
                logger.warning(f"Error while parsing user or company sample rate: {str(e)}")

        # Use default
        return 100
