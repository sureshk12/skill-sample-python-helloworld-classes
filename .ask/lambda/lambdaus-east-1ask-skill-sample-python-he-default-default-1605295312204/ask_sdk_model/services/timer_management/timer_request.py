# coding: utf-8

#
# Copyright 2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You may not use this file
# except in compliance with the License. A copy of the License is located at
#
# http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for
# the specific language governing permissions and limitations under the License.
#

import pprint
import re  # noqa: F401
import six
import typing
from enum import Enum


if typing.TYPE_CHECKING:
    from typing import Dict, List, Optional, Union, Any
    from datetime import datetime
    from ask_sdk_model.services.timer_management.creation_behavior import CreationBehavior as CreationBehavior_c34ad8fe
    from ask_sdk_model.services.timer_management.triggering_behavior import TriggeringBehavior as TriggeringBehavior_71806894


class TimerRequest(object):
    """
    Input request for creating a timer.


    :param duration: An ISO-8601 representation of duration. E.g. for 2 minutes and 3 seconds - \&quot;PT2M3S\&quot;.
    :type duration: (optional) str
    :param timer_label: Label of this timer alert, maximum of 256 characters.
    :type timer_label: (optional) str
    :param creation_behavior: 
    :type creation_behavior: (optional) ask_sdk_model.services.timer_management.creation_behavior.CreationBehavior
    :param triggering_behavior: 
    :type triggering_behavior: (optional) ask_sdk_model.services.timer_management.triggering_behavior.TriggeringBehavior

    """
    deserialized_types = {
        'duration': 'str',
        'timer_label': 'str',
        'creation_behavior': 'ask_sdk_model.services.timer_management.creation_behavior.CreationBehavior',
        'triggering_behavior': 'ask_sdk_model.services.timer_management.triggering_behavior.TriggeringBehavior'
    }  # type: Dict

    attribute_map = {
        'duration': 'duration',
        'timer_label': 'timerLabel',
        'creation_behavior': 'creationBehavior',
        'triggering_behavior': 'triggeringBehavior'
    }  # type: Dict
    supports_multiple_types = False

    def __init__(self, duration=None, timer_label=None, creation_behavior=None, triggering_behavior=None):
        # type: (Optional[str], Optional[str], Optional[CreationBehavior_c34ad8fe], Optional[TriggeringBehavior_71806894]) -> None
        """Input request for creating a timer.

        :param duration: An ISO-8601 representation of duration. E.g. for 2 minutes and 3 seconds - \&quot;PT2M3S\&quot;.
        :type duration: (optional) str
        :param timer_label: Label of this timer alert, maximum of 256 characters.
        :type timer_label: (optional) str
        :param creation_behavior: 
        :type creation_behavior: (optional) ask_sdk_model.services.timer_management.creation_behavior.CreationBehavior
        :param triggering_behavior: 
        :type triggering_behavior: (optional) ask_sdk_model.services.timer_management.triggering_behavior.TriggeringBehavior
        """
        self.__discriminator_value = None  # type: str

        self.duration = duration
        self.timer_label = timer_label
        self.creation_behavior = creation_behavior
        self.triggering_behavior = triggering_behavior

    def to_dict(self):
        # type: () -> Dict[str, object]
        """Returns the model properties as a dict"""
        result = {}  # type: Dict

        for attr, _ in six.iteritems(self.deserialized_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else
                    x.value if isinstance(x, Enum) else x,
                    value
                ))
            elif isinstance(value, Enum):
                result[attr] = value.value
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else
                    (item[0], item[1].value)
                    if isinstance(item[1], Enum) else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        # type: () -> str
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        # type: () -> str
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        # type: (object) -> bool
        """Returns true if both objects are equal"""
        if not isinstance(other, TimerRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        # type: (object) -> bool
        """Returns true if both objects are not equal"""
        return not self == other
