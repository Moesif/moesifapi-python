from .models import *
from .exceptions.api_exception import *
from .api_helper import *
from .logger_helper import LoggerHelper
import logging

logger = logging.getLogger(__name__)

class User:

    def __init__(self):
        self.logger_helper = LoggerHelper()

    def update_user(self, user_profile, api_client, DEBUG):
        if not user_profile:
            logger.info(f'Expecting the input to be either of the type - UserModel, dict or json while updating user for pid - {self.logger_helper.get_worker_pid()}')
        else:
            if isinstance(user_profile, dict):
                if 'user_id' in user_profile:
                    try:
                        api_client.update_user(UserModel.from_dictionary(user_profile))
                        if DEBUG:
                            logger.info(f'User Profile updated successfully for pid - {self.logger_helper.get_worker_pid()}')
                    except APIException as inst:
                        if 401 <= inst.response_code <= 403:
                            logger.error(f"Unauthorized access sending event to Moesif. Please check your Application Id for pid - {self.logger_helper.get_worker_pid()}")
                        if DEBUG:
                            logger.info(f"Error while updating user, with status code [{inst.response_code}] for pid - {self.logger_helper.get_worker_pid()}")
                else:
                    logger.info(f'To update an user, an user_id field is required for pid - {self.logger_helper.get_worker_pid()}')

            elif isinstance(user_profile, UserModel):
                if user_profile.user_id is not None:
                    try:
                        api_client.update_user(user_profile)
                        if DEBUG:
                            logger.info(f'User Profile updated successfully for pid - {self.logger_helper.get_worker_pid()}')
                    except APIException as inst:
                        if 401 <= inst.response_code <= 403:
                            logger.error(f"Unauthorized access sending event to Moesif. Please check your Application Id for pid - {self.logger_helper.get_worker_pid()}")
                        if DEBUG:
                            logger.info(f"Error while updating user, with status code [{inst.response_code}] for pid - {self.logger_helper.get_worker_pid()}")
                else:
                    logger.info(f'To update an user, an user_id field is required for pid - [{self.logger_helper.get_worker_pid()}]')
            else:
                try:
                    user_profile_json = APIHelper.json_deserialize(user_profile)
                    if 'user_id' in user_profile_json:
                        try:
                            api_client.update_user(UserModel.from_dictionary(user_profile_json))
                            if DEBUG:
                                logger.info(f'User Profile updated successfully for pid - {self.logger_helper.get_worker_pid()}')
                        except APIException as inst:
                            if 401 <= inst.response_code <= 403:
                                logger.error(f"Unauthorized access sending event to Moesif. Please check your Application Id for pid - {self.logger_helper.get_worker_pid()}")
                            if DEBUG:
                                logger.info(f"Error while updating user, with status code [{inst.response_code}] for pid - {self.logger_helper.get_worker_pid()}")
                    else:
                        logger.info(f'To update an user, an user_id field is required for pid - {self.logger_helper.get_worker_pid()}')
                except:
                    logger.warning(f'Error while deserializing the json, please make sure the json is valid for pid - {self.logger_helper.get_worker_pid()}')

    def update_users_batch(self, user_profiles, api_client, DEBUG):
        if not user_profiles:
            logger.info(f'Expecting the input to be either of the type - List of UserModel, dict or json while updating users for pid - {self.logger_helper.get_worker_pid()}')
        else:
            if all(isinstance(user, dict) for user in user_profiles):
                if all('user_id' in user for user in user_profiles):
                    try:
                        batch_profiles = [UserModel.from_dictionary(d) for d in user_profiles]
                        api_client.update_users_batch(batch_profiles)
                        if DEBUG:
                            logger.info(f'User Profile updated successfully for pid - {self.logger_helper.get_worker_pid()}')
                    except APIException as inst:
                        if 401 <= inst.response_code <= 403:
                            logger.error(f"Unauthorized access sending event to Moesif. Please check your Application Id for pid - {self.logger_helper.get_worker_pid()}")
                        if DEBUG:
                            logger.info(f"Error while updating users, with status code [{inst.response_code}] for pid - {self.logger_helper.get_worker_pid()}")
                else:
                    logger.info(f'To update users, an user_id field is required for pid - {self.logger_helper.get_worker_pid()}')

            elif all(isinstance(user, UserModel) for user in user_profiles):
                if all(user.user_id is not None for user in user_profiles):
                    try:
                        api_client.update_users_batch(user_profiles)
                        if DEBUG:
                            logger.info(f'User Profile updated successfully for pid - {self.logger_helper.get_worker_pid()}')
                    except APIException as inst:
                        if 401 <= inst.response_code <= 403:
                            logger.error(f"Unauthorized access sending event to Moesif. Please check your Application Id for pid - {self.logger_helper.get_worker_pid()}")
                        if DEBUG:
                            logger.info(f"Error while updating users, with status code [{inst.response_code}] for pid - {self.logger_helper.get_worker_pid()}")
                else:
                    logger.info(f'To update users, an user_id field is required for pid - {self.logger_helper.get_worker_pid()}')
            else:
                try:
                    user_profiles_json = [APIHelper.json_deserialize(d) for d in user_profiles]
                    if all(isinstance(user, dict) for user in user_profiles_json) and all(
                                    'user_id' in user for user in user_profiles_json):
                        try:
                            batch_profiles = [UserModel.from_dictionary(d) for d in user_profiles_json]
                            api_client.update_users_batch(batch_profiles)
                            if DEBUG:
                                logger.info(f'User Profile updated successfully for pid - {self.logger_helper.get_worker_pid()}')
                        except APIException as inst:
                            if 401 <= inst.response_code <= 403:
                                logger.error(f"Unauthorized access sending event to Moesif. Please check your Application Id for pid - {self.logger_helper.get_worker_pid()}")
                            if DEBUG:
                                logger.info(f"Error while updating users, with status code [{inst.response_code}] for pid - {self.logger_helper.get_worker_pid()}")
                    else:
                        logger.info(f'To update users, an user_id field is required for pid - {self.logger_helper.get_worker_pid()}')
                except:
                    logger.warning(f'Error while deserializing the json, please make sure the json is valid for pid - {self.logger_helper.get_worker_pid()}')
