import tinys3
import time

conn = tinys3.Connection('AKIAJOPLNA4GSIA2BKEA','+1gyTjTua9ym7yMPim/Bo9mNBbaRnoyo7jOfO6Sy',tls=True)
f = open('/home/marlon/ionic/clodoo-ionic/python-server/server.py','rb')

if conn.upload(time.strftime("%H:%M:%S") + '-server.py',f,'falconsoft-3d'):
    print "Subido"