#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2024 https://github.com/Oops19
#


import ast
import os
from typing import Set, Tuple

from block_generate_outfits.enums.bgoc import BlockGenerateOutfitCategory
from sims4communitylib.services.commands.common_console_command import CommonConsoleCommand, CommonConsoleCommandArgument
from sims4communitylib.services.commands.common_console_command_output import CommonConsoleCommandOutput
from singletons import DEFAULT

from ts4lib.libraries.ts4folders import TS4Folders

from block_generate_outfits.modinfo import ModInfo
from sims.outfits.outfit_enums import OutfitCategory
from sims.sim_info_base_wrapper import SimInfoBaseWrapper

from sims4communitylib.utils.common_injection_utils import CommonInjectionUtils
from sims4communitylib.utils.common_log_registry import CommonLogRegistry, CommonLog

log: CommonLog = CommonLogRegistry.get().register_log(ModInfo.get_identity().name, 'bgo_main')
log.enable()
log.debug(f"Thank you for using Block Generate Outfits")


class BlockGenerateOutfitsMain:

    # Default values
    is_enabled = True
    keep_outfits_category_and_index: Set[Tuple[OutfitCategory, int]] = {(OutfitCategory.BATHING, 0), (OutfitCategory.SPECIAL, 1), }

    def __init__(self):
        self.ts4f = TS4Folders(ModInfo.get_identity().base_namespace)
        self.load('block_generate_outfits.txt')
        log.debug(f"Affected outfits: {BlockGenerateOutfitsMain.keep_outfits_category_and_index}")

    def load(self, filename):
        file_name = os.path.join(self.ts4f.data_folder, filename)
        try:
            with open(file_name, 'rt', encoding='UTF-8') as fp:
                data = fp.read()
                data = ast.literal_eval(data)
                rv: Set[Tuple[OutfitCategory, int]] = set()
                for outfit_str, outfit_idx in data:
                    outfit_cat = OutfitCategory(BlockGenerateOutfitCategory[outfit_str].value)
                    rv.add((outfit_cat, outfit_idx))
                BlockGenerateOutfitsMain.keep_outfits_category_and_index = rv
        except Exception as e:
            log.error(f"Couldn't import {file_name} ({e})")

    @staticmethod
    @CommonConsoleCommand(ModInfo.get_identity(), 'o19.bgo.toggle', 'Toggle block')
    def cheat_o19_bgo_toggle(output: CommonConsoleCommandOutput):
        BlockGenerateOutfitsMain.is_enabled = not BlockGenerateOutfitsMain.is_enabled
        if BlockGenerateOutfitsMain.is_enabled:
            output(f"Sims can't replace existing outfits.")
        else:
            output(f"Sims can re-generate their outfits.")

    @staticmethod
    @CommonConsoleCommand(ModInfo.get_identity(), 'o19.bgo.help', 'Show help')
    def cheat_o19_bgo_toggle(output: CommonConsoleCommandOutput):
        BlockGenerateOutfitsMain.is_enabled = not BlockGenerateOutfitsMain.is_enabled
        output(f"Outfit Categories which support 5 outfits [0-4]: EVERYDAY FORMAL ATHLETIC SLEEP PARTY SWIMWEAR HOTWEATHER COLDWEATHER BATUU")
        output(f"Outfit Categories which support 3 outfits [0-2]: SPECIAL (0=Default, 1=Towel, 2=Fashion)")
        output(f"Outfit Categories which support 1 outfit [0]: BATHING CAREER SITUATION")

    @staticmethod
    @CommonConsoleCommand(ModInfo.get_identity(), 'o19.bgo.edit', 'Add or remove one outfit temporarily.',
                          command_arguments=(
                                  CommonConsoleCommandArgument('action', 'string', "'+' or '-' to add or remove an outfit", is_optional=False, default_value='+'),
                                  CommonConsoleCommandArgument('category', 'string', "'EVERYDAY', ..., 'BATUU'", is_optional=False, default_value='EVERYDAY'),
                                  CommonConsoleCommandArgument('index', 'integer', "0; 0-2 or 0-5 ...  Depending on catgory", is_optional=False, default_value=0),
                          )
                          )
    def cheat_o19_bgo_edit(output: CommonConsoleCommandOutput, action: str = '+', category: str = 'EVERYDAY', index: int = 0):
        try:
            outfit_str = category.upper()
            output(f"{action} {outfit_str} {index}")
            outfit_cat = OutfitCategory(BlockGenerateOutfitCategory[outfit_str].value)
            outfit_idx = index
            outfit_category_and_index = (outfit_cat, outfit_idx)
            if action == '+':
                BlockGenerateOutfitsMain.keep_outfits_category_and_index.add(outfit_category_and_index)
            elif action == '-':
                BlockGenerateOutfitsMain.keep_outfits_category_and_index.remove(outfit_category_and_index)
            output(f"Affected outfits: {BlockGenerateOutfitsMain.keep_outfits_category_and_index}")
            output(f"Edit the configuration file to persist these changes.")
        except Exception as e:
            output(f"Error {e}")

    @staticmethod
    @CommonInjectionUtils.inject_safely_into(ModInfo.get_identity(), SimInfoBaseWrapper, SimInfoBaseWrapper.generate_outfit.__name__, handle_exceptions=False)
    def o19_si_bw_generate_outfit(original, self, outfit_category, outfit_index=0, tag_list=(), filter_flag=DEFAULT, body_type_flags=DEFAULT, *args, **kwargs):
        # sim_info_base_wrapper.py
        # class SimInfoBaseWrapper
        # def generate_outfit(self, outfit_category, outfit_index=0, tag_list=(), filter_flag=DEFAULT, body_type_flags=DEFAULT, **kwargs):
        # noinspection PyBroadException
        try:
            if BlockGenerateOutfitsMain.is_enabled:
                if self.has_outfit((outfit_category, outfit_index)):
                    outfit_category_and_index = (outfit_category, outfit_index)

                    if not BlockGenerateOutfitsMain.keep_outfits_category_and_index or \
                            outfit_category_and_index in BlockGenerateOutfitsMain.keep_outfits_category_and_index:
                        log.debug(f"Skipping outfit '{outfit_category_and_index}' generation for '{self}'")
                        return True

            return original(self, outfit_category, outfit_index, tag_list, filter_flag, body_type_flags, *args, **kwargs)
        except Exception as e:
            log.error(f"Error '{e}' in Keep-Outfits", throw=False)


BlockGenerateOutfitsMain()
