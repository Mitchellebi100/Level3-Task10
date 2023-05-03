import os
import sys
import django
sys.path.insert(0 ,os.path.abspath(' .. '))
os.environ['DJANGO_SETTINGS_MODULE'] = 'ecom_project.settings'
django.setup()