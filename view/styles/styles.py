BUTTON_STYLE = """
QPushButton {
    background-color: #603A81;  
    border: 2px solid #3E1562;  
    border-radius: 10px;        
    color: white;               
    font-size: 16px;            
    font-weight: bold;          
    padding: 10px 20px;         
    text-align: center;         
}

QPushButton:hover {
    background-color: #3E1562;  
    border: 2px solid #310856;  
}

QPushButton:pressed {
    background-color: #2F0653;  
    border: 2px solid #28004B;  
}
"""

COMBO_BOX_STYLE = """
QComboBox {
    background-color: #f0f0f0;         
    border: 2px solid #3E1562;       
    border-radius: 5px;             
    padding: 5px;                 
    font-size: 14px;               
    color: #333;                     
}

QComboBox::drop-down {
    subcontrol-origin: padding;
    subcontrol-position: top right;
    width: 0px;                       
    border: none;                      
}

QComboBox::down-arrow {
    image: none;                      
    width: 0px;                        
    height: 0px;                   
}

QComboBox QAbstractItemView {
    background-color: #f0f0f0;       
    border: 2px solid #3E1562;       
    selection-background-color: #3E1562; 
    selection-color: white;           
    padding: 5px;                      
    font-size: 14px;                  
}
"""

TEXT_BROWSER_STYLE = """
QTextBrowser {
    background-color: #f9f9f9;      
    border: 2px solid #4D1C77;         
    border-radius: 5px;            
    padding: 10px;                    
    font-size: 14px;                 
    color: #333;                    
}

QTextBrowser:focus {
    border: 2px solid #28004B;         
}
"""

TEXT_EDIT_STYLE = """
QTextEdit {
    background-color: #f9f9f9;         
    border: 2px solid #4D1C77;        
    border-radius: 5px;                
    padding: 10px;                    
    font-size: 14px;                    
    color: #333;                       
}

QTextEdit:focus {
    border: 2px solid #28004B;         
}
"""

BACKGROUND_COLOR = """
    QWidget {
        background-color: #9788B6;
    }
"""