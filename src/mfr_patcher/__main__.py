import argparse
import json

from jsonschema import validate

from mfr_patcher.item_patcher import ItemPatcher
from mfr_patcher.locations import LocationSettings
from mfr_patcher.random_palettes import PaletteSettings, PaletteRandomizer
from mfr_patcher.rom import Rom
from mfr_patcher.data import get_data_path


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # GBA ROM input/output paths
    parser.add_argument("rom_path", type=str,
        help="Path to a GBA ROM file")
    parser.add_argument("out_path", type=str,
        help="Path to output ROM file")
    # patch data
    parser.add_argument("patch_data_path", type=str,
        help="Path to patch data json file")
    # other settings
    parser.add_argument("-sdt", "--skip_door_transitions", action="store_true",
        help="Makes all door transitions instant")

    args = parser.parse_args()

    # load input rom
    rom = Rom(args.rom_path)

    # load patch data file and validate
    with open(args.patch_data_path) as f:
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
        print("Randomizing palettes...")
        pal_randomizer = PaletteRandomizer(rom, pal_settings)
        pal_randomizer.randomize()

    # patch items
    print("Writing items...")    
    item_patcher = ItemPatcher(rom, loc_settings)
    item_patcher.write_items()

    if args.skip_door_transitions:
        # TODO: move to separate patch
        rom.write_32(0x69500, 0x300001F)
        rom.write_16(0x694E4, 0xD000)

    rom.save(args.out_path)
    print(f"Output written to {args.out_path}")
