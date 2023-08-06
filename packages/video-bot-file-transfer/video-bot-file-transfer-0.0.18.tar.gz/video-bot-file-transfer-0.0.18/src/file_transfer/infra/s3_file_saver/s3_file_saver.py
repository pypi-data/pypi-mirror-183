#native
from typing import List, AnyStr
from os import path
import ntpath


#externals
import boto3

#project
from file_transfer.utils.helpers import get_attr, remove_last_slash


class S3FileSaver:

   
    def __init__(self, config):

        self.config = config
        
        self.target_bucket = self.config['target_bucket']
        self.target_directory = remove_last_slash(self.config['target_directory'])
        self.aws_credentials = self.config['aws_credentials'] 
      

        self.session = boto3.Session(
            aws_access_key_id=self.aws_credentials['client_id'],
            aws_secret_access_key=self.aws_credentials['client_secret']
        )

        self.respect_source_directory_structure = get_attr(self.config, 'respect_source_directory_structure', True)
        self.use_attributes_to_generate_directory_structure = get_attr(self.config, 'use_attributes_to_generate_directory_structure', True)
        self.source_base_path =  remove_last_slash(get_attr(self.config, 'source_base_path', ''))

       
        
        if (len(str(self.source_base_path)) == 0) and (self.respect_source_directory_structure == True):
            raise Exception('Source base Path is required when Respect Source Directory Structure is true')


         
    def adjust_key_name(self, key):

        if (key[0] == '/'):
            size = len(key)
            print('adjusting key name: ' + key)
            new_key = key[1:size]
            print('adjusting key name: ' + new_key)
            return new_key
        else:
            return key    
        
    def run(self, files: List[AnyStr]):

      target_bucket = self.target_bucket
      target_directory = self.target_directory
      
      respect_source_directory_structure = self.respect_source_directory_structure
      use_attributes_to_generate_directory_structure = self.use_attributes_to_generate_directory_structure

      source_base_path = self.source_base_path

      session = self.session

      results: List[AnyStr] = []

     
      s3 = session.resource('s3')

      bucket = s3.Bucket(target_bucket)

      for file in files: 

            try: 
                

                if ('location' in file):
                    filename = file['location']
                else:
                    filename = file 

                print(f'Saving file {filename}')

                if (respect_source_directory_structure == True):
                    key_filename = ntpath.basename(filename)
                    dir_name = path.dirname(filename)
                    dir_name = dir_name.replace(source_base_path, target_directory) 
                    key = path.join(dir_name,key_filename)
                else:
                    if (use_attributes_to_generate_directory_structure == False or not(('location' in file)) ):
                        key_filename = ntpath.basename(filename)
                        key = path.join(target_directory, key_filename)
                    else:
                        items = file.items()
                        full_path = target_directory
                        key_filename = ntpath.basename(filename)
                        for item in items:
                            if (item[0] != 'location'):
                                id = item[1]
                                full_path = path.join(full_path, id)
                        key = path.join(full_path, key_filename)                     
                        
                key = self.adjust_key_name(key)
                bucket.upload_file(filename, key)
                status = 'OK'
                message = 'File Uploaded Successfully'
               
                

                results.append({'file': file, 'status': status, 'message': message, 'target': key, 'target_bucket':  target_bucket})

            except Exception as err:
                message = str(err)
                print(f'{filename} - Could Not Upload File: {str(err)}')
                status = 'ERR'
                message = message
                results.append({'file': file, 'status': status, 'message': message})
                continue

      return results
      