import unreal
import os

# Get the list of weapons from ADACA_extract

weapons_dir = "C:/Users/Spencer/Desktop/ADACA_extract/ADACA/Content/Classes/Weapons/"
weapons = [w.replace(".uasset", "") for w in os.listdir(weapons_dir) if w.startswith("Wep_") and w.endswith(".uasset")]

print(f"Weapons found: {weapons}")

package_path = "/Game/Classes/Weapons"

factory = unreal.BlueprintFactory()
factory.set_editor_property("ParentClass", unreal.Actor)

asset_tools = unreal.AssetToolsHelpers.get_asset_tools()

for weapon in weapons:
    print(f"Creating blueprint Actor class for {weapon}...")
    new_asset = (asset_tools.create_asset(weapon, package_path, None, factory))
    # unreal.EditorAssetLibrary.save_loaded_asset(new_asset)


