#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2023 https://github.com/Oops19
#


from sims4communitylib.mod_support.common_mod_info import CommonModInfo


class ModInfo(CommonModInfo):
    _FILE_PATH: str = str(__file__)

    @property
    def _name(self) -> str:
        return 'Block-Generate-Outfits'

    @property
    def _author(self) -> str:
        return 'o19'

    @property
    def _base_namespace(self) -> str:
        return 'block_generate_outfits'

    @property
    def _file_path(self) -> str:
        return ModInfo._FILE_PATH

    @property
    def _version(self) -> str:
        return '1.0.0'


'''
v1.0.0
    Stable version
v0.0.1
    Initial version
'''
