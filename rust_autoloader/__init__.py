import os
import hashlib
import time
import subprocess
from threading import Thread

def get_rust_files(dir_path):
    """get all the rust files in current directory"""

    rust_files = []
    if dir_path[len(dir_path)-1] == '/':
        dir_path = dir_path[:len(dir_path)-1]

    # check for .rs files and store the absolute path.
    for path in os.listdir(dir_path):
        if path.endswith('.rs'):
            rust_files.append(dir_path + '/' + path)
    return rust_files

rust_files_hash = {}
def hashfile(afile, hasher, blocksize=65536):
    """store the hashes of each file in a dict"""
    buf = afile.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    return hasher.digest()

def run_hash_check(dir_path):
    """ check hash changes for rust files and call compilation if change detected """

    for fname in get_rust_files(dir_path):
        if fname not in rust_files_hash:
            rust_files_hash[fname] = hashfile((open(fname, 'rb')), hashlib.md5())
        else:
            if rust_files_hash[fname] != hashfile((open(fname, 'rb')), hashlib.md5()):
                rust_files_hash[fname] = hashfile((open(fname, 'rb')), hashlib.md5())
                compile_file(fname)

def compile_file(fname):
    """ compiles the file and prints errors (if any) """
    p = subprocess.Popen(["rustc", fname], stderr=subprocess.PIPE)
    output, err = p.communicate()
    if err != "":
        print err,
        print
        print
    else:
        print "compilation success... running the program..."
        run_file(fname)

def run_file(fname):
    """ runs the file and prints the output """

    # TODO: taking input from autoloader.

    p = subprocess.Popen([fname.rstrip('.rs')], stdout=subprocess.PIPE)

    # a simple thread that polls the process and kills if execution time exceeds 10 seconds.
    thread = Thread(target=kill_process, args=(p, 10,))
    thread.start()
    thread.join()

    output, err = p.communicate()
    if output != "":
        print "output is: "
        print output,
        print
        print
    else:
        if p.poll() < 0:
            print "continuing autoloader..."
            print
            print
        else:
            print "no output generated..."

def kill_process(popen_obj, max_exec_time):
    """ returns -1 if the process is killed, 0 if execution succeeded"""
    for i in xrange(max_exec_time):
        if popen_obj.poll() == 0:
            print "execution successful..."
            return 0
        time.sleep(1)
    print "10 seconds crossed, killing the process...."
    popen_obj.kill()
    print "process killed..."
    return -1

def run(dir_path):
    # polls the current directory rust files every 2 seconds.
    print "autoloader up and running... go and edit your rust files now!"
    while True:
        time.sleep(2)
        run_hash_check(dir_path)

if __name__ == "__main__":
    run(os.path.dirname(os.path.abspath(__file__)))
