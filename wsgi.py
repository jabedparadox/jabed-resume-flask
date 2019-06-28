#!/usr/bin/python
#!/usr/bin/python3
#!/usr/bin/env python
#!/usr/bin/env python3

# -*- coding: utf8 -*-
# 
# date                 :- 
# author               :- Md Jabed Ali(jabed)
import sys

project_home = u'/home/jabedparadox/'
if project_home not in sys.path:
    sys.path = [project_home] + sys.path


# import flask app as "application" for WSGI
from app import app as application
