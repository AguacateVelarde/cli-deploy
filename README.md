# Deploy Login Online 

## For install all dependencies run before :
```
pip install -r requirement.txt
```
## Export your locale as : 
```
export LC_ALL=es_ES.UTF-8
```

## To change default values config variables.py 

 ####  default_path 
    * Project folder default
 #### default_build_command
    * build command for create a project 
        default : "ng build --prod --output-hashing none --single-bundle true --bundle-styles false  --project login"
 #### default_destiny_folder_copy
    * Project folder target copy files
 #### default_files_copy
    * Array contain all files in folder dist/login to copy to target path 
 #### default_files_target
    * Hash dictionary contain "filename" : "filename-copy"

