import os
import subprocess
import datetime

global_root = os.getcwd()

the_result = ''

def scanFolder(rootdir=global_root):
  files = []
  directories = []
  # print('root', rootdir)
  results = os.listdir(rootdir)

  for result in results: 
    result_path = os.path.join(rootdir,result)
    if os.path.isdir(result_path): 
      directories.append(result_path)
    else:
      if result_path.endswith('.mp4'):
        files.append(result_path)

  total_duration = 0

  if not directories and files: 
    name_of_root_folder = global_root.split('\\')[-1] + '.txt'
    with open(name_of_root_folder, 'a') as f:
      result = get_length_multiple(files)
      total_duration += result
      the_result = "" + rootdir.split('\\')[-1] + " " + str(datetime.timedelta(seconds=result)).split('.')[0]
      print(the_result)
      f.write(the_result + '\n')




  if directories:
    for directory in directories:
      dir_path = os.path.join(rootdir, directory)
      # print('')
      # print('============================================')
      # print('')
      scanFolder(dir_path)


def get_length_multiple(files):
  total_result = 0
  for filename in files: 
    result = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                             "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", filename], 
                             stdout=subprocess.PIPE, 
                             stderr=subprocess.STDOUT)
    total_result += float(result.stdout)
  return total_result

scanFolder()