import tempfile
import shutil
import os

from wincpy.checks import utils

__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"


def check_clean_cache(student_module):
    cache_path, _ = __get_paths(student_module)
    student_module.clean_cache()
    assert os.path.isdir(cache_path), f"`cache_path` did not create {cache_path}"

    # Put some bogus file in it that should be gone after calling clean_cache()
    with open(os.path.join(cache_path, "throwaway"), "w") as fp:
        fp.write("You can remove this file.")
    student_module.clean_cache()
    assert not os.listdir(
        cache_path
    ), f"`clean_cache` does not ensure the cache is empty"

    __clean(student_module)


def check_cache_zip(student_module):
    __clean(student_module)
    cache_path, zip_path = __get_paths(student_module)
    student_module.cache_zip(zip_path, cache_path)
    n_cached_files = len(os.listdir(cache_path))
    assert (
        n_cached_files == 1000
    ), f"Expected to find 1000 files in the cache folder after running `cache_zip` but found {n_cached_files}"

    __clean(student_module)


def check_cached_files(student_module):
    try:
        check_cache_zip(student_module)
    except:
        raise AssertionError(
            "You need to implement `cache_zip` before we can check `cached_files`"
        )

    cache_path, zip_path = __get_paths(student_module)
    student_module.cache_zip(zip_path, cache_path)

    cached_stuff = [os.path.join(cache_path, f) for f in os.listdir(cache_path)]
    cached_files = [f for f in cached_stuff if os.path.isfile(f)]
    cached_files_student = student_module.cached_files()
    assert (
        cached_files == cached_files_student
    ), f"We got a different list of files than you returned. Here's our first one:\n\n{cached_files[0]}\n\nRemember to use *absolute* paths!"

    __clean(student_module)


def check_find_password(student_module):
    try:
        check_cached_files(student_module)
    except:
        raise AssertionError(
            "You need to implement `cached_files` before we can check `find_password`"
        )
    cache_path, zip_path = __get_paths(student_module)
    student_module.cache_zip(zip_path, cache_path)
    student_module.find_password(
        student_module.cached_files()
    ) == "correct_horse_battery_staple", "The returned password is not correct."


def __get_paths(student_module):
    module_base_dir = os.path.split(utils.get_main_abspath(student_module))[0]
    return os.path.join(module_base_dir, "cache"), os.path.join(
        module_base_dir, "data.zip"
    )


def __clean(student_module):
    cache_path, zip_path = __get_paths(student_module)
    try:
        shutil.rmtree(cache_path)
    except FileNotFoundError:
        pass
