#28-12-2021 : W's filemanagement class. Based on save_my_yamls.py
import pathlib, collections, os, shutil

class w_c_files(): 
    def __init__(self, from_pattern, to_pattern, from_path, to_path) -> None:
        self.c_from_pattern = from_pattern
        self.c_to_pattern = to_pattern
        self.c_from_path = from_path
        self.c_to_path = to_path
    
    def __repr__(self) -> str:
        return(f"From pattern: {self.c_from_pattern}, to pattern: {self.c_to_pattern}.\nFrom path: {self.c_from_path}, to path: {self.c_to_path}.")

    def w_count_file(self, dir1, pattern) -> str:
        return ("\n"+ str(collections.Counter(p.suffix for p in dir1.rglob(pattern))))

    def w_copy_file(self, dir1, dir2, pattern):
        print(f"\nCurrent dir: {dir2}")
        for f in dir1.rglob(pattern):
            dir3 = pathlib.Path(f.parts[-2])
            dir3.mkdir(parents=True, exist_ok=True)
            new_file_path = dir2 / f.parts[-2] / (f.stem + '.w-yaml')
            print (f"Copy {f} to {new_file_path}")
            shutil.copy(f, new_file_path)
     
    def w_delete_file(self, dir1, pattern):
        for file_name in os.listdir(dir1):
            if os.path.isdir(file_name) :
                if file_name.startswith('.') or file_name.startswith('test'):
                    print(f"System Dir: {file_name}")    
                else :
                    print(f"Deleting dir: {file_name}")
                    shutil.rmtree(file_name)
            else:
                print(f"File: {file_name}")
                file_path = os.path.join(dir1, file_name)
                if file_name.endswith(pattern):
                    print(f"Deleting: file name: {file_name} from path: {file_path}")
                    os.remove(file_path)

    def w_list_file(self, dir1, pattern):
        for f in dir1.rglob(pattern):
            print (f)
    
    def w_list_tree(self, directory: pathlib.Path):
        print(f'+ {directory}')
        for path in sorted(directory.rglob('*')):
            depth = len(path.relative_to(directory).parts)
            spacer = '    ' * depth
            print(f'{spacer}+ {path.name}')