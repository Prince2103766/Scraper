import eel
import requests


eel.init("web")


@eel.expose
def template(x):
         page=requests.get(x)
         v=page.content
         with open("web/protocol.txt", "w") as d:
               d.write(str(v))
             
eel.start("index.html")
            

      
        
    
    

