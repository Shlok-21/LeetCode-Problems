select * from cinema c
where c.description != 'boring' 
and c.id %2 = 1
order by c.rating desc