--	How many different species of mushroom are there, if a species is identified by the attributes 1-20?

select 
    count(1) 
from (
        select 
            distinct cap_shape,
            cap_color,
            odor,
            gill_size,
            gill_color,
            stalk_color_above_ring,
            veil_color,
            ring_type,
            spore_print_color
        FROM 
        mushrooms
    ) as x
--53


--	Does habitat and cap-color correlate?


SELECT 
    corr(
        case  habitat 
                when 'waste' then 1  
                when 'leaves'  then 2
                when 'woods'  then 3
                when 'n/a'  then 4
                when 'urban'  then 5
                when 'meadows'  then 6
                when 'paths'  then 7
                when 'grasses'  then 8
                else -98 
        end, 

        case cap_color 
                when 'yellow' then 10 
                when 'n/a' then 20
                when 'gray' then 30 
                else -99 
            end
	 )
from mushrooms
-- 0.11675767341216305
-- less correlation

--	Considering a specific geographical point, what colours should we be able to see in the 10 km around it?
select * from findcolors(-75.5697,-2.25322, 10)
