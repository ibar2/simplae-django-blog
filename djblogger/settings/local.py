from .base import *


# adding the template folder to the django project
TEMPLATES[0]['DIRS'].append(os.path.join(BASE_DIR, "templates"))
