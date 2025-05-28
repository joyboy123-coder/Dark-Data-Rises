SELECT 
*
FROM {{ref('clean_orders')}}
WHERE orderstatus = 'Delivered' 
AND shippedregion = 'North'