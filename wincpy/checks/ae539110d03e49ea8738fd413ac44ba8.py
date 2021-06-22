import tempfile
import shutil
import os

from wincpy.helpers import compare_states, exec_assignment_code, get_main_abspath

__winc_id__ = 'ae539110d03e49ea8738fd413ac44ba8'


def run(student_module):
    result = []

    main_abspath = get_main_abspath(student_module)
    # output, state = exec_assignment_code(main_abspath)

    module_folder = main_abspath.replace('main.py', '')

    cache_path = os.path.join(os.getcwd(), 'cache')
    zip_path = os.path.join(module_folder, 'data.zip')

    # Start fresh
    try:
        shutil.rmtree(cache_path)
    except:
        pass

    requirement = 'clean_cache() creates a new directory'
    student_module.clean_cache()
    result.append((requirement, os.path.isdir(cache_path)))

    requirement = 'clean_cache() ensures a clean cache'
    # Put some bogus file in it, should be gone after calling clean_cache()
    with open(os.path.join(cache_path, 'throwaway'), 'w') as fp:
        fp.write('You can remove this file.')
    student_module.clean_cache()
    result.append((requirement, not os.path.exists(os.path.join(cache_path, 'throwaway'))))

    requirement = 'cache_zip() unpacks the zip file into a clean cache folder'
    student_module.cache_zip(zip_path, cache_path)
    result.append((requirement, len(os.listdir(cache_path)) == 1000))

    requirement = 'cached_files() returns a list of absolute paths to all the files in the cache'
    cached_stuff = [os.path.join(cache_path, f) for f in os.listdir(cache_path)]
    cached_files = [f for f in cached_stuff if os.path.isfile(f)]
    cached_files_student = student_module.cached_files()
    result.append((requirement, cached_files == cached_files_student))

    requirement = 'find_password() returns the right password'
    pw = student_module.find_password(student_module.cached_files())
    result.append((requirement, pw == 'correct_horse_battery_staple'))

    # Clean up
    shutil.rmtree(cache_path)

    return result
