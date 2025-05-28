SELECT
*
FROM {{ref('clean_orders')}}
WHERE orderstatus = 'Shipped'