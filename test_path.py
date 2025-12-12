"""测试库demo路径生成逻辑"""

from opendemo.services.storage_service import StorageService
from opendemo.services.config_service import ConfigService
from opendemo.core.demo_manager import DemoManager

config = ConfigService()
storage = StorageService(config)
dm = DemoManager(storage)

print('输出目录:', storage.get_output_directory())
print()

output_dir = storage.get_output_directory()
language = 'python'
demo_name = 'python-http-request'

print('模拟路径计算:')

# 有库名的情况
library_name = 'requests'
base_path = output_dir / language.lower()
if library_name:
    base_path = base_path / 'libraries' / library_name
demo_path = base_path / demo_name
print(f'  library_name={library_name} 时:')
print(f'    base_path: {base_path}')
print(f'    demo_path: {demo_path}')
print()

# 无库名的情况
library_name = None
base_path = output_dir / language.lower()
if library_name:
    base_path = base_path / 'libraries' / library_name
demo_path = base_path / demo_name
print(f'  library_name={library_name} 时:')
print(f'    base_path: {base_path}')
print(f'    demo_path: {demo_path}')
