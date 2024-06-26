from .models import *
from .exceptions.api_exception import *
from .api_helper import *
from .logger_helper import LoggerHelper
import logging

logger = logging.getLogger(__name__)


class Company:

    def __init__(self):
        self.logger_helper = LoggerHelper()

    def update_company(self, company_profile, api_client, DEBUG):
        if not company_profile:
            logger.info(f'Expecting the input to be either of the type - CompanyModel, dict or json while updating company for pid - {self.logger_helper.get_worker_pid()}')
        else:
            if isinstance(company_profile, dict):
                if 'company_id' in company_profile:
                    try:
                        api_client.update_company(CompanyModel.from_dictionary(company_profile))
                        if DEBUG:
                            logger.info(f'Company Profile updated successfully for pid - {self.logger_helper.get_worker_pid()}')
                    except APIException as inst:
                        if 401 <= inst.response_code <= 403:
                            logger.error(f"Unauthorized access sending event to Moesif. Please check your Application Id for pid - {self.logger_helper.get_worker_pid()}")
                        if DEBUG:
                            logger.info(f"Error while updating company, with status code [{inst.response_code}] for pid - {self.logger_helper.get_worker_pid()}")
                else:
                    logger.info(f'To update an company, an company_id field is required for pid - {self.logger_helper.get_worker_pid()}')

            elif isinstance(company_profile, CompanyModel):
                if company_profile.company_id is not None:
                    try:
                        api_client.update_company(company_profile)
                        if DEBUG:
                            logger.info(f'Company Profile updated successfully for pid - {self.logger_helper.get_worker_pid()}')
                    except APIException as inst:
                        if 401 <= inst.response_code <= 403:
                            logger.error(f"Unauthorized access sending event to Moesif. Please check your Application Id for pid - {self.logger_helper.get_worker_pid()}")
                        if DEBUG:
                            logger.info(f"Error while updating company, with status code [{inst.response_code}] for pid - {self.logger_helper.get_worker_pid()}")
                else:
                    logger.info(f'To update a company, a company_id field is required for pid - {self.logger_helper.get_worker_pid()}')
            else:
                try:
                    company_profile_json = APIHelper.json_deserialize(company_profile)
                    if 'company_id' in company_profile_json:
                        try:
                            api_client.update_company(CompanyModel.from_dictionary(company_profile_json))
                            if DEBUG:
                                logger.info(f'Company Profile updated successfully for pid - {self.logger_helper.get_worker_pid()}')
                        except APIException as inst:
                            if 401 <= inst.response_code <= 403:
                                logger.error(f"Unauthorized access sending event to Moesif. Please check your Application Id for pid - {self.logger_helper.get_worker_pid()}")
                            if DEBUG:
                                logger.info(f"Error while updating company, with status code [{inst.response_code}] for pid - {self.logger_helper.get_worker_pid()}")
                    else:
                        logger.info(f'To update a company, an company_id field is required for pid - {self.logger_helper.get_worker_pid()}')
                except:
                    logger.warning(f'Error while deserializing the json, please make sure the json is valid for pid - {self.logger_helper.get_worker_pid()}')

    def update_companies_batch(self, company_profiles, api_client, DEBUG):
        if not company_profiles:
            logger.info(f'Expecting the input to be either of the type - List of CompanyModel, dict or json while updating companies for pid - {self.logger_helper.get_worker_pid()}')
        else:
            if all(isinstance(company, dict) for company in company_profiles):
                if all('company_id' in company for company in company_profiles):
                    try:
                        batch_profiles = [CompanyModel.from_dictionary(d) for d in company_profiles]
                        api_client.update_companies_batch(batch_profiles)
                        if DEBUG:
                            logger.info(f'Company Profile updated successfully for pid - {self.logger_helper.get_worker_pid()}')
                    except APIException as inst:
                        if 401 <= inst.response_code <= 403:
                            logger.error(f"Unauthorized access sending event to Moesif. Please check your Application Id.for pid - {self.logger_helper.get_worker_pid()}")
                        if DEBUG:
                            logger.info(f"Error while updating companies, with status code [{inst.response_code}] for pid - {self.logger_helper.get_worker_pid()}")
                else:
                    logger.info(f'To update companies, an company_id field is required for pid - {self.logger_helper.get_worker_pid()}')

            elif all(isinstance(company, CompanyModel) for company in company_profiles):
                if all(company.company_id is not None for company in company_profiles):
                    try:
                        api_client.update_companies_batch(company_profiles)
                        if DEBUG:
                            logger.info(f'Company Profile updated successfully for pid - {self.logger_helper.get_worker_pid()}')
                    except APIException as inst:
                        if 401 <= inst.response_code <= 403:
                            logger.error(f"Unauthorized access sending event to Moesif. Please check your Application Id for pid - {self.logger_helper.get_worker_pid()}")
                        if DEBUG:
                            logger.info(f"Error while updating companies, with status code [{inst.response_code}] for pid - {self.logger_helper.get_worker_pid()}")
                else:
                    logger.info(f'To update companies, an company_id field is required for pid - {self.logger_helper.get_worker_pid()}')
            else:
                try:
                    company_profiles_json = [APIHelper.json_deserialize(d) for d in company_profiles]
                    if all(isinstance(company, dict) for company in company_profiles_json) and all(
                                    'company_id' in user for user in company_profiles_json):
                        try:
                            batch_profiles = [CompanyModel.from_dictionary(d) for d in company_profiles_json]
                            api_client.update_companies_batch(batch_profiles)
                            if DEBUG:
                                logger.info(f'Company Profile updated successfully for pid - {self.logger_helper.get_worker_pid()}')
                        except APIException as inst:
                            if 401 <= inst.response_code <= 403:
                                logger.error(f"Unauthorized access sending event to Moesif. Please check your Application Id for pid - {self.logger_helper.get_worker_pid()}")
                            if DEBUG:
                                logger.info(f"Error while updating companies, with status code [{inst.response_code}] for pid - {self.logger_helper.get_worker_pid()}")
                    else:
                        logger.info(f'To update companies, an company_id field is required for pid - {self.logger_helper.get_worker_pid()}')
                except:
                    logger.warning(f'Error while deserializing the json, please make sure the json is valid for pid - {self.logger_helper.get_worker_pid()}')
