import os

class resource():
    def __init__(self, resourceName: str, webside: bool):
        self.resource = resourceName
        self.webside = webside
    
    def create(self):
        try:
            os.mkdir(self.resource)
            os.chdir(self.resource)
            os.mkdir("client-side")
            os.mkdir("server-side")
 
            with open("fxmanifest.lua","x") as fxmanifest:
                print("[!] FXMANIFEST ADD TO RESOURCE")
                if self.webside:
                    os.mkdir("web-side")
                    fxmanifest.write('fx_version "cerulean"\ngame "gta5"\n\nui_page "web-side/index.html"\n\nfiles { \n    "web-side/*,\n    "web-side/**/*"\n}\n\nclient_scripts { \n    "@vrp/lib/utils.lua",\n    "client-side/*" \n}\n\nserver_scripts { \n    "@vrp/lib/utils.lua",\n    "server-side/*" \n}')
                    os.chdir("web-side")
                    open("index.html","x")
                    open("main.js","x")
                    open("style.css","x")
                    os.chdir("..")
                else:
                    fxmanifest.write('fx_version "cerulean"\ngame "gta5"\n\nclient_scripts { \n    "@vrp/lib/utils.lua",\n    "client-side/*" \n}\n\nserver_scripts { \n    "@vrp/lib/utils.lua",\n    "server-side/*" \n}')
            os.chdir("client-side")
            
            with open("client.lua","x") as client:
                client.write('local Tunnel = module("vrp","lib/Tunnel")\nlocal Proxy = module("vrp","lib/Proxy")\nlocal vSERVER = Tunnel.getInterface(GetCurrentResourceName())')
                print("[!] CLIENT ADD TO RESOURCE")
            
            os.chdir("..")
            os.chdir("server-side")

            with open("server.lua","x") as server:
                server.write('local Tunnel = module("vrp","lib/Tunnel")\nlocal Proxy = module("vrp","lib/Proxy")\nlocal pTz = {}\nTunnel.bindInterface(GetCurrentResourceName(),pTz)')
                print("[!] SERVER ADD TO RESOURCE")
            
        except Exception as error:
            print(error)
