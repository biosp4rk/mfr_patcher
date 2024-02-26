import json
import typing

from jsonschema import validate

from mfr_patcher.data import get_data_path
from mfr_patcher.hints import Hints
from mfr_patcher.item_patcher import ItemPatcher, set_starting_items, set_tank_increments
from mfr_patcher.locations import LocationSettings
from mfr_patcher.random_palettes import PaletteRandomizer, PaletteSettings
from mfr_patcher.rom import Rom
from mfr_patcher.text import write_seed_hash


def patch(input_path: str,
          output_path: str,
          patch_data_path: str,
          status_update: typing.Callable[[float, str], None]
          ):
    # load input rom
    rom = Rom(input_path)

    # load patch data file and validate
    with open(patch_data_path) as f:
        patch_data = json.load(f)

    with open(get_data_path("schema.json")) as f:
        schema = json.load(f)
    validate(patch_data, schema)

    # load locations and set assignments
    loc_settings = LocationSettings.load()
    loc_settings.set_assignments(patch_data["Locations"])

    # get random palette settings
    pal_settings = None
    if "Palettes" in patch_data:
        pal_settings = PaletteSettings.from_json(patch_data["Palettes"])

    # randomize palettes - palettes are randomized first in case the item
    # patcher needs to copy tilesets
    if pal_settings is not None:
        status_update(-1, "Randomizing palettes...")
        pal_randomizer = PaletteRandomizer(rom, pal_settings)
        pal_randomizer.randomize()

    # write item assignments
    status_update(-1, "Writing item assignments...")
    item_patcher = ItemPatcher(rom, loc_settings)
    item_patcher.write_items()

    # get hints
    hints = None
    if "Hints" in patch_data:
        hints = Hints.from_json(patch_data["Hints"])

    # write hints
    if hints is not None:
        status_update(-1, "Writing hints...")
        hints.write(rom)

    # starting items
    if "StartingItems" in patch_data:
        status_update(-1, "Writing starting items...")
        set_starting_items(rom, patch_data["StartingItems"])

    # tank increments
    if "TankIncrements" in patch_data:
        status_update(-1, "Writing tank increments...")
        set_tank_increments(rom, patch_data["TankIncrements"])

    if patch_data.get("SkipDoorTransitions"):
        # TODO: move to separate patch
        rom.write_32(0x69500, 0x3000BDE)
        rom.write_8(0x694E2, 0xC)

    write_seed_hash(rom, patch_data["SeedHash"])

    rom.save(output_path)
    status_update(-1, f"Output written to {output_path}")