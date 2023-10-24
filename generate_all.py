#!/usr/bin/python3

import glob
import os
import subprocess

ghidra_project_basename = "rizzo-"
rizzo_out_child_base_dirname = "esp-idf-"

# Get current dir
base_dir = os.getcwd()

# Paths
esp_idf_elfs_path = os.path.join(base_dir, "esp-idf_elfs")
ghidra_install_path = os.path.join(base_dir, "ghidra")
ghidra_rizzo_path = os.path.join(base_dir, "ghidra-rizzo")
ghidra_projects_path = os.path.join(base_dir, "ghidra_projects")
ghidra_headless_path = os.path.join(ghidra_install_path, "support", "analyzeHeadless")

ghidra_project_basename = "rizzo-"
if not os.path.exists(ghidra_projects_path):
    os.mkdir(ghidra_projects_path)

release_list = ['release_v2.0',
                'release_v2.1',
                'release_v3.0',
                'release_v3.1',
                'release_v3.2',
                'release_v3.3',
                'release_v4.0',
                'release_v4.1',
                'release_v4.3',
                'release_v4.4',
                'release_v5.0',
                'release_v5.1']

os.chdir(esp_idf_elfs_path)

for release_dir in release_list:
    out_dir = os.path.join(base_dir, release_dir)
    if not os.path.exists(out_dir):
        os.mkdir(os.path.join(base_dir, release_dir))

    os.chdir(os.path.join(esp_idf_elfs_path, release_dir))
    elf_glob = glob.glob('*.elf')
    for elf in elf_glob:
        elf_path = os.path.normpath(os.path.join(esp_idf_elfs_path, release_dir, elf))
        out_file = os.path.join(out_dir, elf.replace('.elf', '.riz'))
        ghidra_project_name = ghidra_project_basename + release_dir + "-" + elf
        subprocess.run(['touch', out_file])
        command = [ghidra_headless_path,
                   ghidra_projects_path,
                   ghidra_project_name,
                   "-import", elf_path,
                   "-scriptPath", ghidra_rizzo_path,
                   "-postScript", "RizzoSave.py", out_file] 

        subprocess.run(command)
