# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 07:49:16 2022

@author: franc
"""

from cloopui_server import *
import json
import threading


this_dir, this_filename = os.path.split(__file__)  # Get path of data.pkl
template_path = os.path.join(this_dir, 'template.html')


def is_port_in_use(port: int) -> bool:
    import socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('localhost', port)) == 0


class plot:
    
    def __init__(self):
        self.variables = []
        self.units = []

    def add_line(self,var_name,units=""):
        self.variables.append(var_name)
        self.units.append(units)



class webui:
    
    
    def __init__(self):
        self.components = []
        self.send_data = {}
      
        
    def add_plot(self):
        self.components.append(plot())
        return self.components[-1]
    
    
    def add_slider(self,var_name,default=50,min_val=0,max_val=100,step=1,unit=""):
        self.components.append( {"var":var_name,
                                 "type":"slider",
                                 "min_val":min_val,
                                 "max_val":max_val,
                                 "step":step,
                                 "unit":unit,
                                 "default":default} )
        self.send_data[var_name] = default
    
    
    def add_number(self,var_name,unit=""):
        self.components.append( {"var":var_name,
                                 "type":"number",
                                 "unit":unit} )
        
        
    def add_button(self,var_name,default=False):
        self.components.append( {"var":var_name,"type":"button","default":default} )
        self.send_data[var_name] = default
        
        
    def add_select(self,var_name,options):
        self.components.append( {"var":var_name,"type":"select","options":options})
        self.send_data[var_name] = options[0]
        
        
    def create_page(self,page_name,short_name):
        send_data = json.dumps(self.send_data)
        
        html_code = ""
        interval_code = ""
        
        count = 0
        for comp in self.components:
            if( isinstance(comp, dict) ): # All except plot
                if(comp["type"] == "number"):
                    html_code = html_code + f"""
                        <div class="row">
                            <p style="text-align:center;font-size:130%;margin-bottom:0px;">{comp["var"]}</p>
                            <p style="text-align:center;font-size:140%;margin-top:5px;"><b><span id="nb_{count}"></span></b></p>
                        </div>
                    """
                    interval_code = interval_code + f"""
                        number("nb_{count}","{comp["var"]}");    
                    """
                
                elif(comp["type"] == "button"):
                    cl = "negative"
                    if comp["default"]:
                        cl = "positive"
                    
                    html_code = html_code + f"""
                    <div class="row">
                        <div id="bool_{comp["var"]}" class="{cl} btn" style="font-size:140%;width:100%;height:30px;text-align:center;padding-top:5px;" onclick="send_data['{comp["var"]}'] = send_data['{comp["var"]}']==false; change_bool('{comp["var"]}')">
                            {comp["var"]}
                        </div>
                    </div>
                    """
                
                elif(comp["type"]== "slider"):
                    
                    html_code = html_code + f"""
                    <div class="row">
                        <p style="text-align:center;font-size:120%;margin-bottom:5px;">{comp["var"]}</p>
                            <input type="range" min="{comp["min_val"]}" max="{comp["max_val"]}" step="{comp["step"]}" value="{comp["default"]}" class="slider" oninput="$('#slider_val_{count}').html(this.value);" onchange="send_data['{comp["var"]}'] = (this.value); $('#slider_val_{count}').html(this.value)">
                        <p style="text-align:center;font-size:110%;margin-top:5px;"><span id="slider_val_{count}" >{comp["default"]}</span></p>
                    </div>
                    """
                
                elif(comp["type"] == "select"):
                    
                    html_code = html_code + f"""
                    <div class="row">
                        <p style="text-align:center;font-size:120%;margin-bottom:5px;">{comp["var"]}</p>
                        <select id="{comp["var"]}" onchange='change_select("{comp["var"]}")'>
                    """
                    for option in comp["options"]:
                        html_code = html_code + f"""
                            <option value="{option}">{option}</option>
                        """
                    html_code = html_code + """
                        </select></div>
                    """
                
                
            else: # PLOT
                html_code = html_code + f"""
                    <div class="row">
                        <div id="plot_{count}" style="width:100%;height:400px;"></div>
                    </div>
                """
                list_var = json.dumps(comp.variables)
                interval_code = interval_code + f"""
                    plot("plot_{count}",{list_var});
                """
            
            count += 1
            
        page = open(template_path).read()
        page = page.replace("{{send_data}}",send_data).\
                 replace("{{interval_code}}",interval_code).\
                 replace("{{html_code}}",html_code).\
                 replace("{{foldername}}",short_name)
        
        file = open(page_name + ".html","w")
        file.write(page)
        file.close()



    def webpage(self,name):        
        self.create_page(name+"/index",name)
                


