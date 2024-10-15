import os
import subprocess

# Путь к папке с файлами FBX
fbx_folder = "/Users/motya/work/pythTool/models"

# Путь к папке, куда будут сохраняться файлы GLB
glb_folder = "./glb"

# Проверяем, существует ли папка для файлов GLB, и создаем ее при необходимости
if not os.path.exists(glb_folder):
    os.makedirs(glb_folder)

# Проходимся циклом по всем файлам в папке с FBX
for fbx_file in os.listdir(fbx_folder):
    if fbx_file.endswith(".fbx"):
        # Создаем полный путь к файлу FBX
        fbx_file_path = os.path.join(fbx_folder, fbx_file)

        # Создаем имя файла для экспорта в GLB
        glb_file = os.path.splitext(fbx_file)[0] + ".glb"
        glb_file_path = os.path.join(glb_folder, glb_file)

        # Формируем команду для Blender
        blender_command = [
            "/Applications/Blender.app/Contents/MacOS/Blender",
            "--background",
            "--python-expr",
            "import bpy; bpy.ops.wm.read_factory_settings(use_empty=True); bpy.ops.import_scene.fbx(filepath='{}'); bpy.ops.export_scene.gltf(filepath='{}', export_format='GLB');".format(fbx_file_path, glb_file_path)
            #"import bpy; bpy.ops.import_scene.fbx(filepath='{}'); bpy.ops.export_scene.gltf(filepath='{}', export_format='GLB');".format(fbx_file_path, glb_file_path)
        ]

        # Запускаем Blender с командой
        subprocess.run(blender_command)

print("Реэкспорт завершен.")



#blender_command = [
#    "/Applications/Blender.app/Contents/MacOS/Blender",
#    "--background",
#    "--python-expr",
#    "import bpy; bpy.ops.wm.read_factory_settings(use_empty=True); bpy.ops.import_scene.fbx(filepath='{}'); bpy.ops.export_scene.gltf(filepath='{}', export_format='GLB');".format(fbx_file_path, glb_file_path)
#    #"import bpy; bpy.ops.import_scene.fbx(filepath='{}'); bpy.ops.export_scene.gltf(filepath='{}', export_format='GLB');".format(fbx_file_path, glb_file_path)
#]