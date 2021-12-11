# SCD - Slowly Changing Dimension:

Type-0: (retain original)  
  The Type 0 dimension attributes never change,  
  For Example: Date of Birth  
  Type 0 is usually applied to mostly `date` dimension attributes

Type-1: (Overwrite) i.e. FULL-REFRESH Mode  
  This method overwrites old with new data, and therefore does not track historical data,    
  ![image](https://user-images.githubusercontent.com/26399543/145673083-4551f565-5d9a-4a66-a5fb-fcb9db7b6252.png)  
  when supplier_state changes, it will override the existing value w/o maintaing the history,  
  so its' easy to manage but losing the history  
  ![image](https://user-images.githubusercontent.com/26399543/145673097-a166fcc9-f13c-4d6c-b25a-adbdfff8d968.png)

Type-2: (add new row)  
  This method tracks historical data by creating multiple records for a given natural key:  
    
    Approach-1:  
  ![image](https://user-images.githubusercontent.com/26399543/145673166-dca54d9a-9247-41d7-8aec-9099a8abe771.png)  
    Approach-2:  
  ![image](https://user-images.githubusercontent.com/26399543/145673220-0bf736c7-d42f-492f-8006-ce350035e314.png)  
    Approach-3:  
  ![image](https://user-images.githubusercontent.com/26399543/145673232-a4461d18-0bcc-4558-b3bf-89ff8b3f9e49.png)  

Type-3: (add new attribute)  
  This method tracks changes using separate columns and preserves limited history.
  ![image](https://user-images.githubusercontent.com/26399543/145673331-76b65600-b2fd-4e7e-946b-ba4d8a6bc215.png)

Type-4: (add history table) i.e. FULL-REFRESH-KEEP-HISTORY Mode  
  The Type 4 method is usually referred to as using "history tables", where one table keeps the current data,  
  and an additional table is used to keep a record of some or all changes.  
  ![image](https://user-images.githubusercontent.com/26399543/145673415-a7e501f6-1bd6-4722-bd2e-04e2bf72f8a6.png)
  
Type-5  
  combination of type-4 and type-1, hence it is named type-5  
Type-6 (combined approach)  
  The Type 6 method combines the approaches of types 1, 2 and 3 (1 + 2 + 3 = 6)  
Type-7 (hybrid)
  This method places both the surrogate key and the natural key into the fact table.  

We could apply the above types, to the attributes of the dimension tables.  
and not on the fact tables, as fact tables are mostly static in nature.  

**Reference:**  
1. https://en.wikipedia.org/wiki/Slowly_changing_dimension

