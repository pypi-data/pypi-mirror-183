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
import re

from majormode.perseus.model.version import Version

from bootloader.unreal_engine.model.apple_version import AppleAppVersion


DEFAULT_VERSION = Version(0, 0, 1)

UNREAL_ENGINE_CONFIG_PROPERTY_PROJECT_VERSION = 'ProjectVersion'
UNREAL_ENGINE_CONFIG_PROPERTY_ADDITIONAL_PLIST_DATA = 'AdditionalPlistData'

REGEX_PATTERN_PROPERTY_PROJECT_VERSION = rf'^{UNREAL_ENGINE_CONFIG_PROPERTY_PROJECT_VERSION}\s*=\s*([a-zA-Z0-9\.\-]+)\s*$'
REGEX_PATTERN_PROPERTY_ADDITIONAL_PLIST_DATA = rf'^{UNREAL_ENGINE_CONFIG_PROPERTY_ADDITIONAL_PLIST_DATA}\s*=.*$'

REGEX_PROPERTY_PROJECT_VERSION = re.compile(REGEX_PATTERN_PROPERTY_PROJECT_VERSION)
REGEX_PROPERTY_ADDITIONAL_PLIST_DATA =re.compile(REGEX_PATTERN_PROPERTY_ADDITIONAL_PLIST_DATA)


def read_project_version(
        path: Path,
        build_number: int = None,
        replace_patch_version: bool = False,
        require_semantic_versioning: bool = False) -> str or Version:
    """
    Return the project version of an Unreal Engine project.

    The version of an Unreal Engine project is identified in the attribute
    `ProjectVersion` of the section
    `[/Script/EngineSettings.GeneralProjectSettings]` of the configuration
    file `DefaultGame.ini` located in the folder `$ROOT_PATH/Config` of
    the Unreal Engine project.


    @param path: The absolute path to the root folder of an Unreal Engine
        project.

    @param build_number: The build number of the Unreal Engine project.

    @param replace_patch_version: Indicate whether to replace the patch
        version of the Unreal Engine project with the specified build
        number.  The argument `build_number` MUST be passed  to the
        function.

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
    if replace_patch_version and build_number is None:
        raise ValueError("A build number MUST be passed to replace the patch version")

    if not path.exists():
        raise ValueError(f"The path {path} doesn't exist")

    config_file_path = Path().joinpath(path.expanduser(), 'Config', 'DefaultGame.ini')

    # Unreal Engine project configuration files have a custom syntax for
    # supporting arrays:
    #
    # ```ini
    # [Section]
    # !ArrayVar = anything_since_this_just_clears_it
    # +ArrayVar = first_value
    # +ArrayVar = second_value
    # +ArrayVar = third_value
    # ```
    #
    # https://docs.unrealengine.com/5.0/en-US/configuration-files-in-unreal-engine/
    #
    # This syntax is not supported by the Python standard module
    # `configparser`. The following code would raise the exception
    # `configparser.DuplicateOptionError` when reading the configuration
    # file of a Unreal Engine project file:
    #
    # ```python
    # config_parser = configparser.ConfigParser()
    # config_parser.read(config_file_path)
    # ```
    #
    # Instead, we need to parse the Unreal Engine project file with a
    # regular expression.  It's a bit patchy.
    with open(config_file_path, 'rt') as fd:
        lines = fd.readlines()

    for line in lines:
        regex_match = REGEX_PROPERTY_PROJECT_VERSION.match(line.strip())
        if regex_match:
            project_version = regex_match.group(1)

            if require_semantic_versioning:
                project_version = Version(project_version)

            if replace_patch_version:
                if not require_semantic_versioning:
                    raise ValueError("The Unreal Engine project version MUST be required to comply with Semantic Versioning to get its patch version updated")

                project_version = Version(project_version.major, project_version.minor, build_number)
            else:
                project_version = f'{project_version}+{build_number}'

            return project_version

    raise ValueError(f"The Unreal Engine project has no version defined in the configuration file {config_file_path}")


def update_ios_version(
        path: Path,
        version: AppleAppVersion) -> None:
    """
    Update the iOS version of an Unreal Engine project define in the
    additional property list data.


    The iOS version of an Unreal Engine project is identified in the attribute
    `AdditionalPlistData` of the section
    `[/Script/IOSRuntimeSettings.IOSRuntimeSettings]` of the configuration
    file `DefaultEngine.ini` located in the folder `$ROOT_PATH/Config` of
    the Unreal Engine project.


    @param path: The absolute path to the root folder of an Unreal Engine
        project.

    @param version: The iOS version to write in the Unreal Engine project
        configuration file.
    """
    if not path.exists():
        raise ValueError(f"The path {path} doesn't exist")

    config_file_path = Path().joinpath(path.expanduser(), 'Config', 'DefaultEngine.ini')
    with open(config_file_path, 'rt') as fd:
        lines = fd.readlines()

    is_additional_plist_data_property_defined = False

    for i in range(len(lines)):
        regex_match = REGEX_PROPERTY_ADDITIONAL_PLIST_DATA.match(lines[i].strip())
        if regex_match:
            lines[i] = f'{UNREAL_ENGINE_CONFIG_PROPERTY_ADDITIONAL_PLIST_DATA}={version.plist_data}'
            is_additional_plist_data_property_defined = True
            break

    if not is_additional_plist_data_property_defined:
        raise ValueError(f"The Unreal Engine project has no additional plist data property defined in the configuration file {config_file_path}")

    with open(config_file_path, 'wt') as fd:
        fd.writelines(lines)


def update_project_version(
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

    @param version: The version to write in the Unreal Engine project
        configuration file.
    """
    if not path.exists():
        raise ValueError(f"The path {path} doesn't exist")

    config_file_path = Path().joinpath(path.expanduser(), 'Config', 'DefaultGame.ini')
    with open(config_file_path, 'rt') as fd:
        lines = fd.readlines()

    is_project_version_property_defined = False

    for i in range(len(lines)):
        regex_match = REGEX_PROPERTY_PROJECT_VERSION.match(lines[i].strip())
        if regex_match:
            lines[i] = f'{UNREAL_ENGINE_CONFIG_PROPERTY_PROJECT_VERSION}={version}'
            is_project_version_property_defined = True
            break

    if not is_project_version_property_defined:
        raise ValueError(f"The Unreal Engine project has no version defined in the configuration file {config_file_path}")

    with open(config_file_path, 'wt') as fd:
        fd.writelines(lines)
