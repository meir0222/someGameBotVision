import pyautogui



class InterfaceManager:

    def goToInventory(self):
        self.getTabsWindow()
        # print(list(self.tabsWindow.values())[:-1])
        inv = pyautogui.locateOnScreen('classes/assets/inv.png',region=(list(self.tabsWindow.values())[:-1]),confidence =0.6)
        pyautogui.click((inv.left,inv.top))



    def getTabsWindow(self):
        self.tabsWindow = {'x':pyautogui.locateOnScreen('classes/assets/tabs.png',confidence=0.7).left,
        'y':pyautogui.locateOnScreen('classes/assets/tabs.png',confidence=0.7).top,
        'w': 232,
        'h': 350
        }

        img =   pyautogui.screenshot(region=(self.tabsWindow['x'],
        self.tabsWindow['y'],
        self.tabsWindow['w'],
        self.tabsWindow['h'])  )

        self.tabsWindow['img'] = img  
        
    


        

    def getWorldChat(self):
        self.worldChat = {'x':pyautogui.locateOnScreen('classes/assets/worldChat.png',confidence=0.7).left,
        'y':pyautogui.locateOnScreen('classes/assets/worldChat.png',confidence=0.7).top - 145,
        'w': 518,
        'h': 145
        }
        
        img = pyautogui.screenshot(region=(self.worldChat['x'],
        self.worldChat['y'],
        self.worldChat['w'],
        self.worldChat['h']))

        self.worldChat['img'] = img
        


    def getMiniMap(self):

        self.minimap = {'x':pyautogui.locateOnScreen('classes/assets/minimap.png',confidence=0.7).left,
        'y':pyautogui.locateOnScreen('classes/assets/minimap.png',confidence=0.7).top -  17,
        'w': 213,
        'h': 161
        }
        
        img =   pyautogui.screenshot(region=(self.tabsWindow['x'],
        self.minimap['y'],
        self.minimap['w'],
        self.minimap['h'])  )

        self.minimap['img'] = img  



        
    def getComponenets(self):
        self.getTabsWindow()
        self.getMiniMap()
        self.getWorldChat()

        
    def prntInfo(self):
        print(self.tabsWindow)
        print(self.worldChat)
        print(self.minimap)
        



I = InterfaceManager()
I.goToInventory()

