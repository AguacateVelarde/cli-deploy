import os
from subprocess import call, check_output, Popen, PIPE
from shutil import copy2
from variables import default_files_copy, default_files_target

def core_deploy(path, command_build): 
    print( 'Running deploy ... ')
    call(command_build.split(), cwd=path)    

def core_copy( path, destiny_path ):
    print( 'COPIE COMMAND : from {} to {}'.format( path, destiny_path ))
    dist_path = ''.join([ path, '/dist', '/login' ])
    for _file in os.listdir(dist_path) :
        if _file in default_files_copy :
            if not os.path.exists( destiny_path ):
                os.mkdir( destiny_path ) 
                print( 'CREATE FOLDER : {}'.format( destiny_path ) )  
            file_dist = ''.join([ dist_path, '/', _file ])
            file_destiny = ''.join( [ destiny_path, '/', default_files_target[_file] ] ) 
            print( '\t copy {}'.format( file_dist ) )
            print( ' \t \t -> to destiny {}'.format( file_destiny ) )       
            copy2(file_dist, file_destiny)

            
            