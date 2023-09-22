import json

def is_jsons(res):
    try:
        json.loads(res)
        return res.json
    except:
        return res.text 
   
       
       
        
   