.model small
.stack 100h
.data
.code
    main proc
    mov ax, @data 
    mov ds , ax 
    
    mov ah,1        ;service routine to take input
    int 21h      
    
    mov bl, al
               
             
   
    mov dl, 0Ah      ;syntax = destination , source
    mov ah, 2
    int 21h 
    
    mov dl, 0Dh
    mov ah,2
    int 21h    
     
    mov dl,bl   
    
   
      
    mov ah,2     
    int 21h                
            
    mov ah, 4ch
    int 21h 
    
    endp
    end main