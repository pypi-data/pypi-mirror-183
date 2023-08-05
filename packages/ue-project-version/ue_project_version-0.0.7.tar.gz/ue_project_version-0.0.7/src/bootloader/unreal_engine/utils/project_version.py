# Copyright (C) 2022 Bootloader.  All rights reserved.
#
# This software is the confidential and proprietary information of
# Bootloader or one of its subsidiaries.  You shall not disclose this
# confidential information and shall use it only in accordance with the
# terms of the license agreement or other applicable agreement you
# entered into with Bootloader.
#
# BOOTLOADER MAKES NO REPRESENTATIONS OR WARRANTIES ABOUT THE
# SUITABILITY OF THE SOFTWARE, EITHER EXPRESS OR IMPLIED, INCLUDING BUT
# NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR
# A PARTICULAR PURPOSE, OR NON-INFRINGEMENT.  BOOTLOADER SHALL NOT BE
# LIABLE FOR ANY LOSSES OR DAMAGES SUFFERED BY LICENSEE AS A RESULT OF
# USING, MODIFYING OR DISTRIBUTING THIS SOFTWARE OR ITS DERIVATIVES.

from pathlib import Path
import configparser
import os
import re
import sys

from majormode.perseus.model.version import Version


DEFAULT_VERSION = Version(0, 0, 1)

UNREAL_ENGINE_CONFIG_PROPERTY_PROJECT_VERSION = 'ProjectVersion'

REGEX_PATTERN_PROPERTY = rf'^{UNREAL_ENGINE_CONFIG_PROPERTY_PROJECT_VERSION}\s*=\s*([a-zA-Z0-9\.\-]+)\s*$'
REGEX_PROPERTY = re.compile(REGEX_PATTERN_PROPERTY)


def find_project_version_ini_file(
        path: Path,
        require_semantic_versioning: bool = False) -> str or Version:
    """
    Return the project version of an Unreal Engine project.


    The version of an Unreal Engine project is identified in the attribute
    `ProjectVersion` of the section
    `[/Script/EngineSettings.GeneralProjectSettings]` of the configuration
    file `DefaultGame.ini` located in the folder `$ROOT_PATH/Config` of
    the Unreal Engine project.

    https://docs.unrealengine.com/5.0/en-US/configuration-files-in-unreal-engine/


    @param path: The absolute path to the root folder of an Unreal Engine
        project.

    @param require_semantic_versioning: Indicate whether the version
        identified in the configuration file of the Unreal Engine project
        MUST comply with Semantic Versioning.


    @return: The version of the Unreal Engine project.


    @raise ValueError: If the configuration file of the Unreal Engine
        project has not been found, or if the property corresponding to
        the project version is not defined in the configuration file, or
        if the project version is not compliant with Semantic Versioning
        when required.
    """
    if not path.exists():
        raise ValueError(f"The path {path} doesn't exist")

    config_file_path = Path().joinpath(path.expanduser(), 'Config', 'DefaultGame.ini')

    # config_parser = configparser.ConfigParser()
    # config_parser.read(config_file_path)

    with open(config_file_path, 'rt') as fd:
        lines = fd.readlines()

    for line in lines:
        regex_match = REGEX_PROPERTY.match(line.strip())
        if regex_match:
            project_version = regex_match.group(1)

            if require_semantic_versioning:
                project_version = Version(project_version)

            return project_version

    raise ValueError(f"The Unreal Engine project has no version defined in the configuration file {config_file_path}")


def update_project_version_ini_file(
        path: Path,
        version: str or Version) -> None:
    """
    Update the project version of an Unreal Engine project.


    The version of an Unreal Engine project is identified in the attribute
    `ProjectVersion` of the section
    `[/Script/EngineSettings.GeneralProjectSettings]` of the configuration
    file `DefaultGame.ini` located in the folder `$ROOT_PATH/Config` of
    the Unreal Engine project.

    https://docs.unrealengine.com/5.0/en-US/configuration-files-in-unreal-engine/


    @param path: The absolute path to the root folder of an Unreal Engine
        project.

    @param version: The version to write inn the Unreal Engine project
        configuration file.
    """
    if not path.exists():
        raise ValueError(f"The path {path} doesn't exist")

    config_file_path = Path().joinpath(path.expanduser(), 'Config', 'DefaultGame.ini')

    with open(config_file_path, 'rt') as fd:
        lines = fd.readlines()

    is_project_version_defined = False

    for i in range(len(lines)):
        regex_match = REGEX_PROPERTY.match(lines[i].strip())
        if regex_match:
            lines[i] = f'{UNREAL_ENGINE_CONFIG_PROPERTY_PROJECT_VERSION}={version}'
            is_project_version_defined = True
            break

    if not is_project_version_defined:
        raise ValueError(f"The Unreal Engine project has no version defined in the configuration file {config_file_path}")

    with open(config_file_path, 'wt') as fd:
        fd.writelines(lines)
