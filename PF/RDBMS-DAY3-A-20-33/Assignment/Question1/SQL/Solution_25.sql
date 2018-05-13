--select * from item , retailstock;


select itemcode ,descr , price from item  where category = 'B'and  descr like '%Shirt' or descr like '%Skirt';
--select itemcode ,descr , retailstock.unitprice from item , retailstock where item.itemcode = retailstock.itemcode and desc in ('Shirt' , 'Skirt') and category = 'B'  ;