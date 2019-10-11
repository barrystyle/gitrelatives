import os, sys, time, json

# git-relatives (barrystyle 11102019)
# find closest related version of a file between two git repositories
# 
# set source to the file whose relatives you are searching
# set target to the repository you want to search for a relative

source = '/data/vvvvv/xxxxx.cpp'
target = '/data/yyyyy/zzzzz.cpp'

# convenience functions
def compare_command(source, target):
    return('git diff '+source+' '+target)

def reset_diff_history(target):
    return('git reset --hard && git pull')

def load_diff_history(target):
    return('git reset --hard && git pull && git log --follow --oneline -- '+get_target_name(target))

def get_working_dir(target):
    fullpath = ''
    for section in target.split('/'):
        fullpath = section
    return target.replace(fullpath,'')

def get_target_name(target):
    fullpath = ''
    for section in target.split('/'):
        fullpath = section
    return fullpath

def run_command(cmdstring):
    funcreturn = os.popen(cmdstring).read()
    return funcreturn

# main
reset_diff_history(target)
workingdir = 'cd ' + get_working_dir(target) + ' && ' + load_diff_history(target)
diffhistory = run_command(workingdir)
smallest = 104857600
smallesthash = ''
try: 
  for line in diffhistory.split('\n'):
    time.sleep(0.1)
    diffhash = line.split(' ')[0]
    if len(diffhash) != 9:
       continue
    run_command('cd ' + get_working_dir(target) + ' && git reset ' + diffhash + ' --hard')
    testcompare = 'cd ' + get_working_dir(target) + ' && git diff ' + source + ' ' + target
    diffout = run_command(testcompare)
    print diffhash + ' is ' + str(len(diffout))
    if len(diffout) < smallest and len(diffout) != 0:
       smallest = len(diffout)
       smallesthash = diffhash
except:
  pass

print smallesthash + ' is closest'
 


