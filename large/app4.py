import os

파일들 = os.listdir('test')

for i in 파일들:
    os.rename(f'test/{i}', f'test/a{i}')

import shutil
for i in os.listdir('test'):
    shutil.copy(f'test/{i}',f'test2/{i}')