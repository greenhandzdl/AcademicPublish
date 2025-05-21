# 删除所有匹配后缀名的文件
import os

# 定义要删除的文件后缀
IGNORED_SUFFIXES = {
    ".aux",
    ".log",
    ".out",
    ".toc",
    ".pdf",
    ".synctex.gz"
}

def delete_files_by_suffix(root_dir):
    deleted_files = []
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if any(filename.endswith(suffix) for suffix in IGNORED_SUFFIXES):
                file_path = os.path.join(dirpath, filename)
                print(f"Deleting: {file_path}")
                os.remove(file_path)
                deleted_files.append(file_path)
    return deleted_files

if __name__ == "__main__":
    deleted = delete_files_by_suffix('.')
    if deleted:
        print(f"\n共删除了 {len(deleted)} 个文件。")
    else:
        print("\n没有找到匹配的文件。")