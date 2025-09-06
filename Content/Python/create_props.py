import unreal
import os

# Get the list of props from ADACA_extract

props_dir = "C:/Users/Spencer/Desktop/ADACA_extract/ADACA/Content/StaticMeshes/Props"
props = [p.replace(".uasset", "") for p in os.listdir(props_dir) if p.startswith("Prop_") and p.endswith(".uasset")]

print(f"Weapons found: {props}")

package_path = "/Game/StaticMeshes/Props"

factory = unreal.BlueprintFactory()
factory.set_editor_property("ParentClass", unreal.Actor)

asset_tools = unreal.AssetToolsHelpers.get_asset_tools()

for prop in props:
    print(f"Creating blueprint Actor class for {prop}...")
    new_asset = (asset_tools.create_asset(prop, package_path, None, factory))
    # unreal.EditorAssetLibrary.save_loaded_asset(new_asset)


