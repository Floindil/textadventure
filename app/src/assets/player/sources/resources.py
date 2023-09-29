from ...names_values import resources as r

class Resources:
    resources= {
        r[0]: 0,
        r[1]: 0
    }
    
    @classmethod
    def update_resource(cls,value:int,resource:int):
        current= cls.resources.get(r[resource])
        new= current+ value
        if new< 0: new= 0
        cls.resources.update({r[resource]: new})
        
    