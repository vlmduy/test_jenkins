import os, sys
from google.appengine.ext import vendor

# Add any libraries installed in the "lib" folder.
vendor.add('lib')
if os.name == 'nt':
    os.name = None
    sys.platform = ''