import os

clean_container = 'docker rm -f `docker ps -a | grep \'api_calculator\' | awk \'{print $1;}\'`'
print(str(os.system (clean_container)))

clean_untagged_image = 'docker rmi `docker images | grep \'api_calculator\' | awk \'{ print $3; }\'`'
print(str(os.system(clean_untagged_image)))

