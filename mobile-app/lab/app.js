
Ext.onReady(function(){
    
    
    Ext.create('Ext.Button', {
        cls:'onbutton',
        height:'31%',
        width:'100%',
        //text: 'On',
        scale:'large',
     
        renderTo: Ext.getBody(),
        
        handler: function() {
        
            Ext.Ajax.request({
                
                cors: true,
                useDefaultXhrHeader: false,
                withCredentials: true,
                url: 'http://10.10.14.2:5000/on',
                method: 'GET',
                timeout:5000,
                
                
                success: function (response) {
                    alert('On Toggled!');
                
                },
                failure: function (response) {

                    Ext.Msg.alert('Status', 'Request Failed.');
                    
                    
                }
            });
           
        }
    });

    Ext.create('Ext.Button', {
        cls:'offbutton',
        height:'31%',
        width:'100%',
        //text: 'Off',
        scale:'small',
       
        renderTo: Ext.getBody(),
        
        handler: function() {
        
            Ext.Ajax.request({
                cors: true,
                useDefaultXhrHeader: false,
                withCredentials: true,
                url: 'http://10.10.14.2:5000/off',
                method: 'GET',
                timeout:5000,
                
                
                success: function (response) {
                    alert('Off Toggled!');
                
                },
                failure: function (response) {
                    
                    Ext.Msg.alert('Status', 'Request Failed.');
    
                }
            });
           
        }
    });

    Ext.create('Ext.Button', {
        cls:'blinkbutton',
        height:'31%',
        width:'100%',
        //text: 'Blink',
        scale:'small',
      
        renderTo: Ext.getBody(),
        
        handler: function() {
        
            Ext.Ajax.request({
                cors: true,
                useDefaultXhrHeader: false,
                withCredentials: true,
                url: 'http://10.10.14.2:5000/blink',
                method: 'GET',
                timeout:5000,
                
                
                success: function (response) {
                    alert('Blink Toggled!');
                
                },
                failure: function (response) {
                   
                    Ext.Msg.alert('Status', 'Request Failed.');
                    
                
                }
            });
           
        }
    });


    Ext.create('Ext.Button', {
        cls:'statusbutton',
        height:'31%',
        width:'100%',
        //text: 'Off',
        scale:'small',
       
        renderTo: Ext.getBody(),
        
        handler: function() {
        
            Ext.Ajax.request({
                cors: true,
                useDefaultXhrHeader: false,
                withCredentials: true,
                url: 'http://10.10.14.2:5000/off',
                method: 'GET',
                timeout:5000,
                
                success: function (response) {
                    alert('Off Toggled!');
                
                },
                failure: function (response) {
                    
                    Ext.Msg.alert('Status', 'Request Failed.');
    
                }
            });
           
        }
    });

    
})

